# Go basics

Go to go site for initial info: https://go.dev/
**Editor:** Prof. will use VSCode but others work well (let's see if I can use Vim)
**For the next time:** Chose the editor that we want to use and install go

**Introduction:**
developed by google, at first it was not public then it was published to world. The main goal was to develop the app Scalable at first.  
Go is similar to c for certain aspect, is fast to compile and is really fast in code execution also.
*Example:* Hello world in go:
```go
package main

import "fmt"

func main() {
	fmt.Println("Hello, 世界")
}
```
Go is a compiled language.
Go statements are usually separated by semicolon ";". The compiler is able to run code without semicolon by inserting the semicolon where they should go.

To compile and run a file we can use: ```go run file.go```  
To just compile we can use: ```go build file.go```  
*Note:* you can use specific flags to specific some options, for instance -o to choose a name for the output file

*Other example of code:*
```go
package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("Welcome to the playground!")
	fmt.Println("The time is", time.Now())
}
```
*thing to know about go:* 
- we can see the correct syntax to do multiple imports in go.
- we can import single functions inside a package using a slash (*I.e:* ```math/rand```). Then we can refer to the function using package.function()
- we can have variable exported to other packages, in which case they have a capital letter
- function's type declaration is at the end of the function ```func add(x int, y int) int``` (*Note:* something similar applies to the variables in the function as we can see). Something like this is also accepted ```func add(x, y int)```
- functions in go can return more than one value
- we choose the variables we want to return in the function so that they are automatically returned at return time:
```go
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}
```

