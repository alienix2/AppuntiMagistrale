package main

import (
	"context"
	"fmt"
	"net/http"

	"github.com/justinas/nosurf"
)

func secureHeaders(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		headers := map[string]string{
			"Content-Security-Policy": "default-src 'self'; style-src 'self' fonts.googleapis.com; font-src fonts.gstatic.com",
			"Referrer-Policy":         "origin-when-cross-origin",
			"X-Content-Type-Options":  "nosniff",
			"X-Frame-Options":         "deny",
			"X-XSS-Protection":        "0",
		}
		for key, value := range headers {
			w.Header().Add(key, value)
		}

		next.ServeHTTP(w, r)
	})
}

// This function is defined on application so that it can read infos
// about the application
func (app *application) logRequest(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		app.infoLog.Printf("%s - %s %s %s", r.RemoteAddr, r.Proto, r.Method, r.URL.RequestURI())

		next.ServeHTTP(w, r)
	})
}

func (app *application) recoverPanic(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// The deferred function will always run in the event of a panic as Go unwinds the stack
		defer func() {
			// Use the builtin recover function to check if there has been a panic or not
			if err := recover(); err != nil {
				// I set a "Connection: close" header on the response
				w.Header().Set("Connection", "close")

				// I call the serverError helper method to return a 500 Internal Server Error response
				app.serverError(w, fmt.Errorf("%s", err))
			}
		}()

		next.ServeHTTP(w, r)
	})
}

func (app *application) requireAuthentication(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// If the user not authenticated, redirect to the login page and
		// return from the middleware chain so that no other middleware are
		// executed
		if !app.isAuthenticated(r) {
			http.Redirect(w, r, "/user/login", http.StatusSeeOther)
			return
		}

		// Otherwise I set a set the "Cache-Control: no-store" header so that pages
		// require authentication are not stored in the user's browser cache
		w.Header().Add("Cache-Control", "no-store")

		// And call the next handler in the chain
		next.ServeHTTP(w, r)
	})
}

// noSurf middleware using a customized cookie with secure, path and httponly attributes
func noSurf(next http.Handler) http.Handler {
	csrfHandler := nosurf.New(next)

	csrfHandler.SetBaseCookie(http.Cookie{
		HttpOnly: true,
		Secure:   true,
		Path:     "/",
	})

	return csrfHandler
}

// Check if a user is authenticated
func (app *application) authenticate(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// I retrieve the authenticatedUserID value from the session using the
		// GetInt() method. If 0 user is not authenticated and other handlers are called
		id := app.sessionManager.GetInt(r.Context(), "authenticatedUserID")
		if id == 0 {
			next.ServeHTTP(w, r)
			return
		}

		// Otherwise we check if in the database there is a user with the id
		exists, err := app.users.Exists(id)
		if err != nil {
			app.serverError(w, err)
			return
		}

		// If a matching user is found then the user is authorized, we create a copy
		// of the request and assign it to r
		if exists {
			ctx := context.WithValue(r.Context(), isAuthenticatedKey, true)
			r = r.WithContext(ctx)
		}

		// After that I call the next handler
		next.ServeHTTP(w, r)
	})
}
