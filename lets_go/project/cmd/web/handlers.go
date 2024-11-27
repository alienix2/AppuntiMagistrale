package main

import (
	"errors"
	"fmt"
	"net/http"
	"strconv"

	"alienix2.letsgo/internal/models"
	"alienix2.letsgo/internal/validator"
	"github.com/go-playground/form/v4"
	"github.com/julienschmidt/httprouter"
)

// Note: the form: is necessary to map the form fields to the struct fields, using the library
type snippetCreateForm struct {
	Content             string     `form:"content"`
	Title               string     `form:"title"`
	validator.Validator `form:"-"` // Embedding
	Expires             int        `form:"expires"`
	// FieldErrors map[string]string
}

// home handler function writing bytes to a slice that already has a response body
// it's a method defined against the application struct
func (app *application) home(w http.ResponseWriter, r *http.Request) {
	// If the request URL path is not "/" then return a 404 not found response
	// if r.URL.Path != "/" && r.URL.Path != "/home" {
	// 	app.notFound(w)
	// 	return
	// }

	snippets, err := app.snippets.Latest()
	if err != nil {
		app.serverError(w, err)
		return
	}

	// I call the newTemplateData helper to get a template containing the default data
	// and add the Snippets data to it
	// data := &templateData{Snippets: snippets}
	data := app.newTemplateData(r)
	data.Snippets = snippets

	// I use the renderer
	app.render(w, http.StatusOK, "home.tmpl.html", data)

	// for _, snippet := range snippets {
	// 	fmt.Fprintf(w, "%+v\n", snippet)
	// }

	// Initialize a slice containing the paths to the two files. It's important
	// to note that the file containing our base template must be the *first*
	// file in the slice.
	// files := []string{
	// 	"./ui/html/base.tmpl.html",
	// 	"./ui/html/partials/nav.tmpl.html",
	// 	"./ui/html/pages/home.tmpl.html",
	// }
	//
	// // We use the template.ParseFiles() function to read the template file into a new template set
	// // If there is an error we log the error and return a 500 internal server error response
	// // w.Write([]byte("Hello from home"))
	// ts, err := template.ParseFiles(files...)
	// if err != nil {
	// 	app.serverError(w, err)
	// 	return
	// }
	//
	// // Create an instance of a templateData struct holding the snippets data
	// data := &templateData{Snippets: snippets}
	//
	// // We use the execute method on the template to write the template content as the response body.
	// // The last parameter to execute is nil, which means we are not passing any data to the template for now
	// // err = ts.Execute(w, nil)
	// err = ts.ExecuteTemplate(w, "base", data)
	// if err != nil {
	// 	app.serverError(w, err)
	// }
}

// func (app *application) snippetView(w http.ResponseWriter, r *http.Request) {
// 	// I extract the value of the ID from the query and try to convert it to integer
// 	// If it cannot be converted or is less than 1, I return a 404 not found response
// 	id, err := strconv.Atoi(r.URL.Query().Get("id"))
//
// 	if err != nil || id < 1 {
// 		app.notFound(w)
// 		return
// 	}
//
// 	// We use te SnippetModel.Get() method to retrieve the data for a specific record based on its ID
// 	// If no matching record is found, we return a 404 not found response
// 	snippet, err := app.snippets.Get(id)
// 	if err != nil {
// 		if errors.Is(err, models.ErrNoRecord) {
// 			app.notFound(w)
// 		} else {
// 			app.serverError(w, err)
// 		}
// 		return
// 	}
//
// 	// I create an instance of a templateData struct containing the snippet data
// 	// and pass it to the render method
// 	data := app.newTemplateData(r)
// 	data.Snippet = snippet
//
// 	// I use the renderer
// 	app.render(w, http.StatusOK, "view.tmpl.html", data)
// 	//
// 	// // I inizialize a slice using the path to view.tpml.html file
// 	// // plus the path to the base and navigation
// 	// files := []string{
// 	// 	"./ui/html/base.tmpl.html",
// 	// 	"./ui/html/partials/nav.tmpl.html",
// 	// 	"./ui/html/pages/view.tmpl.html",
// 	// }
// 	//
// 	// // I parse the files and check for errors
// 	// ts, err := template.ParseFiles(files...)
// 	// if err != nil {
// 	// 	app.serverError(w, err)
// 	// 	return
// 	// }
// 	//
// 	// // Create an instance of a templateData struct holding the snippet data
// 	// data := &templateData{Snippet: snippet}
// 	//
// 	// // In the end I execute the template
// 	// err = ts.ExecuteTemplate(w, "base", data)
// 	// if err != nil {
// 	// 	app.serverError(w, err)
// 	// }
// 	// // w.Write([]byte("Display the snippet"))
// 	// // We write the snippet as plain text to the http.ResponseWriter
// 	// fmt.Fprintf(w, "%+v", snippet)
// }

func (app *application) snippetView(w http.ResponseWriter, r *http.Request) {
	// We use the ParamsFromContext() method to get a slice of route parameters from the request context
	params := httprouter.ParamsFromContext(r.Context())

	// We extract the value of the id parameter from the slice, and try to convert it to an integer
	id, err := strconv.Atoi(params.ByName("id"))
	if err != nil || id < 1 {
		app.notFound(w)
		return
	}

	snippet, err := app.snippets.Get(id)
	if err != nil {
		if errors.Is(err, models.ErrNoRecord) {
			app.notFound(w)
		} else {
			app.serverError(w, err)
		}
		return
	}

	data := app.newTemplateData(r)
	data.Snippet = snippet

	app.render(w, http.StatusOK, "view.tmpl.html", data)
}

// func (app *application) snippetCreate(w http.ResponseWriter, r *http.Request) {
// 	// r.Method is an HTTP method, if it's not POST then return a 405 method not allowed response
// 	// if r.Method != "POST" {
// 	if r.Method != http.MethodPost {
// 		w.Header().Set("Allow", http.MethodPost)
// 		// w.WriteHeader(405)
// 		// w.Write([]byte("Method not allowed"))
// 		// Same as above (http.StatusMethodNotAllowed = 405)
// 		app.clientError(w, http.StatusMethodNotAllowed)
// 		return
// 	}
//
// 	title := "O snail"
// 	content := "O snail\nClimb Mount Fuji,\nBut slowly, slowly!\n\n- Kobayashi Issa"
// 	expires := 7
//
// 	// We pass the data to the SnippetModel.Insert() method, which returns the ID of the new record
// 	id, err := app.snippets.Insert(title, content, expires)
// 	if err != nil {
// 		app.serverError(w, err)
// 		return
// 	}
//
// 	// Redirect the user to the relevant page for the snippet
// 	http.Redirect(w, r, fmt.Sprintf("/snippet/view?id=%d", id), http.StatusSeeOther)
// }

func (app *application) snippetCreate(w http.ResponseWriter, r *http.Request) {
	data := app.newTemplateData(r)

	// We inizialize the form so that it's not uninitialized when the template
	// is first called
	data.Form = snippetCreateForm{Expires: 365}
	app.render(w, http.StatusOK, "create.tmpl.html", data)
}

func (app *application) snippetCreatePost(w http.ResponseWriter, r *http.Request) {
	// // we call the r.ParseForm() which adds any data in POST request bodies
	// // to the r.PostForm map. If there is an error we will call app.ClientError()
	// err := r.ParseForm()
	// if err != nil {
	// 	app.clientError(w, http.StatusBadRequest)
	// 	return
	// }

	// // We use the r.PostForm.Get() method to retrieve the value of the title and content fields
	// // from the form. We also get the expires, and we want the expires field to be an int
	// // title := r.PostForm.Get("title")
	// // content := r.PostForm.Get("content")
	// expires, err := strconv.Atoi(r.PostForm.Get("expires"))
	// if err != nil {
	// 	app.clientError(w, http.StatusBadRequest)
	// 	return
	// }

	// // Create an instance of the snippetCreateForm struct containing the form data
	// form := snippetCreateForm{
	// 	Title:   r.PostForm.Get("title"),
	// 	Content: r.PostForm.Get("content"),
	// 	Expires: expires,
	// 	// FieldErrors: map[string]string{},
	// }

	// I declare a new instance of snippetCreateForm struct
	var form snippetCreateForm

	err := app.decodePostForm(r, &form)
	if err != nil {
		app.clientError(w, http.StatusBadRequest)
		return
	}

	// I check for any validation error
	// fieldErrors := make(map[string]string)

	// // Title should not be blank and should be less than 100 characters
	// if strings.TrimSpace(form.Title) == "" {
	// 	form.FieldErrors["title"] = "Title cannot be blank"
	// } else if utf8.RuneCountInString(form.Title) > 100 {
	// 	form.FieldErrors["title"] = "Title cannot be longer than 100 characters"
	// }
	//
	// // content should not be blank
	// if strings.TrimSpace(form.Content) == "" {
	// 	form.FieldErrors["content"] = "Content cannot be blank"
	// }
	//
	// // expires should match one of our patterns (1, 7 or 365 days)
	// if expires != 1 && expires != 7 && expires != 365 {
	// 	form.FieldErrors["expires"] = "Expiry must be 1, 7 or 365 days"
	// }

	// We can call the method CheckField of the embedded Validator type directly on the form
	// this automatically fills the map that is part of the Validator struct and
	// therefore is also into the snippetCreateForm struct
	form.CheckField(validator.NotBlank(form.Title), "title", "Title cannot be blank")
	form.CheckField(validator.MaxChars(form.Title, 100), "title", "Title cannot be longer than 100 characters")
	form.CheckField(validator.NotBlank(form.Content), "content", "Content cannot be blank")
	form.CheckField(validator.PermittedInt(form.Expires, 1, 7, 365), "expires", "Invalid expiry value")

	// // If there is any error, return it in a HTTP reponse
	// if len(form.FieldErrors) > 0 {
	// 	// fmt.Fprintf(w, "%v", fieldErrors)
	// 	data := app.newTemplateData(r)
	// 	data.Form = form
	// 	app.render(w, http.StatusUnprocessableEntity, "create.tmpl.html", data)
	// 	return
	// }

	if !form.Valid() {
		data := app.newTemplateData(r)
		data.Form = form
		app.render(w, http.StatusUnprocessableEntity, "create.tmpl.html", data)
		return
	}

	// We pass the data to the SnippetModel.Insert() method, which returns the ID of the new record
	id, err := app.snippets.Insert(form.Title, form.Content, form.Expires)
	if err != nil {
		app.serverError(w, err)
		return
	}

	// Use put to add a string and corresponding key
	app.sessionManager.Put(r.Context(), "flash", "Snippet successfully created!")

	// Redirect the user to the relevant page for the snippet
	http.Redirect(w, r, fmt.Sprintf("/snippet/view/%d", id), http.StatusSeeOther)
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

// Helper method, the second parameter is the target destination that we want to decode data into
func (app *application) decodePostForm(r *http.Request, dst any) error {
	err := r.ParseForm()
	if err != nil {
		return err
	}

	// I call the Decode() method on the formDecoder passing a pointer to the form struct
	// this will populate the struct fields with the form data (check documentation of the library)

	err = app.formDecoder.Decode(dst, r.PostForm)
	if err != nil {
		// If we try to use an invalid target destination, the method will return
		// an error with the type *form.InvalidDecoderError. In that case we need
		// to return a panic
		var invalidDecoderError *form.InvalidDecoderError
		if errors.As(err, &invalidDecoderError) {
			panic(err)
		}

		// Otherwise I just return the error
		return err
	}

	return nil
}

type userSignupForm struct {
	Name                string `form:"name"`
	Email               string `form:"email"`
	Password            string `form:"password"`
	validator.Validator `form:"-"`
}

func (app *application) userSignup(w http.ResponseWriter, r *http.Request) {
	// fmt.Fprintln(w, "Display a HTML form for signing up a new user...")
	data := app.newTemplateData(r)
	data.Form = userSignupForm{}
	app.render(w, http.StatusOK, "signup.tmpl.html", data)
}

func (app *application) userSignupPost(w http.ResponseWriter, r *http.Request) {
	// Declare an zero-valued instance of our userSignupForm struct.
	var form userSignupForm
	// Parse the form data into the userSignupForm struct.
	err := app.decodePostForm(r, &form)
	if err != nil {
		app.clientError(w, http.StatusBadRequest)
		return
	}
	// Validate the form contents using our helper functions.
	form.CheckField(validator.NotBlank(form.Name), "name", "This field cannot be blank")
	form.CheckField(validator.NotBlank(form.Email), "email", "This field cannot be blank")
	form.CheckField(validator.Matches(form.Email, validator.EmailRX), "email", "This field must be a valid email address")
	form.CheckField(validator.NotBlank(form.Password), "password", "This field cannot be blank")
	form.CheckField(validator.MinChars(form.Password, 8), "password", "This field must be at least 8 characters long")

	// If there are any errors, redisplay the signup form along with a 422
	// status code.
	if !form.Valid() {
		data := app.newTemplateData(r)
		data.Form = form
		app.render(w, http.StatusUnprocessableEntity, "signup.tmpl.html", data)
		return
	}

	// Try to create a new user record in the database. If the email already
	// exists then add an error message to the form and re-display it.
	err = app.users.Insert(form.Name, form.Email, form.Password)
	if err != nil {
		if errors.Is(err, models.ErrDuplicateEmail) {
			form.AddFieldError("email", "Email address is already in use")
			data := app.newTemplateData(r)
			data.Form = form
			app.render(w, http.StatusUnprocessableEntity, "signup.tmpl.html", data)
		} else {
			app.serverError(w, err)
		}
		return
	}

	// Otherwise add a confirmation flash message to the session confirming that
	// their signup worked.
	app.sessionManager.Put(r.Context(), "flash", "Your signup was successful. Please log in.")
	// And redirect the user to the login page.
	http.Redirect(w, r, "/user/login", http.StatusSeeOther)
}

type userLoginForm struct {
	Email               string `form:"email"`
	Password            string `form:"password"`
	validator.Validator `form:"-"`
}

func (app *application) userLogin(w http.ResponseWriter, r *http.Request) {
	data := app.newTemplateData(r)
	data.Form = userLoginForm{}
	app.render(w, http.StatusOK, "login.tmpl.html", data)
}

func (app *application) userLoginPost(w http.ResponseWriter, r *http.Request) {
	// Decode the form data into userLoginForm struct
	var form userLoginForm

	err := app.decodePostForm(r, &form)
	if err != nil {
		app.clientError(w, http.StatusBadRequest)
		return
	}

	// Check that email and password are provided. We also check the email format just
	// for a UX-nicety
	form.CheckField(validator.NotBlank(form.Email), "email", "This field cannot be blank")
	form.CheckField(validator.Matches(form.Email, validator.EmailRX), "email", "This field must be a valid email address")
	form.CheckField(validator.NotBlank(form.Password), "password", "This field cannot be blank")

	if !form.Valid() {
		data := app.newTemplateData(r)
		data.Form = form
		app.render(w, http.StatusUnprocessableEntity, "login.tmpl.html", data)
		return
	}

	// Check if the credentials are valid. If they're not add a generic non-field error message
	// and redisplay the login page
	id, err := app.users.Authenticate(form.Email, form.Password)
	if err != nil {
		if errors.Is(err, models.ErrInvalidCredentials) {
			form.AddNonFieldError("Invalid email or password")
			data := app.newTemplateData(r)
			data.Form = form
			app.render(w, http.StatusUnprocessableEntity, "login.tmpl.html", data)
		} else {
			app.serverError(w, err)
		}
	}
	// Use the RenewToken() method on the current session to change the session
	// ID. It's good practice to do this when the privileges change
	err = app.sessionManager.RenewToken(r.Context())
	if err != nil {
		app.serverError(w, err)
		return
	}
	// Add the ID of the current user to the session, so that they are now
	// 'logged in'.
	app.sessionManager.Put(r.Context(), "authenticatedUserID", id)
	// Redirect the user to the create snippet page.
	http.Redirect(w, r, "/snippet/create", http.StatusSeeOther)
}

func (app *application) userLogoutPost(w http.ResponseWriter, r *http.Request) {
	// I use RenewToken() method on the current session to change the session ID again
	err := app.sessionManager.RenewToken(r.Context())
	if err != nil {
		app.serverError(w, err)
		return
	}

	// I remove the authenticatedUserID from the session
	app.sessionManager.Remove(r.Context(), "authenticatedUserID")

	// Add a flash message to the session to confirm to the user that they've been logged out
	app.sessionManager.Put(r.Context(), "flash", "You've been logged out successfully!")

	// I redirect the user to the home page
	http.Redirect(w, r, "/", http.StatusSeeOther)
}

// Function that returns true if the user is autenticated
func (app *application) isAuthenticated(r *http.Request) bool {
	return app.sessionManager.Exists(r.Context(), "authenticatedUserID")
}
