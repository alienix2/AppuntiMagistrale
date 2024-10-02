# Go programming language

## Variable declaration
Declaring a variable: `var varName typeName`  
*Example of a variable declaration:*
```go
package main
import "fmt"

var c, python, java bool

func main() {
	var i int
	fmt.Println(i, c, python, java)
}
```
*Note:* variables are automatically initialized to their zero value.

Initialize multiple variables at once: `var varName1, varName2 = value1, value2`  

There is another way to initialize a value: `:=`  
*Note:* this operator can only be used to assign a value to a variable that has not been declared yet. This is **NOT** an alternative to an assignment operator. **Important:** This operator can only be used in the body of a function.

A variable can declared with a direct assignment as seen above, but there are specific rule about the type that is being inferred from the value used in the assignment.

## Basic types

**Variables:**  
The basic types for **variables** in Go are:
- bool
- string
- int  int8  int16  int32  int64
- uint uint8 uint16 uint32 uint64 uintptr
- byte (alias for uint8)
- rune (alias for int32 represents a Unicode code point)
- float32 float64
- complex64 complex128

**Constants:**  
the declaration of constants is done with the `const` keyword. The type is inferred from the value assigned to the constant. *I.e:* `const int = 60` will be an integer.

## Type conversions
In Go there is no implicit type conversion. You always have to convert the type explicitly.
The syntax for conversion is: `T(v)` where `T` is the type and `v` is the value to convert.

## Control structure

**For loop:**  
In Go for loop is the only kind of loop actually present.  
*Example of a for loop:*
```go
package main
import "fmt"

func main() {
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)
}
```
*Note:* you **must** always use `{}` for the body of the loop.

The init and post statements are optional.
*Example of a for loop without init and post statements:*
```go
	for ; sum < 1000; {
		sum += sum
	}
```
A loop without condition will loop forever.
*Example of a loop without condition:*
```go
  for {
    //do something
  }
```
**if statement:**  
if statements follow a similar syntax to the for loop. You must always use the `{}` for the body of the if statement.
*Example of an if statement:*
```go
  if x < 0 {
    return -x
  }
  return x
```
In Go you can have an `if` statement with a short statement before the condition. This statement is executed before the condition and its scope is limited to the if statement.
*Example of an if statement with a short statement:*
```go
  if v := math.Pow(x, n); v < lim {
    return v
  }
```
There is also the `else` statement that can be used in conjunction with the `if` statement.
*Example of an if statement with an else statement:*
```go
  if v := math.Pow(x, n); v < lim {
    return v
  } else {
    fmt.Printf("%g >= %g\n", v, lim)
  }
```
*Note:* the v variable in this case is also available in the else block.

**Exercise loops and functions:** (calculate the square root of a number using the Newton's method)
```go
package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	z := x
	var z_old float64
	i := 1
	
	for ; math.Abs(z - z_old) > 1e-8; i++{
		z_old = z
		z -= (z * z -x) / (2 * z)
		fmt.Printf("%d - %f\n", i, z)
	}
	
	return z
}

func main() {
	fmt.Println(Sqrt(2))
	fmt.Println(math.Sqrt(2))
}
```

**Switch statement:**  
The switch statement is similar to the one in C, or Java. The main difference is that you don't need to add a `break` statement at the end of each case. The switch statement will automatically break at the end of each case.  
A different from C is that the case can be an expression. The cases are evaluated from top to bottom and the first one that is true is executed.
In go there is also the default case that is executed if no other case is true.
*Example of a switch statement:*
```go
func main() {
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon.")
	default:
		fmt.Println("Good evening.")
	}
}
```
**Defer:**  
Defer is used to ensure that a function call is performed later in a program's execution. You use defer to make it so the action described is executed before the function returns.
*Example of defer:*
```go
func main() {
	defer fmt.Println("world")

	fmt.Println("hello")
}
```
*Note:* the deferred function's arguments are evaluated when the defer statement is evaluated, not when the function is executed. In example if I use defer inside a loop all the actions will be executed after the function returns still.

## Other topics

**Pointers:**  
pointers work a lot like C, the main difference is that you don't have pointer arithmetic. This is done mainly to prevent certain kind of errors which are really common when programming in C.

**Structs:**  
a struct is a collection of fields. A struct in Go is very similar to a struct in C.
*Example of a struct:*
```go
type Vertex struct {
  X int
  Y int
}
```
You can access the fields of a struct using the `.` operator.`

**Struct literals:**  
You can list just a subset of fields by using the `Name:` syntax. The order of the fields doesn't matter.  
*Example of a struct literal:*
```go
var (
	v1 = Vertex{1, 2}  // has type Vertex
	v2 = Vertex{X: 1}  // Y:0 is implicit
	v3 = Vertex{}      // X:0 and Y:0
	p  = &Vertex{1, 2} // has type *Vertex
)
```
**Arrays:**  
 The type `[n]T` is an array of n values of type `T`.  
*Example of an array:*
```go
var a [2]string
a[0] = "Hello"
a[1] = "World"
fmt.Println(a[0], a[1])
```
*Note:* Arrays have a fixed size. The size is part of the type of the array. This means that arrays cannot be resized.

**Slices:**  
A slice is a dynamically-sized, flexible view into the elements of an array.  
The type `[]T` is a slice with elements of type `T`.  
*Example of a slice:*
```go
primes := [6]int{2, 3, 5, 7, 11, 13}
var s []int = primes[1:4]
fmt.Println(s)
```
*Note:* in the slice the first index is included and the last one is excluded.  
Slices are like references to arrays. A slice does not store any data, it just describes a section of an underlying array. This means that modifying a slice will cause the modification to be present also in the original array (and all the other slices derived from that array)  
Slices have defaults. The default is 0 for the low bound and the length of the array for the high bound.
Slices have length and capacity. The length is the number of elements in the slice and the capacity is the number of elements in the underlying array starting from the first element of the slice.  
Length and capacity can be accessed with the use of the methods `len(s)` and `cap(s)`.  
A slice can be created with the `make` function. The syntax is `make([]T, len, cap)`. The capacity is optional and if not specified it will be equal to the length.
Elements can be appended to a slice using the `append` function. The syntax is `append(s []T, x ...T) []T`. The `...` operator is used to append multiple elements at once.

**Range:**  
The `range` keyword is used to iterate over a slice or a map.
*Example of a range:*
```go
for i, v := range pow {
	fmt.Printf("2**%d = %d\n", i, v)
}
```
**Maps:**  
A map is a collection of key-value pairs. Maps are unordered.
Map literals are like struct literals, but the keys are required.
If I try to access a key that is not present in the map I will get the zero value of the type of the value. The problem with that is that I might not be able to understand if the value is present with the zero or is not present at all. To solve this problem we can use the syntax `elem, ok = m[key]` and check the value contained in the `ok` variable.

**Go modules:**
In go a module can be seen as something similar to a library. In order to use go modules we must use the go utility. With go modules we are able to use a testing file. (Check the github repo for more insight about this)
In a go module `go get github.com/...` is used to download the module. The module is then imported in the code with the `import` statement.
