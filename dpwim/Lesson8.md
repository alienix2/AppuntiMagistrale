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
