package main

import (
	"net/http"
	"path/filepath"

	"github.com/julienschmidt/httprouter"
	"github.com/justinas/alice"
)

// The routes() method returns a servermux with our application routes
func (app *application) routes() http.Handler {
	// http.NewServerMux() initializes a new servermux, then registers the home as the handler function for the / route
	// mux := http.NewServeMux()
	router := httprouter.New()

	// Create a file server which serves files out of the ./ui/static directory
	fileServer := http.FileServer(neuteredFileSystem{http.Dir("./ui/static/")})

	// Use mux.Handle() to register the file server as the handler for all URL paths that start with "/static/"
	// For matching requests, we strip the "/static" prefix before the request reaches the file server
	// mux.Handle("/static/", http.StripPrefix("/static", fileServer))
	//
	// mux.HandleFunc("/", app.home)
	// mux.HandleFunc("/snippet/view", app.snippetView)
	// mux.HandleFunc("/snippet/create", app.snippetCreate)

	router.Handler(http.MethodGet, "/static/*filepath", http.StripPrefix("/static", fileServer))
	// router.HandlerFunc(http.MethodGet, "/home", app.home)

	// I create a new middleWare chain for dynamic routes
	dynamic := alice.New(app.sessionManager.LoadAndSave)

	// Note: if using app methods directly, use router.HandlerFunc instead of router.Handler
	router.Handler(http.MethodGet, "/", dynamic.ThenFunc(app.home))
	router.Handler(http.MethodGet, "/snippet/view/:id", dynamic.ThenFunc(app.snippetView))
	router.Handler(http.MethodGet, "/snippet/create", dynamic.ThenFunc(app.snippetCreate))
	router.Handler(http.MethodPost, "/snippet/create", dynamic.ThenFunc(app.snippetCreatePost))

	// Routes for user authentication
	router.Handler(http.MethodGet, "/user/signup", dynamic.ThenFunc(app.userSignup))
	router.Handler(http.MethodPost, "/user/signup", dynamic.ThenFunc(app.userSignupPost))
	router.Handler(http.MethodGet, "/user/login", dynamic.ThenFunc(app.userLogin))
	router.Handler(http.MethodPost, "/user/login", dynamic.ThenFunc(app.userLoginPost))
	router.Handler(http.MethodPost, "/user/logout", dynamic.ThenFunc(app.userLogoutPost))

	// return app.recoverPanic(app.logRequest(secureHeaders(mux)))
	standard := alice.New(app.recoverPanic, app.logRequest, secureHeaders).Then(router)
	return standard
}

type neuteredFileSystem struct {
	fs http.FileSystem
}

func (nfs neuteredFileSystem) Open(path string) (http.File, error) {
	f, err := nfs.fs.Open(path)
	if err != nil {
		return nil, err
	}

	s, err := f.Stat()
	if err != nil {
		return nil, err
	}

	if s.IsDir() {
		index := filepath.Join(path, "index.html")
		if _, err := nfs.fs.Open(index); err != nil {
			closeErr := f.Close()
			if closeErr != nil {
				return nil, closeErr
			}
			return nil, err
		}
	}

	return f, nil
}

// func neuter(next http.Handler) http.Handler {
// 	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
// 		if strings.HasSuffix(r.URL.Path, "/") {
// 			http.NotFound(w, r)
// 			return
// 		}
//
// 		next.ServeHTTP(w, r)
// 	})
// }
