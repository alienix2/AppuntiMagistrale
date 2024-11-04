package main

import (
	"log"
	"net/http"
)

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
