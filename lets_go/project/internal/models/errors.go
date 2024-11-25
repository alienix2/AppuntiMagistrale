package models

import (
	"errors"
)

// We define this custom error so that our app isn't tied to the underlying database
var (
	// Error for when a record is not found
	ErrNoRecord = errors.New("models: no matching record found")

	// Error for when a user tries to login with wrong credentials
	ErrInvalidCredentials = errors.New("models: invalid credentials")

	// Error for when a user tries to signup with an email that is already in use
	ErrDuplicateEmail = errors.New("models: duplicate email")
)
