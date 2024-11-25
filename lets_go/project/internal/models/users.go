package models

import (
	"database/sql"
	"errors"
	"strings"
	"time"

	"github.com/go-sql-driver/mysql"
	"golang.org/x/crypto/bcrypt"
)

// Define a User type. The field names and type align with the columns in the database
type User struct {
	Created        time.Time
	Name           string
	Email          string
	HashedPassword []byte
	ID             int
}

// Define a UserModel type which wraps a sql.DB connection pool
type UserModel struct {
	DB *sql.DB
}

// We define an Insert method to add a new record to the users table
func (m *UserModel) Insert(name, email, password string) error {
	// Create a bcrypt hash of the plain-text password.
	hashedPassword, err := bcrypt.GenerateFromPassword([]byte(password), 12)
	if err != nil {
		return err
	}

	stmt := `INSERT INTO users (name, email, hashed_password, created) VALUES(?, ?, ?, UTC_TIMESTAMP())`

	// Use the Exec() method to insert the user details and hashed password
	// into the users table.
	_, err = m.DB.Exec(stmt, name, email, string(hashedPassword))
	if err != nil {

		// If we get an error we check if the error is related to the email being already in use
		// and therefore present in the database (this is because we have a unique constraint on the email column)
		var mySQLError *mysql.MySQLError
		if errors.As(err, &mySQLError) {
			if mySQLError.Number == 1062 && strings.Contains(mySQLError.Message, "users_uc_email") {
				return ErrDuplicateEmail
			}
		}
		return err
	}
	return nil
}

// We define an authenticate method to verify whether a user exists with the provided email and password
func (m *UserModel) Authenticate(email, password string) (int, error) {
	return 0, nil
}

// We define a method to check if a user already exists with a specific ID
func (m *UserModel) Get(id int) (*User, error) {
	return nil, nil
}
