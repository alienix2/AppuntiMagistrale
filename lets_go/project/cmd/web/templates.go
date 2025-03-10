package main

import (
	"html/template"
	"io/fs"
	"path/filepath"
	"time"

	"alienix2.letsgo/internal/models"
	"alienix2.letsgo/ui"
)

// Define an application struct that contains any dynamic data that the handlers may need
type templateData struct {
	CSRFToken       string
	Flash           string
	Form            any
	Snippet         *models.Snippet
	Snippets        []*models.Snippet
	CurrentYear     int
	IsAuthenticated bool
}

// humanDate function with a date formatted in human readable format
func humanDate(t time.Time) string {
	if t.IsZero() {
		return ""
	}

	return t.UTC().Format("02 Jan 2006 at 15:04")
}

// Inizialize the template.FuncMap onject and store in a global variable
// This is a string-keyed map which maps the names of our custom template functions
// to the functions themselves
var functions = template.FuncMap{
	"humanDate": humanDate,
}

// Function to store the template in a cache
func newTemplateCache() (map[string]*template.Template, error) {
	// Initialize a map cache
	cache := map[string]*template.Template{}

	// Use the filepath.Glob() function to get a slice of all filepath matching
	// the pattern "./ui/html/*.page.tmpl.html"
	// pages, err := filepath.Glob("./ui/html/pages/*.tmpl.html")
	pages, err := fs.Glob(ui.Files, "html/pages/*.tmpl.html")
	if err != nil {
		return nil, err
	}

	// Loop through the pages one by one
	for _, page := range pages {
		// Extract the file name and put it in the variable
		name := filepath.Base(page)

		// // Create a slice with all the filepaths including the page
		// files := []string{
		// 	"./ui/html/base.tmpl.html",
		// 	"./ui/html/partials/nav.tmpl.html",
		// 	page,
		// }
		// // Parse the files and put them in the template set
		// ts, err := template.ParseFiles(files...)
		// if err != nil {
		// 	return nil, err
		// }

		// // Parse the base template into a template set
		// ts, err := template.New(name).Funcs(functions).ParseFiles("./ui/html/base.tmpl.html")
		//
		//
		// if err != nil {
		// 	return nil, err
		// }
		//
		// // Call parseGlob on the template to add any partials
		// ts, err = ts.ParseGlob("./ui/html/partials/*.tmpl.html")
		// if err != nil {
		// 	return nil, err
		// }
		//
		// // I call the ParseFiles method on the template set to add the page template
		// ts, err = ts.ParseFiles(page)
		// if err != nil {
		// 	return nil, err
		// }

		// I use ParseFS instead of ParseFiles
		patterns := []string{
			"html/base.tmpl.html",
			"html/partials/*tmpl.html",
			page,
		}
		ts, err := template.New(name).Funcs(functions).ParseFS(ui.Files, patterns...)
		if err != nil {
			return nil, err
		}

		// Add template to the globe
		cache[name] = ts
	}

	// I return the map
	return cache, nil
}
