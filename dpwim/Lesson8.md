# More on design goals of distributes systems

## Goal 5: Availability

**Intuitive definition:** an answer should always be provided an answer to a request, if the process answering didn't fail, **eventually**. This means that there is not upper bound to the time needed to formulate a reply.

There are two thing to consider:

- failure should be detected as fast as possible
- the system should have a way to recover from a failure

## Goal 6: Modularity

An application should be composed of many different modules. Each module should implement an interface that allows other modules to communicate with them. The functional and implementation aspects are independent and each module could also use different programming language.

This allows to replace a module with another one that implements the same interface without changing the rest of the system.

## Challenges in distributed systems

**Typical questions:**

- What is the right interface and abstraction?
- How should I partition my system for scalability and modularity?
- How can I detect features?
- How do nodes coordinate?

**Some other challenges:**

- **Security:** authentication, protection from attacks, isolating misbehaving nodes etc.
- **Implementation:** is there a bottleneck? How can I reduce that bottleneck?
- **Quality of service:** load balancing (*I.e:* if I have many replica in our system, I should divide the workload between them, otherwise this is useless), responsiveness, throughput, etc.

## RESTFul Architecture

The basic idea are:

- **Resources:** everything is a resource, and each resource is identified by a URI
- All the services offer the same interfaces: GET, POST, PUT, DELETE
- **Stateless:** the server doesn't keep track of the client state (this is the client's responsibility)
- Messages are fully **self-described** which means that each message includes enough information to process it.

### Restful resource

A resource is a concept that can be stored or retrieved. It can be a document, a photo, a collection of other resources, a service, etc. The important thing is that it is identified by a URI.

*Note:* a resource could be a collection or a single element. Resources may contain sub-resources and there in **no** name conventions for URIs (even if there are some conventions and best practices)

### Restful operations

The operations that can be performed on a resource are:

- **GET:** retrieve the resource
- **POST:** create a new resource
- **PUT:** update a resource
- **DELETE:** delete a resource

### Some observations

In a REST architecture, the components are **referentially* and **temporally** coupled. This means that:

- the client knows the URI of the resource
- the client and the server must be up and running at the same time.

This has some **pros** and some **cons**:

- **Pros:** the interaction is easy to implement
- **Cons:** in high dynamic system the model presents some limitation. *I.E:* if a lot of clients are opening and closing connections I might have some performance issue.

### Coordination model

The models that are commonly used are based on the processes being coupled/decoupled referentially and temporally:

|   |Temporally coupled|Temporally decoupled|
|-|-------------------|--------------------|
|**Referentially coupled**    |Remote Procedure Call (RPC)|Message Passing|
|**Referentially decoupled**|Publish/Subscribe|Event-based|

## Public-Subscribe

This idea is based on 3 kind of nodes:

- **Publisher:** they broadcast messages without knowing who will receive them
- **Subscriber:** they receive messages without knowing who sent them
- **Broker:** it is the intermediary between the two. It receives messages from the publisher and forwards them to the subscriber.

Publisher and subscriber are decoupled referentially and the broker is decoupled temporally. The communication is one to many cause a mesasge from one publisher can be sent to many subscribers. One of the main issue of this method is that the broker could be a **bottleneck** if we consider a system with a single broker for many publisher and subscribers, but the broker could be decentralized in that case.

### Subscription filters

The broker can filter the messages that are sent to the subscribers. There are three ways to do that:

- **Topic-based:** This is done by using a **topic** that is a string that is used to filter the messages. If a subscriber is not interested in the **topic** of a message, the broker will know that and won't forward the message to him.
- **Content-based:** This is done by using the content of the message to filter it. The broker will check the content of the message and will forward it only to the subscriber that are interested in that content. (*I.e:* if the mail contains "Acme" I want to receive, otherwise I don't)
- **Type-based:** This is done by using the type of the message to filter it. The broker will check the type of the message and will forward it only to the subscriber that are interested in that type. The difference with topic-based is that in this case each type can specify attributes and methods and we also have the concept of sub-typing

*Example:* MQTT Protocol in Java:

```Java
MqttClient client = new MqttClient("tcp://localhost:2018", MqttClient.generateClientId());
client.connect();
MqttMessage message = new MqttMessage();
message.setPayload((new Date()).toString()).getBytes());
client.publish("today", message);
client.disconnect();
```

```Java
public class SimpleMqttCallBack implements MqttCallback {
// ...
  public void messageArrived(String s, MqttMessage mqttMessage) throws Exception {
      System.out.println("Message received:\n\t" + new String(mqttMessage.getPayload()) );
  }
  // ...
}
```

```Java
MqttClient client=new MqttClient("tcp://localhost:1883",MqttClient.generateClientId());
client.setCallback( new SimpleMqttCallBack() );
client.connect();
client.subscribe("today");
```

## Tuple Space

This is a model that is based on the idea of a **shared memory**. The idea is that the memory is shared between the processes and the processes can read and write in this memory. The memory is a collection of tuples and each tuple is a collection of fields. The components can put data in the shared space and then to retrieve them they provide a research pattern that is compared with the tuples in order to find the matching ones.

The tuples are permanent and never removed, if not explicitly stated. Also this means that if the consumer of a tuple is not yet ready to receive it that's not a problem.

### Linda

In Linda we have three operations:

- **in(t):** it removes a tuple t from the tuple space and returns it to the caller
- **out(t):** it inserts a tuple t in the tuple space
- **rd(t):** it reads a tuple t from the tuple space without removing it

*Note:* in this case in e rd are blocking operations, while out is not.
