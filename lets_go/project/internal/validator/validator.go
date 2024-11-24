package validator

import (
	"strings"
	"unicode/utf8"
)

// Define a new type named Validator which contains a map of errors
type Validator struct {
	FieldErrors map[string]string
}

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

// PermittedInt if a value is in a list of permitted integers
func PermittedInt(value int, permittedValues ...int) bool {
	for i := range permittedValues {
		if value == permittedValues[i] {
			return true
		}
	}
	return false
}
