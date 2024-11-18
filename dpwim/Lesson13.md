# Message-oriented middleware

The basic idea is that two components communicate by exchanging messages without having to be synchronized because there is a buffer in the middle that stores the messages. *Note:* the basic idea is similar to an e-mail.

## Communication properties

The communication can happen only by adding/removing messages from queues. Also the comunication is loosely coupled in time:

- the receiver doesn't have to be active when the sender sends the message
- a message remains in the queue until it is explicitly removed

### Messages

Messages can contain any kinds of data and may be of any size within a given limit. The middleware can support automatically fragmentation of messages.

A destination is identified together with its queue by a systemwide name. Each message contains the address/name of the destination

### Queue managers

Queue managers can be implemented as a library linked to the application or a separate process. Since each application is associated with a **local queue** this means that is must also have a queue manager.

An application can send/receive messages to/from it's local queue. *Note:* to support persistent asynchronous communication, queue managers should be implemented as separate processes.

### Addresses

Each queue must have a logical name/address that is unique within the system. The address is used to identify the destination of a message, which means that every logical name must be associated with a network address (ip_address:port).

To manage a messaging queue system we must connect the queue managers with the overlay network. Another effort that must be done is to manage the network if a new queue should be added.

### Heterogeneity

The **MoM** (Message-oriented Middleware) should support different kinds of systems and languages. This means that the middleware should provide a way to translate the messages between different systems.

They usually use a **message broker** which allows to translate the messages between different protocols, allowing systems that use different protocols to be able to communicate.

### Case study AMQP

In **AMQP** we have different parts well defined:

- **Messaging service**
- **Messaging protocol** that defines the format of the messages
- **Messaging interface** used by the programmers to write their application

In AMQP there three kinds of entities:

- **Producer**
- **Consumer**
- **Queue**

A consumer can indicate a producer if the message has been successfully processed or has been rejected. A message marked as **durable** won't be lost if the broker crashes.

**Exchanges** are used to route messages to queues. They can be of different types:

- **Direct:** the message is sent to the queue with the same name as the routing key
- **Fanout:** the message is sent to all the queues
- **Topic:** the message is sent to the queues that have a routing key that matches the message
- **Headers:** the message is sent to the queues that have the same headers as the message

They have several attributes:

- **Name**
- **Durability:** if the exchange should survive a broker crash
- **Auto-delete:** if the exchange should be deleted when no queues are bound to it
- **Arguments:** used to configure the exchange

### Direct exchange

In the case of a direct exchange, the message is sent to the queue with the same name as the routing key. When a queue is bound to an exchange it can specify a routing key. If the routing key of the message matches the routing key of the queue, the message is sent to the queue.

### Fanout exchange

In the case of a fanout exchange, the message is sent to all the queues. When a queue is bound to an exchange it doesn't specify a routing key. This means that the message is sent to all the queues.

### Topic exchange

In the case of a topic exchange, the message is sent to the queues that have a routing key that matches the message. The routing key is a string that can contain wildcards such as:

- **\***: matches exactly one word
- **#**: matches zero or more words

### Headers exchange

In the case of a headers exchange, the message is sent to the queues that have the same headers as the message. The headers are a dictionary that contains the headers of the message.

### AMQP Message attributes

The message has several attributes:

- **Content type**
- **Content encoding**
- **Headers**
- **Delivery mode:** if the message is durable or not
- **Priority:** the priority of the message
- **Correlation id:** the id of the message
- **Reply to:** the queue where the response should be sent
- **Expiration:** the time when the message should be deleted
- **Message id:** the id of the message
- **Timestamp:** the time when the message was sent
- **Many more**

### Example: Hello world in RabbitMQ

In this case we will use **RabbitMQ** that is an implementation of **AMQP**.

We consider two clients: a **producer** and a **consumer**. The producer sends a message to the queue and the consumer receives the message from the queue. The consumer also registers a callback that is called when a message is received. (*See:* <https://github.com/rabbitmq/rabbitmq-tutorials/tree/main/go>)

*Note:* see also the publish-subscribe example in the same repository: <https://github.com/rabbitmq/rabbitmq-tutorials/tree/main/go>

### Case study: ZeroMQ

**ZeroMQ** is a high-performance asynchronous messaging library that provides a message queue, but it doesn't provide a broker. The idea is to resemble the **Berkeley sockets**

All the communications are handled using sockets that support many-to-many communication.

The main patterns implemented are:

- **Request-reply:** the client sends a request and waits for a reply
- **Publish-subscribe:** the client sends a message to all the subscribers
- **Push-pull:** the client sends a message to the first available worker (fan-out/fan-in pattern)

Each of these three patterns define a specific infrastructure.
