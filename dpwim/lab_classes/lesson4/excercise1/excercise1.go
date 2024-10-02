package main

import (
	"fmt"
	"math"
)

func factorial(n int) (result float64) {
	if n > 0 {
		result = float64(n) * factorial(n-1)
		return result
	}
	return 1
}

func exp(x int) float64 {
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

func main() {
	fmt.Println("e^x = ", e_x(100))
	fmt.Println("e^x = ", exp(100))
}
