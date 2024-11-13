package main

import (
	"html/template"
	"path/filepath"

	"alienix2.letsgo/internal/models"
)

// Define an application struct that contains any dynamic data that the handlers may need
type templateData struct {
	Snippet  *models.Snippet
	Snippets []*models.Snippet
}

// Function to store the template in a cache
func newTemplateCache() (map[string]*template.Template, error) {
	// Initializea map cache
	cache := map[string]*template.Template{}

	// Use the filepath.Glob() function to get a slice of all filepath matching
	// the pattern "./ui/html/*.page.tmpl.html"
	pages, err := filepath.Glob("./ui/html/pages/*.tmpl.html")
	if err != nil {
		return nil, err
	}

	// Loop through the pages one by one
	for _, page := range pages {
		// Extract the file name and put it in the variable
		name := filepath.Base(page)

		// Create a slice with all the filepaths including the page
		files := []string{
			"./ui/html/base.tmpl.html",
			"./ui/html/partials/nav.tmpl.html",
			page,
		}
		// Parse the files and put them in the template set
		ts, err := template.ParseFiles(files...)
		if err != nil {
			return nil, err
		}
		// Add template to the globe
		cache[name] = ts
	}

	// I return the map
	return cache, nil
}
