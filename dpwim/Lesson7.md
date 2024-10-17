# More on the GO language

## Readers

The `io.Reader` interface has a method `Read` that reads data into a byte slice. The `io.Reader` interface is implemented by many types in the standard library, including files, network connections, compressors, ciphers, and others.
*Read method:* `func (T) Read(b []byte) (n int, err error)`. This method returns an `io.EOF` error when the stream ends.  
*Example of exercise:*

```go
type MyReader struct{}

func (t MyReader) Read(b []byte) (nint, err error){
  for i := 0; i < len(b); i++ {
    b[i] = 'A'
  }
  return len(b), nil
}

func main() {
  reader.Validate(MyReader{})
}
```

## Image package

The image package is part of the standard library, in particular it provides the `image.Image` interface and the `color.Color` interface. The `color.Color` interface is implemented by many types in the standard library, including `color.RGBA` and `color.Gray`. The `image.Image` interface has the method `ColorModel` that returns the `color.Model` of the image, and the method `Bounds` that returns the domain of the image. The `image.Image` interface also has the method `At` that returns the color of a specific pixel.
*Simple example:*

```go
type Image interface {
    ColorModel() color.Model
    Bounds() Rectangle
    At(x, y int) color.Color
}
```

## Another type of polymorphism

In go we have the type parameters. In particular we can define a function that takes a type as a parameter. `func Index[T comparable](s []T, x T) int`. This is really close to what happens in Java.
*Example:*

```go
type List[T any] struct {
 next *List[T]
 val  T
}
```

*Note:* we can use comparable to use == and != operators on type values.

## Threads in GO

## Go routines

Go routines can be created using the syntax `go f(x, y, z)`. The evaluation of `f`, `x`, `y`, and `z` happens in the current go routine and the execution of `f` happens in the new go routine. Go routines are lightweight, so it's common to have thousands of go routines in a single program. *Note:* the language was actually created to work well with this kind of stuff.

### Channels

In the majority of the languages we have threads that have a shared state. In GO there is shared memory but it's not usually used. Instead, we have channels. Channels are a typed conduit through which you can send and receive values with the channel operator `<-`. The data flows in the direction of the arrow. *Example:*

```go
ch <- v    // Send v to channel ch.
v := <-ch  // Receive from ch, and assign value to v.
```

Channels must be created first using `ch := make(chan int)`. By default, sends and receives block until the other side is ready. This allows goroutines to synchronize without explicit locks or condition variables.

We can have more than one threads writing on a single channel. In this case, the channel will be blocked until the receiver is ready to read all the data.  
*Example:*

```go
func fibonacci(n int, c chan int) {
  x, y := 0, 1
  for i := 0; i < n; i++ {
    c <- x
    x, y = y, x+y
  }
  close(c)
}

func main() {
  c := make(chan int, 10)
  go fibonacci(cap(c), c)
  for i := range c {
    fmt.Println(i)
  }
}
```

Channels can be buffered. The length of the buffer can be defined as follows: `ch := make(chan int, 100)`. In this case, the channel can store up to 100 values. When the buffer is full, the sender will block until the receiver is ready to receive a value.  
The one who sends can tell the receiver that he doesn't want to receive anything more by closing the channel as follows: `close(c)`. The receiver can check if the channel is closed by using the following syntax: `v, ok := <-ch`. If the channel is closed and there are no more values to receive, `ok` will be false.

#### Select

The `select` statement lets a goroutine wait on multiple communication operations. A select blocks until one of its cases can run, then it executes that case. It chooses one at random if multiple are ready.  
*Example:*

```go
func fibonacci(c, quit chan int) {
  x, y := 0, 1
  for {
    select {
    case c <- x:
      x, y = y, x+y
    case <-quit:
      fmt.Println("quit")
      return
    }
  }
}

func main() {
  c := make(chan int)
  quit := make(chan int)
  go func() {
    for i := 0; i < 10; i++ {
      fmt.Println(<-c)
    }
    quit <- 0
  }()
  fibonacci(c, quit)
}
```

*Note:* a default case in a select is run if no other case is ready.
