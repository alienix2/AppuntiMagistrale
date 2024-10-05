package main

import (
	"math"
)

func factorial(n int) (result float64) {
	if n > 0 {
		result = float64(n) * factorial(n-1)
		return result
	}
	return 1
}

func exp(x int) float64 { //Professor's solution
	sum := 1.0
	fact := 1
	pow := 1

	for i := 1; i < 10; i++ {
		pow *= x
		fact *= i
		sum += float64(pow) / float64(fact)
	}
	return sum
}

func e_x(x float64) (expansion float64) {
	expansion = 1.0
	for i := 1; i < 10; i++ {
		var factorial = factorial(i)
		expansion += (math.Pow(float64(x), float64(i))) / factorial
	}
	return expansion
}

func super_digit(n int) int {
	if n < 10 {
		return n
	}
	return super_digit(n/10 + n%10)
}

func array_replication(arr []int, k int) []int {
	var result []int
	for i := 0; i < len(arr); i++ {
		for j := 0; j < k; j++ {
			result = append(result, arr[i])
		}
	}
	return result
}

func array_replication1(arr []int, k int) []int {
	var result []int //This is a slice cause it has no fixed size
	for i := 0; i < k; i++ {
		result = append(result, arr...)
	}
	return result
}

func swap_adjacent(s string) string {
	var result = []rune(s)
	for i := 0; i < len(s)-1; i += 2 {
		result[i], result[i+1] = result[i+1], result[i]
	}
	return string(result)
}

func mingle_strings(s1, s2 string) string {
	var result string
	for i := 0; i < len(s1); i++ {
		result += string(s1[i]) + string(s2[i])
	}
	return result
}
