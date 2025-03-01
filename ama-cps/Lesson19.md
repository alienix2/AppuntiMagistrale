# Petri nets (First lecture of the second semester)

*Note:* in the next lectures the previous parts should be used as a basis (Markov chains in particular).

The **markovian** can be seen as a language, and in this regard a very low level language. In this part of the course we will see a higher level language in the Petri nets. The idea is that we can somehow "compile" the Petri net in order to obtain some kind of markovian chain.

## PT Petri nets

We will focus on this kind of Petri net for the very first part. These are the easiest kind and the basic on which we can build more complex ones.

### History and basics

**Carl Petri** first introduced the concept of a Petri net when he was only 13. He kept on working on the topic as he grew up.

The Petri nets are used to model and evaluate:

- Dependability
- Performance
- Performability

*Note:* with **performability** we mean the combination of performance and dependability, basically *how much well a system performs considering that the system can fail*, *how well the system performs at different levels of degradation*.

With Petri nets many system behaviors can be modeled, such as:

- Sequentialization
- Randomness
- Parallelism
- Non determinism
- Synchronization
- Mutex, Time, Conflict, etc.

*Note:* they can describe both **qualitative** and **quantitative** aspects of a system.

### Constraints

The basic PNs doesn't take into consideration some of the aspects above. Even if we consider that we can build them in a way that allows to build more complex kind of PNs on top of them. (**Stochastic PNs**)

The PNs can be classified as **Markovian** or **Non-Markovian**. The first ones are the ones we will focus on.

*Note:* on the slides there are many examples of PNs, we won't see many of them in this course, but the prof's work group developed and improved some of them.

### Tools

We will use a tool called **Mobius** to model and evaluate the PNs. It is a very powerful tool that can be used to model and evaluate many different kind of systems. The tool includes many solvers including the ones we need.

### Combinatory vs State-space

Until now we looked at the combinatorial methods, now we are moving into the **state-space** modeling. Actually the Markov chains were in the state-space modeling.

The main difference is that we don't have a fixed number of states, but we have a set of states that can change over time.

#### Pros and cons

The combinatorial methods don't require to define the space-state, they are simple and intuitive and are based on the statistical independences of all the components. The main issue is that they are not suitable for very complex dependencies.

The state-space are a lot more powerful but they are also a lot more complex to work on. The thing is that actually when the system in itself is complex then they are able to model the simpler in a clearer and easier way.

### Model analysis

How can we evaluate a model? Usually we look at two properties:

- **Modeling power**: how well the model can represent the system
- **Analysis power**: how easy it is to analyze the model

Usually the point is that a model that has an high modeling power is likely going to have a low analysis power as it is usually more complex.  On the other hand a model that easy to analyze is going to usually lack the capacity to represent complex features of the original system.

## Place/Transition PNs

These kind of models have:

- a net structure N: **static part**
- a marking m: **state of the system**

A system is composed of a set of places and transitions. The places are usually a circle, and the transitions are usually rectangles (very slim rectangles)

The **state** of a system is the set of all the places that are marked.

The **arcs** are the connections between the places and the transitions. The arcs are usually directed and have a weight. If an arc doesn't have a weight it's weight is considered to be one.

### Definitions

A **marking** is a function m (# or mark) that associates a non-negative integer to each place in the net. $m(p)$ is the number of tokens in place p.

A marking is usually represented as a vector of integers.

A **P/T PN with marking** is a quintuple: $PN = (P, T, A, v, m_0)$ where:

- P is the set of places
- T is the set of transitions
- A is the set of arcs
- v is the function that associates to each arc a place or a transition
- $m_0$ is the initial marking

A **P/T PN withou marking** is a quadruple: $PN = (P, T, A, v)$ where:

- P is the set of places
- T is the set of transitions
- A is the set of arcs
- v is the function that associates to each arc a place or a transition

*Note:* look at the slides for an example and an exercise.

### PN evolution

The PN evolves according to the marking and follows specific rules.

The marking change when tokens are moved from one place to another, in particular when a transition is **fired**. The firing consumes and produces tokens.

The firing should be regulated by an **enabling condition** and the related **firing rule**.

The **enabling condition** sets the condition to fire: a transition t is enabled in a marking m if and only if the amount of tokens $m(p)$ in all the input places p of t is greater or equal than the weight of the input arcs from p to t.

The **firing rule** is the rule that regulates the firing of a transition. When a transition is fired the tokens are moved from the input places to the output places. When a firing happens first the tokens are removed from all the input places specified by the weight of the input arc from p to t, then the tokens are added to each output as defined by the weight of the output arcs from p to t.

*Note:* the transition cannot fire if "in the meanwhile" another transition firing generates a marking in which it is no longer enabled. If I have some kind of non-determinism I need to elaborate all the possibilities and create all the diagrams for the different possibilities.

When the firing of an enabled transition in $m_1$ produces the marking $m_2$ we write $m_1 \xrightarrow{t} m_2$, which means that $m_1$ is **directly reachable** from $m_0$.

An input without any input places is always enabled and called a **source**. A transition without any output places is called a **sink** (cause it's not generating token)

The **enabling degree** of a transition t in a marking m is defined as:

$$
e_t(m) = \min \left\{ \lfloor\frac{m(p)}{v(p, t)}\rfloor | p \in P, (p,t) \in A \right\}
$$

In a P/T PN this represents the amount of enabled consecutive firings of a transition starting from a marking m

## Using the PNs

With a PN we can study some kind of properties:

- **Structural:** based only on the structure
- **Behavioral:** depending on the initial marking, some of those are:
  - Reachability
  - Boundedness
  - Reversibility
  - Liveness

The PNs are always based on what is called **Interleaving semantics** meaning that for each marking only one firing can be observed at a time.

### More definitions

Given a sequence of firings we can say that when the firing of r transitions of a sequence changes the marking of a PN from $m_i$ to $m_j$ we can say that the marking $m_j$ is reachable from $m_i$ (in r steps).

*Note:* in a P/T PN the order of the transitions is not relevant when all the transitions in a sequence are all enabled and a firing of one of the transitions is not changing the enabling degree of other transitions.

A **reachability set**, $RS(m_0)$ of a P/T PN is the set of all the markings reachable from the initial marking $m_0$.

By analyzing the RS we can tackle two problems:

- **reachability:** does the modeled system reach a specific state starting from the initial marking?
- **boundedness:** is the number of state bounded?

The PN is called **k-limited** if the amount of tokens in each places does not exceed a finite value k for each marking in RG.

The model system **reaches a state** from the state specific by the initial marking if the marking of the destination state is in the $RS(m_0)$

The **reachability graph** of a P/T PN is a directed labeled multigraph (RS, F) where RS is the set of nodes and F is the set of arcs. RS is the **reachability set** of the PN.

*Note:* this is a multigraph because it can have multiple arcs between two nodes.

The RG allow to check the **reversibility** and the **liveness**.

A PN is **reversible** if for each marking m in the RG there is a marking m' in the RG such that m is reachable from m' and vice versa. This information is important in repairable systems, where the system can go back to a previous state.

A transition is **live** if it can be fired infinitely many times (basically it's always enabled). A PN is **live** if all the transitions are live, otherwise it's called **dead**.

*Note:* if at least one transition is alive in a PN then there is no deadlock.
