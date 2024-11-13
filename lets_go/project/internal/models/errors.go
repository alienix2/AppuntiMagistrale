package models

import (
	"errors"
)

// We define this custom error so that our app isn't tied to the underlying database
var ErrNoRecord = errors.New("models: no matching record found")
