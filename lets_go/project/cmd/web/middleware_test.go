package main

import (
	"bytes"
	"io"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSecureHeaders(t *testing.T) {
	rr := httptest.NewRecorder()

	r, err := http.NewRequest(http.MethodGet, "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	next := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("OK"))
	})

	secureHeaders(next).ServeHTTP(rr, r)

	rs := rr.Result()

	expectedValues := "default-src 'self'; style-src 'self' fonts.googleapis.com; font-src fonts.gstatic.com"
	assert.Equal(t, expectedValues, rs.Header.Get("Content-Security-Policy"))

	expectedValues = "nosniff"
	assert.Equal(t, expectedValues, rs.Header.Get("X-Content-Type-Options"))

	expectedValues = "origin-when-cross-origin"
	assert.Equal(t, expectedValues, rs.Header.Get("Referrer-Policy"))

	expectedValues = "0"
	assert.Equal(t, expectedValues, rs.Header.Get("X-Xss-Protection"))

	expectedValues = "deny"
	assert.Equal(t, expectedValues, rs.Header.Get("X-Frame-Options"))

	assert.Equal(t, rs.StatusCode, http.StatusOK)

	defer rs.Body.Close()
	body, err := io.ReadAll(rs.Body)
	if err != nil {
		t.Fatal(err)
	}
	bytes.TrimSpace(body)

	assert.Equal(t, string(body), "OK")
}
