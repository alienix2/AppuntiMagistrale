# Distributed systems organization

*Chapther 2 of the book*

The two main levels to view the organization of a distributed system are:

- **Software architecture:**
  - the components, how they are organized and how they interact
- **System architecture:**
  - identifies the devices in the system and how they are interconnected
  - defines how the software is deployed on the hardware

## Software vs System architecture

I have several data providers that provide different kind of data. The end user shouldn't care about how the data is sent, it should just see it in a way that he can understand.

### Identifying the different components and where they belong

*Example:*  
![software_physical_architecture](../Screenshots/software_system)
*Other example:*  
![software_physical_architecture](../Screenshots/software_system2)

## What we must think about

- What are the **components** of the system?
- What is the **communication paradigm** that is being used?
- What are the **roles** and **responsibilities** of each component?

There are specific architecture that allow to answer these questions is a structured way. The architecture that will be presented aren't mutually exclusive, some of them may be suitable to cooperate with each-other in very complex systems.

### Layered architecture

This is typical in communication (*I.e:* TCP/IP).

Each layer provides services to the upper layer (using some kind of interfaces) and each layer is able to provide these services by using services provided by layers below.

A component can make a **down call** or an **up call**:

- **Down call:** the component is calling a service provided by a lower layer. *I.e:* a system calls to open a file
- **Up call:** this is necessary when the lower layer needs to notify the upper layer of something. *I.e:* a new packets arrives, the lower layer must communicate the upper layers that it should be handled.

*Note:* this paradigm is widely used also in non-distributed applications like when you use system calls in an operating system.

*Example:* TCP/IP stack:

- **Application layer:** provides services to the user
- **Transport layer:** provides services to the application layer
- **Network layer:** provides services to the transport layer
- **Link layer:** provides services to the network layer

*Note:* in each layer I have APIs that allow the communication between the layers, the objective is to provide something on the upper layer.  
*Note:* if we look at **IoT protocols** we can see that they follow the same paradigm.

*Example of a server in python:* this simple servers shows the use of many different wrapper for APIs by creating a simple server that sends back everything it receives.

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 8888))
while True:
  conn, addr = s.accept()
  print 'Connected by', addr
  while True:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
  conn.close()
```

> *Example in applications:* The application layer in the TCP/IP stack can be divided into multiple layers:
>
>- **Presentation layer:** responsible for the actual interaction with the user.
>- **Application layer:** responsible for processing the data.
>- **Data layer:** responsible for the data management.
>
> Each of these layers could be handled in many different ways. For instance if I consider a searching engine application, in the application layer I must implement a ranking of the pages, the calls for the queries handled in the data layer etc. In the data layer I can have many different kind of databases and many different way to save them physically etc.
>
>**More examples in the slides**

#### Exercise

Think of an application to download a customized version of a book, like the one suggested for the course (which is free and shipped by email after being personalized with the user name).

Once the user selects the book that he want to download, he must be able to input his data and then system should create the personalized copy and send an email providing a user a link to download it's personalized version. This means that there are the 3 application layers that we discussed before.

#### Summing up

Layers interact using up and down calls. One of the main problems is the coupling between the different layers. If the project is poorly designed a bug in a lower level could easily affect all the upper layers. A way to add layers or elements to already existing layers at runtime.

### Object-Based architecture

The components are independent and communicating through the use of method calls. The object are on different machines and each one has a state and an interface known to the others. Each object is replaceable with another object that implements the same interface.

*Note:* this is really similar to what happens in object oriented programming.

**Basic Idea:** an object is on a server and I want to call one of it's methods. The user can see an instance of the object on the server, but it's not physically on it's computer. A **middleware** is needed in order to make the user able to call the object on the server.

A **proxy** is a service that takes the arguments needed, sends the real call to the server and then sends the answer to the client. It also does the **marshaling** and **unmarshaling** of the data.

*Example:* Java and RMI (Remote Method Invocation)

```Java
public interface Rcalendar extends Remote {
  public void addEvent(String date, String event) throws RemoteException;
  public String getEvents(String date) throws RemoteException;
}
```

```Java
public class Client {
  Registry reg = LocateRegistry.getRegistry("server", 1099);
  Rcalendar cal = (Rcalendar) reg.lookup("calendar");
  System.out.println("Now: " + cal.today());
}
```

### Service-oriented Architecture (SOA)

Service-oriented architecture (SOA) is a centralized architecture in which multiple services communicate with each other to deliver a service using standardized interfaces. It’s most useful for building large, complex systems that require integration between services.

**Characteristics of a service:**

- Services interact through a communication protocol over the so-called enterprise service bus
- Services are loose coupled and can be easily replaced
- represents a specific enterprise activity
- is black-box (encapsulation)
- is self-contained
- may be made of other services
- provides a well defined interface
- is reusable
- Services maybe implemented by different providers (different administrative
organization) using different underlying technologies
- A distributed application can be thought as a service composition where services operate in harmony

#### Coordination vs Orchestration

- **Orchestration:** a central controller is responsible for the coordination of the services. The controller is responsible for the flow of the process and the interaction between the services.
- **Coordination:** the services are responsible for themselves. Each one knows what to do and when to do it.

#### Main Entities in SOA

- The **Broker** makes information about services available to consumers
- The **Provider** makes available a service and provides the Broker with the required information
- The **Consumer** locates services in the Broker registry, and then bind to the service Provider to invoke it
*Note:* the interaction between the Consumer and the Provider is governed by the **service contract**

*Example of image recognition and processing:*
![service_oriented_architecture](../Screenshots/image_recognition)
