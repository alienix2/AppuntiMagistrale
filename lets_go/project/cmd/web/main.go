package main

import (
	"flag"
	"log"
	"net/http"
	"os"
)

// Define an application strouct that holds the application-wide dependencies. This includes the info and error loggers
// at the moment but will include more after
type application struct {
	errorLog *log.Logger
	infoLog  *log.Logger
}

func main() {
	// Define a command-line flag with the name 'addr' with a default of 4000 and a hint
	addr := flag.String("addr", ":4000", "HTTP network port")

	// We need to parse the command-line flag and assign it to the addr. This checks for errors and must be done
	// before using the variable
	flag.Parse()

	// Add an error and info log
	infoLog := log.New(os.Stdout, "INFO\t", log.Ldate|log.Ltime)
	// In the error I add the info on the file and line where the error occurred
	errorLog := log.New(os.Stderr, "ERROR\t", log.Ldate|log.Ltime|log.Lshortfile)
	// Instantiate an application struct containing the logger
	app := &application{
		errorLog: errorLog,
		infoLog:  infoLog,
	}

	// Inizialize an http.Server struct to use our loggers and serverMux
	srv := &http.Server{
		Addr:     *addr,
		ErrorLog: errorLog,
		Handler:  app.routes(),
	}

	// http.ListenAndServe() starts the server on port 4000 and is an http server. Uses the servermux we created
	// If http.ListenAndServe() returns an error, log.Fatal() will log the error and exit the program. All the error are non-nil
	app.infoLog.Printf("Starting server on %s", *addr)
	err := srv.ListenAndServe()
	app.errorLog.Fatal(err)
}
