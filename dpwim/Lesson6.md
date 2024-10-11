# Function values in go

In go functions are considered **values**. Function can therefore be used both as a function argument and as return values.
*I.e:* 
```go
func compute(fn func(float64, float64) float64) float64 {
	return fn(3, 4)
}

func test2(a,b float64) float64{
	return a/b
}

func main() {
	compute(test2)
}
```
Functions can also be assigned to a value:
*I.e:*
```go
hypot := func(x, y float64) float64 {
		return math.Sqrt(x*x + y*y)
}
```
If a function returns another function, the function which is in the inside can use the name of the variables that are defined from his parent class **BUT** they create some kind of closure with that specific instance of the function. (Something like what happens with objects)  
*I.e:*
```go
func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

func main() {
	pos, neg := adder(), adder()
	for i := 0; i < 10; i++ {
		fmt.Println(
			pos(i),
			neg(-2*i),
		)
	}
}
```
in this case the two variables pos and neg don't share the variable sum, this means that the two won't interfere with each-other. Also the reason why it works is that the nested functions uses the return operation.

# Methods

Once you create a type in go, you can assign methods to it. This is a lot like what happens in object oriented programming.  
Functions and methods can be distinguished by looking at the fact that methods must implement a special **receiver** argument.
*I.e:*
```go
func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
```
this is a method for the Vertex struct and it takes no arguments.  
Methods for a type can be defined in another files in relation to the struct, but the files must share the same package (folder).  
The type of the receiver can also be a pointer, what's the difference? Passing something normally means passing a value whereas passing it as a pointer mean passing the actual pointer to where the data is (this is like in C).  
*Note:* there is no rule of thumb to decide if it's better to use a pointer or a value in a specific case. One of the most important things to consider is that usually passing a pointer is usually less cost in terms of resources.

## Embedding

In go we have no class. We have methods that can be applied to struct but we have no such thing as inheritance.  
In go there is **composition** which means that a class can be composed from other classes. 
*I.e:*
```go
type MyStruct1 struct{
  a int
}

func (s MyStruct1) incr(x int) int{
  return s.a + x
}

```
What can I do to implement more functionalities?
```go
type MyStruct1 struct{
  a int
}

func (s MyStruct1) incr(x int) int{
  return s.a + x
}

type MyStruct2 struct {
  MyStruct1 //fields of MyStruct1 imported
  b int
}
```
How can I use the code above?
```go
func main() {
  s1 := MyStruct1{10}
  s2 := MyStruct2{
    MyStruct1{2}, 3,
  }
  fmt.println(s1.incr(2)) //12 will be printed
  fmt.println(s2.incr(1)) //3 will be printed
}
```
In this case there is no substitution principle cause there is no proper inheritance.

## Interfaces

These are something that allows to have some kind of substitution principle. Interfaces are simply defined as a set of methods that a type must implement.
*I.e:*
```go
type Abser interface {
  Abs() float64
}
```
In go there is an implicit implementation of an interface that is done by all the classes that actually implement the methods of such interface.
*I.e:*
```go
func (v Vertex) Abs() float64 {
  return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
```
This automatically implements the Abser interface for the Vertex struct.
*Note:* in go there could be a nil receiver. This happens when you call a method on an interface that is not implemented. This doesn't necessarily cause an error in go. It still isn't the best to use interfaces like that, and in most cases this should be avoided.

An interface with no methods is called an **empty interface**. This is implemented by all types. This is used when you want to pass any type to a function.

**Type assertions** are used to check if a type implements an interface. The syntax usually used is: ```t, ok := i.(T)``` where t is the type that you want to check, i is the interface and T is the type that you want to check if it implements the interface. If the type implements the interface the ok variable will be true, otherwise it will be false.  
To check if a type implements an interface you can also use a switch statement.
*I.e:*
```go
switch v := i.(type) {
  case T:
    //here v has type T
  case S:
    //here v has type S
  default:
    //here v has the same type as i
}
```
## Stringer interface
The stringer interface is a special interface that is used to implement the ```String()``` method. This is used to print the value of a type in a specific way. This is an interface of the "fmt" package.
*I.e:*
```go
import "fmt"

type Person struct {
	Name string
	Age  int
}

func (p Person) String() string {
	return fmt.Sprintf("%v (%v years)", p.Name, p.Age)
}

func main() {
	a := Person{"Arthur Dent", 42}
	z := Person{"Zaphod Beeblebrox", 9001}
	fmt.Println(a, z)
}
```
## Errors
Errors in go are handled with the ```error``` interface. This is a simple interface that has only one method: ```Error() string```. This is used to return the error message. The way that is usually used to handle errors in go is to write the function so that it returns two values, and the second is usually the message of the error that will be initialized if an error really happens and will otherwise be nil.
*I.e:*
```go
func Sqrt(x float64) (float64, error) {
  if x < 0 {
    return 0, &MyError{"cannot do the Sqrt of a negative number"}
  }
  return math.Sqrt(x), nil
}
```
