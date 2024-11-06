package main

import (
	"fmt"
	"html/template"
	"net/http"
	"strconv"
)

// home handler function writing bytes to a slice that already has a response body
// it's a method defined against the application struct
func (app *application) home(w http.ResponseWriter, r *http.Request) {
	// If the request URL path is not "/" then return a 404 not found response
	if r.URL.Path != "/" {
		app.notFound(w)
		return
	}

	// Initialize a slice containing the paths to the two files. It's important
	// to note that the file containing our base template must be the *first*
	// file in the slice.
	files := []string{
		"./ui/html/base.tmpl.html",
		"./ui/html/partials/nav.tmpl.html",
		"./ui/html/pages/home.tmpl.html",
	}

	// We use the template.ParseFiles() function to read the template file into a new template set
	// If there is an error we log the error and return a 500 internal server error response
	// w.Write([]byte("Hello from home"))
	ts, err := template.ParseFiles(files...)
	if err != nil {
		app.serverError(w, err)
		return
	}

	// We use the execute method on the template to write the template content as the response body.
	// The last parameter to execute is nil, which means we are not passing any data to the template for now
	// err = ts.Execute(w, nil)
	err = ts.ExecuteTemplate(w, "base", nil)
	if err != nil {
		app.serverError(w, err)
		http.Error(w, "Internal Server Error", 500)
	}
}

func (app *application) snippetView(w http.ResponseWriter, r *http.Request) {
	// I extract the value of the ID from the query and try to convert it to integer
	// If it cannot be converted or is less than 1, I return a 404 not found response
	id, err := strconv.Atoi(r.URL.Query().Get("id"))

	if err != nil || id < 1 {
		app.notFound(w)
		return
	}
	// w.Write([]byte("Display the snippet"))
	fmt.Fprintf(w, "Display a specific snipper with ID %d", id)
}

func (app *application) snippetCreate(w http.ResponseWriter, r *http.Request) {
	// r.Method is an HTTP method, if it's not POST then return a 405 method not allowed response
	// if r.Method != "POST" {
	if r.Method != http.MethodPost {
		w.Header().Set("Allow", http.MethodPost)
		// w.WriteHeader(405)
		// w.Write([]byte("Method not allowed"))
		// Same as above (http.StatusMethodNotAllowed = 405)
		app.clientError(w, http.StatusMethodNotAllowed)
		return
	}

	w.Write([]byte("Create the snippet"))
}

func headerMap(w http.ResponseWriter) {
	w.Header().Set("Cache-Control", "public, max-age=31536000")

	// w.Header().Add("Cache-Control", "public")
	// w.Header().Add("Cache-Control", "max-age=31536000")
}

func downloadHandler(w http.ResponseWriter, r *http.Request) {
	// Note: this doesn't automatically sanitize the file name, so you should do that
	http.ServeFile(w, r, "./ui/static/file.zip")
}
