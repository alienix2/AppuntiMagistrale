package main

import (
	"fmt"
	"net/http"
	"runtime/debug"
)

// serverError helper writes an error message and stack trace to the errorLog
// then sends a generic 500 Internal Server Error response to the user
func (app *application) serverError(w http.ResponseWriter, err error) {
	trace := fmt.Sprintf("%s\n%s", err.Error(), debug.Stack())
	app.errorLog.Output(2, trace)

	http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
}

// clientError helper sends a specific status code and corresponding description
// to the user. We'll use this later in our handlers to send responses like 400 Bad Request
func (app *application) clientError(w http.ResponseWriter, status int) {
	http.Error(w, http.StatusText(status), status)
}

// notFound helper is a convenience wrapper around clientError which sends a 404 Not Found
func (app *application) notFound(w http.ResponseWriter) {
	app.clientError(w, http.StatusNotFound)
}

func (app *application) render(w http.ResponseWriter, status int, page string, data *templateData) {
	// Retrieve the template from the cache based on the page name.
	// If it doesn't exist, call the serverError helper method to log the error
	ts, ok := app.templateCache[page]
	if !ok {
		err := fmt.Errorf("The template %s does not exist", page)
		app.serverError(w, err)
		return
	}

	// Write the status code
	w.WriteHeader(status)

	// Execute the template set, passing in any dynamic data.
	// If there is an error, call the serverError helper method to log the error
	err := ts.ExecuteTemplate(w, "base", data)
	if err != nil {
		app.serverError(w, err)
	}
}
