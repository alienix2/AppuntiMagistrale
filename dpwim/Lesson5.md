# Design goals of distributed systems

## Goal 1: Sharing Resources

The first goal in distributed systems is to make it easy for users to access remote resources and share them in a way which is effective and controlled.  
**Example of resources:**
- devices (cameras, printers, temperature sensors, etc.)
- computational power (cpu, VMs, etc.)
- files
- data (temperature in a house, number of parking lot available, etc.)

**Real examples:**
- BitTorrent: a peer-to-peer file sharing protocol
- Google Maps: users share information about traffic, accidents, etc.
- SETI@home: a distributed computing project that uses the idle time of personal computers to execute some tasks for research purposes

*Note:* as already stated the way to share resources is controlled, and that means that someone decides how resources can be shared.

## Goal 2: Distribution Transparency

This means that we want the end users to be able to access the resource without knowing that the resources are spread around the network. If this actually succeeds the system is called **transparent**.  
### Kinds of transparency:

**Access transparency:**  
this deals with hiding differences in data representation and how the data can be accessed by the user.  
*Example:* we consider big-endian and little-endian integer representation. In networking TCP/IP protocols always encode the fields in the network byte order format. This means that every host that wants to use the protocols must use system calls to convert it's information to network byte order.  
*Other example:* coordination of multiple OS. Two system can use different file convention or file systems, there usually are system calls that allow communication between different systems.

**Location transparency:**  
this deals with hiding where the resources are physically located in the system. The way we can refer to the resources is fundamental to allow location transparency.  
Usually the best way to use location transparency is to assign logical names to the resources. This way the user doesn't need to know the real location.

**Migration transparency:**  
this deals with hiding the fact that the resource could be moved from a location in the system to another. The point is to create a system in which if we change the location of a resource, it can still be accessed in the same way.  
*Example:* we consider a system using a RDBMS that wants to be changed to be a NoSql database. The users that use the system shouldn't even notice that we did that change cause they don't interact with the database directly. *Note:* there are other things to consider like the time actually needed to change from a database to the other once the NoSql database is being introduced, but we aren't talking about that in this case.

**Relocation transparency:**  
this deals with hiding the fact that the resource could be moved from a location in the system to another **while it's being used**.  
*Example:* moving a VM from a point of the system to another without shutting id down.

**Replication transparency:**  
this deals with hiding the fact that the resource could be replicated in the system. Usually the resource is replicated more than one in real case scenarios, the point is that the user shouldn't know about that and shouldn't even care which of the replica he's using in a specific time.  
This type of transparency relies heavily on the location transparency. That is because in order to achieve replica transparency you must use logical name and have location transparency already implemented.

**Concurrency transparency:**  
in this case we consider a system that can handle more than one user at a time.  
This deals with hiding to a user the fact that there are other users that are using the same resource at the same time, each user should think that all the system is available for him to use.  
The main problem that must be solved is the possibility of having resource left in an **inconsistent** state. The difference between network concurrency problem and classic concurrency problem is that on the network there are many more problems that might occur (*I.e:* due to latency)

**Failure transparency:**  
this deals with hiding the fact that a resource fails. If a resource actually fails the user shouldn't care and should still be able to work on the system.  
*Example:* a google server fails, the user is still able to access his data on another server and therefore he doesn't care.

***Note:*** all these kind of transparency are not independent, they are connected with one-another. Sometimes specific kind of transparency might not be needed.

## Goal 3: Openness
To be open a system must provide:
- Standard interfaces
- Flexibility
- Interoperability: this means that we use different components from different providers but they can still cooperate with each-other
- Portability: this means that the system can be moved from one platform to another without changing the code
- Extensibility: this means that if I add new components or replace existing ones, the system won't break

**Standard interfaces:**
When we have a problem we must always try to create a model that can represent it. In particular in this case we use an **Interface definition language** IDL. This language is used to describe the syntax of the services, but it cannot define well the semantics.  
**Semantics** is usually defined using another kind of documentation which most of the time is written in natural language.  
*Example of IDL:* CORBA (Common Object Request Broker Architecture)

**Flexibility:**  
When we consider a system we usually want it to be flexible. This means that the system has many independent component that interact with each-other and can easily be replaced and extended singularly.

**Policies vs Mechanisms:**  
- **Policies:** define what is to be done
- **Mechanism:** defines how it is to be done

The point is that we want to separate the two so that if we change the policy, the mechanisms still work. *I.e:* I have data that must replaced every two days, if I decide to change the policy so that it gets replaced every day, the mechanism doesn't need to be changed.  
*More examples:*
- description of the resource that a component may access **policy**
- ACL **mechanism**
- the operation that a downloaded code may perform **policy**
- different encryption algorithms **mechanism**
- specify different levels of communication **policy**

**Why the two should be separated?** Because this allows to change each of the two without changing the other (in general)

## Goal 4: Scalability
This refers to the ability of a system to grow and manage an increasing amount of work
*Example:* a system with a single server for all the user. **NOT** scalable.  
*Note:* scalability is one of the goals, sometimes it is considered the most important one but many times it is not.

**Scalability dimension:**
- size
- administrative
- load
- functional
- geographical

**Size scalability:**  
The ability of the system to work efficiently when the number of request or resources  increases. *I.e:* a search engine works well even if the number of indexed documents increases

**Horizontal vs Vertical scaling:**
- **Horizontal:** adding more nodes to a system
- **Vertical:** adding more power to an existing node

**Administrative scalability:**
This refers to the ability of the system to be managed well even when the number of administrative domain increases. This type of scalability isn't really needed in some cases, but nowadays this should always be taken into account. *I.e:* if I have a lot of employees in my company, how much resources should each employee be allowed to access? If I have employees in multiple countries I must be able to comply to the laws of each country they work in.

### Scaling techniques
In order to apply the scaling techniques we must consider some challenges:  
**Hiding communication latency:**  
The approach to hide the latency depends on the type of communication that we are using.  The main two approaches are **synchronous** and **asynchronous** communication.  
In most cases the faster approach is the asynchronous one, but it's also the most complex one. Also there are specific cases in which send the information in a synchronous way is needed. Using the asynchronous approach allows to hide communication latency is some cases.  
Another approach to reduce the latency is to move a part of the computation to the client-side.

**Partition and distribution:**
This is a technique that allows to divide the system in multiple parts. This is usually done to reduce the load on a single node.

**Caching and replication:**  
This is a technique that allows to store a copy of the data in a different location. This is usually done to reduce the latency of the system cause two users that need the same resource can actually be redirected to different nodes that offer the same resource.

**Partitioning a task:**  
There are specific tasks than can be divided in multiple parts and executed in parallel. This is usually done to reduce the time needed to execute the single task. It is also useful to allow a node to handle multiple user at the same time by working on a part of the problem only for all the users.
