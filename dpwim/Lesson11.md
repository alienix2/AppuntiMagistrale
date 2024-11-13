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
