package main

import (
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestRot13Reader(t *testing.T) {
	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	r := rot13Reader{s}
	decoded := make([]byte, len("Lbh penpxrq gur pbqr!"))
	r.Read(decoded)

	assert.Equal(t, "You cracked the code!", string(decoded))
}

func TestCountChange(t *testing.T) {
	d := []int{1, 3, 5, 7}
	n := 8

	assert.Equal(t, 6, countChange(d, n), "Expected 6 ways to make change for 8 with coins [1, 3, 5, 7]")
}

func TestInsert(t *testing.T) {
	h := Empty()

	h = h.Insert(10)
	h = h.Insert(20)
	h = h.Insert(15)

	max, err := h.GetMax()
	assert.NoError(t, err, "Expected no error when getting max")
	assert.Equal(t, 20, max, "Expected max to be 20")
}

// Test merging two heaps
func TestMerge(t *testing.T) {
	h1 := Empty().Insert(10).Insert(30)
	h2 := Empty().Insert(20).Insert(40)

	merged := h1.Merge(h2)

	max, err := merged.GetMax()
	assert.NoError(t, err, "Expected no error when getting max after merge")
	assert.Equal(t, 40, max, "Expected max after merge to be 40")
}

// Test deleting the maximum value
func TestDeleteMax(t *testing.T) {
	h := Empty().Insert(10).Insert(30).Insert(20)

	h, err := h.DeleteMax()
	assert.NoError(t, err, "Expected no error when deleting max")

	max, err := h.GetMax()
	assert.NoError(t, err, "Expected no error when getting new max")
	assert.Equal(t, 20, max, "Expected new max to be 20 after deletion")
}

// Test empty heap operations
func TestEmptyHeapOperations(t *testing.T) {
	h := Empty()

	// Test GetMax
	max, err := h.GetMax()
	assert.Error(t, err, "Expected error when getting max from empty heap")
	assert.Equal(t, 0, max, "Expected max to be 0 for empty heap")

	// Test DeleteMax
	newHeap, err := h.DeleteMax()
	assert.Error(t, err, "Expected error when deleting max from empty heap")
	assert.Nil(t, newHeap, "Expected newHeap to be nil after deleting max from empty heap")
}

// Test singleton heap
func TestSingletonHeap(t *testing.T) {
	h := Singleton(42)

	max, err := h.GetMax()
	assert.NoError(t, err, "Expected no error when getting max from singleton heap")
	assert.Equal(t, 42, max, "Expected max to be 42 for singleton heap")

	h, err = h.DeleteMax()
	assert.NoError(t, err, "Expected no error when deleting max from singleton heap")

	max, err = h.GetMax()
	assert.Error(t, err, "Expected error when getting max from empty heap after deletion")
	assert.Equal(t, 0, max, "Expected max to be 0 after deleting max from singleton heap")
}

// Test rank of the heap
func TestRank(t *testing.T) {
	h := Empty().Insert(10).Insert(30).Insert(20)

	rank := h.GetRank()
	assert.Equal(t, 1, rank, "Expected rank to be 1 for the heap with 3 elements")

	h, _ = h.DeleteMax()
	rank = h.GetRank()
	assert.Equal(t, 0, rank, "Expected rank to be 0 after deleting max from the heap")
}
