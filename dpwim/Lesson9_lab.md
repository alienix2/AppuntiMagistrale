# Network programming in Go

## Net package

In go there is no explicit declaration of sockets in the standard library (unlike what happens in other programming languages)
The `net` package provided two very important functions: `Dial` and `Listen`.

## Sockets

Sockets can be seen as endpoints that can be used for a bidirectional communication. They are identified by an IP address and a port number. This means that each socket is bind to an IP and a port number

### TCP client

In order to open a TCP connection we must follow these points:

1. Open a connection using the `Dial` function
2. Wrap the `net.conn` object in a `bufio.Reader` and a `bufio.Writer` object if needed
3. Interact with the server using the standard read and write functions
4. Close the connection

#### Dial function

The `Dial` function is used to open a connection to a server. It takes two arguments: the protocol and the address of the server. The protocol is a string that can be either `tcp` or `udp`. The address is a string that contains the IP address and the port number of the server. You can choose the type of IPV that you want to use in a TCP connection. Instead of a port number you can use a string that represents the default port for widely used services (*I.e:* HTTP on port 80)

*Example of a TCP client:*

```go
// ...
c, err := net.Dial("tcp", connect)
if err != nil {
  fmt.Println(err)
  return
}
for {
  reader := bufio.NewReader(os.Stdin)
  fmt.Print(">> ")
  text, _ := reader.ReadString('\n')
  fmt.Fprintf(c, text+"\n")
  message, _ := bufio.NewReader(c).ReadString('\n')
  fmt.Print("->: " + message)
  if strings.TrimSpace(string(text)) == "STOP" {
    fmt.Println("TCP client exiting...")
    return
}
```

### TCP server

In order to create a TCP server we must follow these points:

1. Create a listener using the `Listen` function
2. Accept incoming connections using the `Accept` method of the listener object
3. Handle the connection using the `Conn` instance and interact with the client using writer and reader
4. Close the connection

#### Listen function

The listen function is used to create a listener object that will listen for incoming connections. It takes two arguments: the protocol and the address of the server. The protocol is a string that can be either `tcp` or `udp`. The address in this case is only represented by a port, and will listen on all the IPs by default.

*Example of a TCP server:*

```go
l, err := net.Listen("tcp", PORT)
if err != nil {
  fmt.Println(err)
  return
}
defer l.Close()
c, err := l.Accept()
if err != nil {
  fmt.Println(err)
  return
}
// Handling the connection
```

### UDP client

In UDP there is no concept of connection. The `Dial` function is used to create a connection to a server, but it doesn't actually create a connection. The `WriteToUDDP` function is used to send a message to a server, and the `ReadFromUDP` function is used to read a message from a server. There is no concept of a stream like in TCP.

#### Function DialUDP

`func DialUDP(network string, laddr, raddr *UDPAddr) (*UDPConn, error)`.
The parameter network defines the network protocol to be used: “udp”, “udp4” (IPv4-only), “udp6” (IPv6-only)
The parameters laddr and raddr represent the local and the remote UDP address, respectively:

- If laddr is nil, a local address is automatically chosen;
- If the IP field of raddr is nil or an unspecified IP address, the local system is assumed

### UDP server

In order to create a UDP server the syntax is almost the same as the TCP server, but the `Listen` function is used with the `udp` protocol. The `ReadFromUDP` function is used to read a message from a client, and the `WriteToUDP` function is used to send a message to a client.

## Dependency injection

This is a design pattern that allows to remove the hard-coded dependencies and make it possible to change them at runtime. This is a way to implement the Inversion of Control principle.

The basic idea is that "An object function that wants to use a given service should not have to know how to construct those services"

*Idea:*  
**Service X** requires **Service Y** to work, but **Service X** should not be responsible for creating **Service Y**, instead **Service Y** could be injected inside **Service X** using this patter.

## Property injection

This is a different version of dependency injection, where the dependencies are injected through another method instead of injecting at creation time.

## Advantages of dependency injection

- **Loose coupling:** The client code does not need to know the implementation details of the service.
- **Easy to test:** The dependencies can be mocked and injected in the test cases.
- **Easy to change:** if you want to add a new feature you just need to create a new implementation of an interface and inject that
- **Easy to reuse:** The same service can be injected in multiple classes.
- **Runtime configuration:** The dependencies can be changed at runtime. This means that in particular using property injection we can change the real implementation of the interface at runtime.

*Note:* for further information: <https://www.jetbrains.com/guide/go/tutorials/dependency_injection_part_one/>
