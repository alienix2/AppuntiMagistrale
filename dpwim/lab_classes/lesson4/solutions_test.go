package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestFactorial(t *testing.T) {
	result := factorial(5)
	assert.Equal(t, 120.0, result, "The factorial of 5 should be 120")
	assert.Equal(t, 1.0, factorial(0), "The factorial of 0 should be 1")
}

func TestExp(t *testing.T) {
	result := e_x(10)
	correct := exp(10)
	assert.Equal(t, correct, result, "The exponential of 5 should be %f", correct)
}

func TestSuperDigit(t *testing.T) {
	result := super_digit(148148148)
	assert.Equal(t, 3, result, "The super digit of 148148148 should be 3")
}

func TestArray_replication(t *testing.T) {
	result := array_replication([]int{1, 2, 3, 4}, 3)
	assert.Equal(t, []int{1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4}, result, "The replication of the array should be [1;1;1;2;2;2;3;3;3;4;4;4]")
}

func TestArray_replication1(t *testing.T) {
	result := array_replication1([]int{1, 2, 3, 4}, 3)
	assert.Equal(t, []int{1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4}, result, "The replication of the array should be [1;2;3;4;1;2;3;4;1;2;3;4]")
}

func TestSwap_adjacent(t *testing.T) {
	result := swap_adjacent(string("abcdpqrs"))
	assert.Equal(t, string("badcqpsr"), result, "The swap of the array should be badcqpsr")
}

func TestMingle_strings(t *testing.T) {
	result := mingle_strings("abcde", "pqrst")
	assert.Equal(t, "apbqcrdset", result, "The mingled string should be apbqcrdset")
}
