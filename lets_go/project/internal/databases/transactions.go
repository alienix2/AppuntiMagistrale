package main

import "database/sql"

type ExampleModel struct {
	DB *sql.DB
}

func (m *ExampleModel) ExampleTransaction() error {
	// Calling begin on the transaction method of the connection pool
	// This returns a transaction object
	tx, err := m.DB.Begin()
	if err != nil {
		return err
	}

	// Defer a call to the rollback method of the transaction object
	// This means that it will always be called but if the transaction
	// succeds it will be a no-op
	defer tx.Rollback()

	// I call tx.Exec() to execute the first SQL statement (I could use
	// any other SQL method like QueryRow or Query)

	_, err = tx.Exec("INSERT INTO example (name) VALUES ('Frodo Baggins')")
	if err != nil {
		return err
	}

	// If there is no error I call tx.commit() to commit the transaction
	// This will make the changes permanent in the database, if there is an error
	// in the commit method it will return an error
	// Commit or Rollback must be called to close the connection
	err = tx.Commit()
	return err
}
