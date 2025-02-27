package main

import (
	"crypto/tls"
	"database/sql"
	"flag"
	"html/template"
	"log"
	"net/http"
	"os"
	"time"

	"alienix2.letsgo/internal/models"
	"github.com/alexedwards/scs/mysqlstore"
	"github.com/alexedwards/scs/v2"
	"github.com/go-playground/form/v4"
	_ "github.com/go-sql-driver/mysql"
)

// Define an application strouct that holds the application-wide dependencies. This includes the info and error loggers
// at the moment but will include more after
type application struct {
	errorLog       *log.Logger
	infoLog        *log.Logger
	snippets       models.SnippetModelInterface
	users          models.UserModelInterface
	templateCache  map[string]*template.Template
	formDecoder    *form.Decoder
	sessionManager *scs.SessionManager
}

func main() {
	// Define a command-line flag with the name 'addr' with a default of 4000 and a hint
	addr := flag.String("addr", ":4000", "HTTP network port")
	// Define a command-line flag with the name 'dsn' with a default of 'web:pass@/snippetbox?parseTime=true' and a hint
	dsn := flag.String("dsn", "web:pass@/snippetbox?parseTime=true", "MySQL data source name")

	// We need to parse the command-line flag and assign it to the addr. This checks for errors and must be done
	// before using the variable
	flag.Parse()

	// Add an error and info log
	infoLog := log.New(os.Stdout, "INFO\t", log.Ldate|log.Ltime)
	// In the error I add the info on the file and line where the error occurred
	errorLog := log.New(os.Stderr, "ERROR\t", log.Ldate|log.Ltime|log.Lshortfile)
	// Instantiate an application struct containing the logger

	// I create an instance of a DB
	db, err := openDB(*dsn)
	if err != nil {
		errorLog.Fatal(err)
	}

	// I defer the closure of the db connection so it closes before exiting the main function
	defer db.Close()

	// Initialize a new template cache
	templateCache, err := newTemplateCache()
	if err != nil {
		errorLog.Fatal(err)
	}

	// Inizialize the form decoder
	formDecoder := form.NewDecoder()

	// Initialize a new session manager
	sessionManager := scs.New()
	sessionManager.Store = mysqlstore.New(db)
	sessionManager.Lifetime = 24 * time.Hour

	// I use the secure attribute for the session cookie
	sessionManager.Cookie.Secure = true

	app := &application{
		errorLog:       errorLog,
		infoLog:        infoLog,
		snippets:       &models.SnippetModel{DB: db},
		users:          &models.UserModel{DB: db},
		templateCache:  templateCache,
		formDecoder:    formDecoder,
		sessionManager: sessionManager,
	}

	// I change the TLS setting to optimize it (OPTIONAL)
	tlsConfig := &tls.Config{
		CurvePreferences: []tls.CurveID{tls.X25519, tls.CurveP256},
	}

	// Inizialize an http.Server struct to use our loggers and serverMux
	srv := &http.Server{
		Addr:      *addr,
		ErrorLog:  errorLog,
		Handler:   app.routes(),
		TLSConfig: tlsConfig,

		// Server timeouts
		IdleTimeout:  time.Minute,
		ReadTimeout:  5 * time.Second,
		WriteTimeout: 10 * time.Second,
	}

	// http.ListenAndServe() starts the server on port 4000 and is an http server. Uses the servermux we created
	// If http.ListenAndServe() returns an error, log.Fatal() will log the error and exit the program. All the error are non-nil
	infoLog.Printf("Starting server on %s", *addr)
	// err = srv.ListenAndServe()

	// I use the ListenAndServeTLS() method to start the HTTPS server. This method takes the path to the TLS certificate
	err = srv.ListenAndServeTLS("./tls/cert.pem", "./tls/key.pem")

	errorLog.Fatal(err)
}

// This function wraps the sql.Open() function and returns a sql.DB connection pool for a DSN
func openDB(dsn string) (*sql.DB, error) {
	db, err := sql.Open("mysql", dsn)
	if err != nil {
		return nil, err
	}

	if err = db.Ping(); err != nil {
		return nil, err
	}

	return db, nil
}
