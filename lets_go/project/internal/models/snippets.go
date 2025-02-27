package models

import (
	"database/sql"
	"errors"
	"time"
)

type SnippetModelInterface interface {
	Insert(title string, content string, expires int) (int, error)
	Get(id int) (*Snippet, error)
	Latest() ([]*Snippet, error)
}

// Define a Snippet struct type
// Note: the fields are ordered so that they occupy the smallest possible memory footprint
type Snippet struct {
	Expires time.Time
	Created time.Time
	Content string
	Title   string
	ID      int
}

// Define a SnippetModel type which wraps a sql.DB connection pool
type SnippetModel struct {
	DB *sql.DB
}

// Insert a new snippet into the database and return its id
func (m *SnippetModel) Insert(title string, content string, expires int) (int, error) {
	// SQL statement, split into two lines (ence the back-ticks)
	stmt := `INSERT INTO snippets (title, content, created, expires) 
  VALUES(?, ?, UTC_TIMESTAMP(), DATE_ADD(UTC_TIMESTAMP(), INTERVAL ? DAY))`

	// Use the Exec() method on the embedded connection pool to execute the statement
	// The return value from Exec() is a Result object which contains the ID of the newly inserted record
	result, err := m.DB.Exec(stmt, title, content, expires)
	if err != nil {
		return 0, err
	}

	// If result is not needed, use the _ blank identifier to discard it, but in this case:
	// Use the LastInsertId() method on the result object to get the ID of our newly inserted record in the snippets table
	id, err := result.LastInsertId()
	if err != nil {
		return 0, err
	}

	// The ID returned is an int64, so we convert it to an int type before returning
	return int(id), nil
}

// return a snippet based on its id
func (m *SnippetModel) Get(id int) (*Snippet, error) {
	// Write the SQL statement we want to execute
	stmt := `SELECT id, title, content, created, expires FROM snippets WHERE expires > UTC_TIMESTAMP() AND id = ?`

	// We use the QueryRow() method on the connection pool
	// This method only returns a single row. id is passed to take place of ?
	row := m.DB.QueryRow(stmt, id)

	// Initialize a pointer to a new zeroed Snippet struct
	s := &Snippet{}

	// Alternative way to do the queryRow and scan in one line
	// err := m.DB.QueryRow("SELECT ...", id).Scan(&s.ID, &s.Title, &s.Content, &s.Created, &s.Expires)

	// Use row.Scan() to copy values of every field in the sql.Row
	// the arguments to row.Scan() are pointers to the place we want to copy the data into
	// the number of arguments must be the same as the number of columns returned by the statement
	err := row.Scan(&s.ID, &s.Title, &s.Content, &s.Created, &s.Expires)
	if err != nil {
		// If the query returns no rows, row.Scan() will return a sql.ErrNoRows error
		// We use this to check for the error and return a specific error message
		if errors.Is(err, sql.ErrNoRows) {
			return nil, ErrNoRecord
		} else {
			return nil, err
		}
	}

	// If everything is fine, return the Snippet object
	return s, nil
}

// return the 10 most recently created snippets
func (m *SnippetModel) Latest() ([]*Snippet, error) {
	stmt := `SELECT id, title, content, created, expires FROM snippets 
  WHERE expires > UTC_TIMESTAMP() ORDER BY created DESC LIMIT 10`

	// Use the Query() method on the connection pool
	// This method returns more than a single row
	rows, err := m.DB.Query(stmt)
	if err != nil {
		return nil, err
	}

	// We defer rows.Close() to ensure the sql.Rows result set is always properly closed before Latest() returns
	// The defer must be before the check otherwise if there's an error you'll get a panic
	defer rows.Close()

	snippets := []*Snippet{}

	// I iterate over the rows in the resultSet.
	// This prepares the rows to be acted on by rows.Scan(). If the iteration completes the resultset
	// is closed automatically
	for rows.Next() {
		// Initialize a pointer to a new zeroed Snippet struct
		s := &Snippet{}

		// Use rows.Scan() to copy the values from each field in the row to the new Snippet object
		err = rows.Scan(&s.ID, &s.Title, &s.Content, &s.Created, &s.Expires)
		if err != nil {
			return nil, err
		}

		// Append the Snippet object to the slice
		snippets = append(snippets, s)
	}

	// when the rows.Next() has finished, we check for any errors that may have occurred
	// during the iteration. We can't assume that no error occured.
	if err = rows.Err(); err != nil {
		return nil, err
	}

	// If everything is fine, return the Snippet object
	return snippets, nil
}

// Note: we are using Query, QueryRow and Exec methods instead of preparing statements ourselves
// This has pros and cons, see page 125-126 of book otherwise
