# Clock Synchronization in Distributed Systems

**Important note:** automatically generated with Claude starting from the slides

## Basic Concepts

### Key Assumptions

- Each machine/entity in a distributed system has its own local clock
- There is no notion of global time; time depends on individual entities and observers

### Common Problems

1. **Make on Different Machines**
   - File timestamps can be mismatched due to unsynchronized clocks
   - Can lead to compilation issues when timestamps are inconsistent

2. **Message Causality**
   - Need to track message dependencies
   - Important for undoing actions or handling message cascades

3. **Database Replication**
   - Updates must be performed in the same order across replicas
   - Example: deposit $100 followed by 1% interest calculation

## Physical Clock Synchronization

### Physical Clock Mechanics

- Timers use crystal oscillations at defined frequencies
- Components:
  - Counter register: decremented at each oscillation
  - Holding register: resets counter value
  - Clock tick: interrupt triggered when counter reaches zero

### Challenges

- Crystals in different machines run at slightly different frequencies
- Clock skew creates differences between machine readings
- Network issues complicate synchronization:
  - Arbitrary message delays
  - Potential message loss

### Synchronization Approaches

#### External Synchronization

- Synchronize all machines to an external reference clock
- Example: Coordinated Universal Time (UTC)
  - Based on atomic time
  - Broadcast via radio stations and satellites

#### Internal Synchronization

- Keep all machines synchronized with each other
- No external reference needed

### Synchronization Algorithms

#### Cristian's Algorithm

1. Client sends request with timestamp T0
2. Server responds with its time T
3. Client records receipt timestamp T1
4. Round trip time estimated as (T1 - T0)/2

#### Berkeley Algorithm

- Internal synchronization among machine set
- Process:
  1. Master elected
  2. Master polls slaves for their time
  3. Master estimates times considering round-trip delays
  4. Average time calculated
  5. Master sends adjustment values to slaves

#### Network Time Protocol (NTP)

- Widely deployed Internet time synchronization protocol
- Hierarchical structure:
  - Stratum 0: High-precision devices (atomic clocks)
  - Stratum 1: Machines synchronized within microseconds
  - Lower strata with increasing potential deviation
- Process:
  1. Client sends timestamped request (T1)
  2. Server records receipt time (T2)
  3. Server sends response with timestamp (T3)
  4. Client records receipt time (T4)
  - Calculations performed to determine offset and round-trip time

## Logical and Vector Clocks

### Virtual Time

#### Core Concept

- **Problem Statement**: Create a common notion of time C among all entities without using physical clocks
- **Goal**: Assign time values C(e) to events that all entities agree upon

#### Requirements

1. **Causality Preservation**: If a→b then C(a) < C(b)
2. **Efficiency**: Avoid generating additional messages
3. **Consistency**: All entities must agree on time values

### Lamport's Logical Clocks

#### Algorithm Details

##### Counter Clock Rules

1. **Local Event Rule**
   - Before performing an event: Cx := Cx + 1
   - Cx represents clock of entity x

2. **Message Sending Rule**
   - When sending message M: Set timestamp ts(M) with current Cx
   - Include timestamp in message

3. **Message Receiving Rule**
   - When receiving message M from y:
   - Adjust local counter: Cx := max{Cx, ts(M)}
   - Execute local event rule before processing M

#### Application: Total-ordered Multicast

##### Problem Context

- Need to ensure consistent order of updates across replicas
- Example: $100 deposit followed by 1% interest calculation

##### Implementation Requirements

1. **Network Setup**
   - Complete network of entities multicasting messages
   - Messages timestamped with logical time
   - Messages from same sender received in send order

2. **Queue Management**
   - Each entity maintains message queue
   - Messages conceptually sent to sender too

##### Algorithm Steps

1. **Message Reception**
   - Apply Lamport's algorithm for clock adjustment
   - Store message in local queue

2. **Acknowledgment**
   - Send ACK message to all entities in group

3. **Message Delivery**
   - Deliver when message is:
     - At front of queue
     - Acknowledged by all entities

### Vector Clocks

#### Fundamental Concepts

1. **Purpose**
   - More detailed representation of event relationships
   - Captures causality that Lamport clocks miss

2. **Structure**
   - Each entity x maintains vector VCx
   - For n entities in system:
     - VCx[x]: Number of local events
     - VCx[y]: Known events at other entities

#### Vector Clock Algorithm

##### Rules

1. **Local Event**

   ```
   Before event: VCx[x] := VCx[x] + 1
   ```

2. **Message Send**

   ```
   Set ts(M) to VCx after local update
   ```

3. **Message Receive**

   ```
   For each k:
   VCx[k] := max{VCx[k], ts(M)[k]}
   Then execute local event rule
   ```

#### Comparison Operations

##### Vector Timestamp Relationships

1. **Less Than Relation**
   - ts(M1) < ts(M2) if:
     - All components: ts[M1](k) ≤ ts[M2](k)
     - At least one: ts[M1](k') < ts[M2](k')

2. **Concurrent Events**
   - Neither ts(M1) < ts(M2) nor ts(M2) < ts(M1)

#### Causally-ordered Multicast Using Vector Clocks

##### Implementation Details

1. **Initialization**

   ```
   VCx[j] := 0 for all j = 1,...,n
   ```

2. **Message Send**

   ```
   VCx[x] := VCx[x] + 1
   sendToAll(ts(M))
   ```

3. **Message Receive**

   ```
   Enqueue M locally
   Deliver when:
   - ts(M)[y] = VCx[y] + 1
   - ts(M)[k] ≤ VCx[k] for k ≠ y
   Then update:
   VCx[k] = max(VCx[k], ts(M)[k]) for all k
   ```

#### Key Properties and Advantages

1. **Causality Tracking**
   - Accurately captures happened-before relationships
   - Identifies concurrent events

2. **Consistency Guarantees**
   - Ensures causal delivery order
   - Maintains distributed system consistency

3. **Message Ordering**
   - Related messages delivered in consistent order
   - Unrelated messages may be delivered in any order

#### Limitations and Considerations

1. **Storage Overhead**
   - Vectors grow with system size
   - Each message carries vector timestamp

2. **Processing Overhead**
   - Vector comparisons more complex than scalar
   - More state to maintain per entity

3. **Scalability Concerns**
   - Vector size grows linearly with number of processes
   - May become bottleneck in large systems
