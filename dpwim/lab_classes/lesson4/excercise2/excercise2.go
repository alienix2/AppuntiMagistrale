package main

import (
	"fmt"
)

func super_digit(n int) int {
	if n < 10 {
		return n
	}
	return super_digit(n/10 + n%10)
}

func main() {
	fmt.Println(super_digit(148148148))
}
