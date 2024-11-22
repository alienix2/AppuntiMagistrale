# Communication

Two of the most popular communication mechanisms are:

- **Remote Procedure Call**
- **Message-Oriented Middleware**

## Middleware

First of all we need to define what's a **middleware**: in this case it's a software layer that sits between the application and the network. It's main purpose is hiding the way our distributed system works under the hood (heterogeneity etc.).

What we want to see is what we want to show our user about the system and how that's implemented behind.

The **services** that a middleware should provide are:

- **Interoperability**: the middleware should allow different systems to communicate with each other.
- **Communication**: the middleware should provide a way to communicate between different systems.
- **Security**: the middleware should provide a way to secure the communication between different systems.
- **Many more**

## Remote Procedure Call

In this case we will see a **direct coordination** which means that the components are:

- **referentially coupled:** the caller knows the callee
- **temporally coupled:** the caller waits for the callee to finish

The basic idea is that a program can call procedures on another machine.

To understand how this works we can think of a call of a procedure done on the same machine. The caller needs to send a request to the callee and wait for the response. In the meantime the caller suspends it's executions and doesn't continue until the response is received.

The main difference is that in this case we need to do our call on the net so we need to serialize the request and send it to the callee. The callee will then deserialize the request and execute the procedure. Since we want to give an interface to the caller, he doesn't have to know about this part, we should provide an interface that he can use easily.

*Note:* we still need to tell the caller that his call might fail because of the network, in this way he can understand specific kind of errors that cannot happen on local calls.

*Example in python:*

API on the client:

```python
class Client:
  def append(self, data, dbList):
    msglst = (APPEND, data, dbList)
    self.chan.sendTo(self.server, msglst)
    msgrcv = self.chan.recvFrom(self.server)
    return msgrcv[1]
```

What the client uses:

```python
dbHandle = client.append(newTable, dbHandle)
```

The serves has an interface that allows to communicate with the client API, **check the slides** for the code.

## Encoding

The client and server must agree on how basic/complex data values are represented. *I.e:* multi-dimensional arrays

### XML-RPC

An example of the above is the **XML-RPC** protocol:

```xml
<methodCall>
  <methodName>examples.getStateName</methodName>
  <params>
    <param>
      <value><i4>41</i4></value>
    </param>
  </params>
</methodCall>
```

#### Passing references/pointers

This is another challenge that should be addressed. The client and server have two different address spaces and this means that pointers and memory allocation are different.

##### Naive solution

The first solution consist in copying the entire data structure and sending it. This is not efficient. This might require to send a lot of useless data and also this could result in a big overhead in the unmarshalling phase. *Note:* this solution is still acceptable used in some cases

##### Global references

Another solution is to use global references. This means that the server will keep a reference to the data structure and the client will send a reference to the server.

In this case we define two kind of objects **local** and **remote**, that are treated differently:

- **Local:** the objects are copied and transmitted entirely
- **Remote:** only the stub is copied and transmitted

*I.e:* this difference is very visible in Java, as remote objects should implement the `Remote` interface.

### How RPC is implemented in a language

There are two main ways to implement RPC in a language:

- As a **library/framework**
- **Included** in the language

#### Framework

In this case the programmers need to specify what is remotely exported by providing an interface of the service. The interface is written in ad hoc language, called **IDL** (Interface Definition Language), that can be compiled to generate the stubs for the client and the server.

**Pros:** programming language independence (*Note:* this is because we just need to adapt the framework to the different programming languages)
**Cons:** not fully transparent to the programmer (*Note:* this is because the programmer needs to generate the IDL and compile it, this can be automatized in many cases)

#### Programming language-based support

In this case the RPC is included in the language. The programmer just needs to specify that a function is remotely exported. This is done by using a specific keyword, like `remote` in Java.

**Pros:** fully transparent to the programmer
**Cons:** programming language dependence, so client and server must be written in the same language

### Asynchronous RPC

In this case the client doesn't wait for the server to finish the execution. The server sends an **ack** as soon as he receives the request and then starts processing the request while the client is also working on it's own.

This needs the use of **callbacks** that are functions that are called when a specific event happens. In this case a reference to a procedure of the client is sent to the server along with the request, in this way the server is able to make a procedure call once he's done processing the request and can send the answer.

### Multicast RPC

In this case the client sends the request to multiple servers and waits for the first answer. This is useful when we have multiple servers that can provide the same service and we want to use the fastest one. All the other answers are discarded.

### Binding a client to a server

In real application a preliminary step called **binding** is needed. This is the process of associating a client with a server. This is done by using a **directory service** (or a **registry**) that keeps track of the servers and their services. The server registers to the **registry** and then the client looks the server up in the registry by using it's **symbolic name**.
