package validator

import (
	"regexp"
	"strings"
	"unicode/utf8"
)

// Define a new type named Validator which contains a map of errors
type Validator struct {
	FieldErrors    map[string]string
	NonFieldErrors []string // I use this to store errors that are not related to a specific field
}

// I use this regular expression to check if the email is valid
// if it's not a panix is thrown
var EmailRX = regexp.MustCompile(`^(?i)[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$`)

// function returning true if the Validator is empty
func (v *Validator) Valid() bool {
	return len(v.FieldErrors) == 0
}

// function that adds an error message to the map of errors
func (v *Validator) AddFieldError(key, message string) {
	// I check if the map is nil, if so I initialize it
	if v.FieldErrors == nil {
		v.FieldErrors = make(map[string]string)
	}

	if _, ok := v.FieldErrors[key]; !ok {
		v.FieldErrors[key] = message
	}
}

func (v *Validator) AddNonFieldError(message string) {
	v.NonFieldErrors = append(v.NonFieldErrors, message)
}

// function that adds an error message to the map of errors
func (v *Validator) CheckField(ok bool, key, message string) {
	if !ok {
		v.AddFieldError(key, message)
	}
}

// NotBlank checks if a field is empty
func NotBlank(value string) bool {
	return strings.TrimSpace(value) != ""
}

// MaxChars returns true if the number of characters is less than or equal to the max
func MaxChars(value string, max int) bool {
	return utf8.RuneCountInString(value) <= max
}

// MinChars returns true if the number of characters is greater than or equal to the min
func MinChars(value string, min int) bool {
	return utf8.RuneCountInString(value) >= min
}

func Matches(value string, rx *regexp.Regexp) bool {
	return rx.MatchString(value)
}

// // PermittedInt if a value is in a list of permitted integers
// func PermittedInt(value int, permittedValues ...int) bool {
// 	for i := range permittedValues {
// 		if value == permittedValues[i] {
// 			return true
// 		}
// 	}
// 	return false
// }

// We use generics to check if the value of type T equals one of the variadic permitted values
func PermittedValue[T comparable](value T, permittedValues ...T) bool {
	for i := range permittedValues {
		if value == permittedValues[i] {
			return true
		}
	}
	return false
}
