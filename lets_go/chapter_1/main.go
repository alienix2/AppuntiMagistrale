package main

import (
	"log"
	"net/http"
)

// home handler function writing bytes to a slice that already has a response body
func home(w http.ResponseWriter, r *http.Request) {
	// If the request URL path is not "/" then return a 404 not found response
	if r.URL.Path != "/" {
		http.NotFound(w, r)
		return
	}
	w.Write([]byte("Hello from home"))
}

func snippetView(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Display the snippet"))
}

func snippetCreate(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Create the snippet"))
}

func main() {
	// http.NewServerMux() initializes a new servermux, then registers the home as the handler function for the / route
	mux := http.NewServeMux()

	mux.HandleFunc("/", home)
	mux.HandleFunc("/snippet/view", snippetView)
	mux.HandleFunc("/snippet/create", snippetCreate)
	// http.ListenAndServe() starts the server on port 4000 and is an http server. Uses the servermux we created
	// If http.ListenAndServe() returns an error, log.Fatal() will log the error and exit the program. All the error are non-nil

	log.Print("Starting server on :4000")
	err := http.ListenAndServe(":4000", mux)
	log.Fatal(err)
}
