package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

// ToDo redo this with go structure
func TestIsFunction(t *testing.T) {
	r1 := []Pair[int64, int64]{{1, 1}, {2, 2}, {3, 3}}
	assert.True(t, isFunction(r1), "The relation r1 is a function")

	r2 := []Pair[int64, int64]{{1, 2}, {2, 4}, {3, 6}, {4, 8}, {1, 0}}
	assert.False(t, isFunction(r2), "The relation r2 is not a function")
}
