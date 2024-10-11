package main

// 1. Write a function isFunction that takes a relation r on integers as input, i.e., a list of pair (x,y) of integers,
// and returns true if r represents a valid function. For example, isFunction r1 where r1 = [(1,1); (2,2); (3,3)]
// returns true because r1 represents the identity function on the set {1,2,3}. Instead, isFunction r2 with
// r2 = [(1,2); (2,4); (3,6); (4,8); (1,0)] returns false because r2 cannot be a function.
type Pair[T, Y any] struct {
	First  T
	Second Y
}

// ToDo redo this using a map
func isFunction(r []Pair[int64, int64]) bool {
	for i := 0; i < len(r); i++ {
		for j := i + 1; j < len(r); j++ {
			if r[i].First == r[j].First {
				if r[i].Second != r[j].Second {
					return false
				}
			}
		}
	}
	return true
}

// 2. Write a function count_change that given a list of coin denominations d and an amount of money n, returns in
// how many ways we can make the change. For example, given d = [1; 3; 5; 7] and n = 8 the result of count_change
// d n is 6. Given d = [1;2;3] and n = 4 the result of count_change d n is 4, because the possible changes are

func count_change(d []int64, n int64) int64 {
	current_n := n
	for i := 0; i < len(d); i++ {
		current_n = current_n - d[i]
		for j := 0; j < len(d); j++ {
		}
	}
	return 1 //ToDo
}
