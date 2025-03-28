# GSPN

This is a subclass of Petri nets that is obtained with the addition of **immediate transitions** and **inhibitor arcs**.

They can be seen as an union of the two classes of Petri nets we have seen before: **SPN** and **TPN**.

## Formal definition

The formal definition of a GSPN is a 8-tuple:

$$GSPN = (P, T, \Pi, I, O, H, W, m_0)$$

Where:

- $PN=(P, T, \Pi, I, O, H, m_0)$ is the priority petri net
- $\Pi$ is the priority function that maps transitions into non-negative natural numbers representing their priority level
- $H$ is the inhibitor function
- $W: T \to \mathbb{R}^+$ is the weight function that maps transitions into positive real numbers. *Note:* this function might represent a rate if T is a timed transition or a weight if T is an immediate transition

Moreover the net must be **confusion free**.

## Transitions in GSPNs

- **Enabling rule**: same as the priority SPNs.
- **Firing rule**: same as the priority SPNs for timed transitions. For immediate transitions the firing rule is the same as the Priority PNs
- **Firing time for timed transitions**: negative exponential distribution and statistically independent
- **Rate of T_k**: $W(T_k)$, rate of the exponential distribution associated with a transition $T_k$
- **Weight of t_h**: $W(T_h)$, weight of the immediate transition $T_h$
- **Timed transitions**: rate policy and priority 0
- **Immediate transitions**: priority > 0 (1 if not otherwise specified)

### Immediate transitions

They are used to represent the state changes in a system without transition time. They are used instead of timed ones in all cases in which the time associated with the time transition is **negligible**.

They allow to reduce the dimension of the reachability graph and can mitigate the stiffness problem. Moreover they also allow to model situations of probabilistic choice between more alternatives.

## Tangible and vanishing markings

In **Tangible markings** only timed transitions are enabled so the time spent in a tangible marking is positive.

Therefore in a tangible marking the behaviour of GSPN and of enabled time transitions is analogous to the behaviour of the SPN.

In **Vanishing markings** only immediate transitions are enabled so the time spent in a vanishing marking is zero.

Therefore in a vanishing marking the behaviour of GSPN and of enabled immediate transitions is analogous to the behaviour of Priority PNs.

*Note:* if a transition is disabled it's not counted in the definitions of both tangible and vanishing markings. This means that if I have a GSPN with both timed and immediate transitions I can never have a marking in which I have both immediate and timed transitions enabled. This is because of the use of the priority that automatically disables the other type of transition.

## Probability of firing

Given k transitions: $t_1, \dots, t_k$ all enabled on the same marking m with or without conflict with:

- weights: $w_i$ for $i = 1, \dots, k$ if immediate
- rates: $r_i$ for $i = 1, \dots, k$ if timed

The probability $P(t_i|m)$ of firing the transition $t_i$ in a marking m is:

$$P(t_i|m) = \frac{w_i}{\sum_{j=1}^k w_j}$$

### Conflict and concurrency

In general **conflict** and **concurrency** can happen between immediate transitions only if those transitions have the same priority.

Using the weights we can resolve probabilistically:

- direct conflicts
- indirect conflicts
- confusion

And the marking that we reach depends on the transition that fires first.

In the case of concurrent immediate transitions and with the absence of confusion the choice on which transition fires first is not relevant.

GSPNs **must be confusion free** because in the presence of confusion there are some edge cases that cannot be handled.

For instance if we extend the GSPN adding an immediate transition and a place between a transition which generates confusion and its output place.

The confusion causes a change in the graphical description of the model and also produces different transition probabilities.

*Note:* a GSPN with confusion is defined as **semantically wrong**, to understand if this is the case we can also use automated tools (or network structure or state space generation).

The stochastic process associated with the marking a GSPN:

$$\{M(t), t \geq 0\}$$

With $M(0) = m_0$ and $M(t)$ is the marking of the GSPN at time t.

### Reduced reachability set and reachability graph

The **vanishing** markings make more expensive solving the CTSMC. Sometimes it might even be impossible to actually work with the vanishing markings still present.

For this reason we start by removing the vanishing markings and then we compute the **transition rates** for the remaining markings (stable).

The **stochastic process** associate with the stable markings is basically an SPN. And we can compute the **reduced reachability set** and the **reduced reachability graph**.

#### Generating the CTMC associated with a GSPN

1. Each state of the CTMC is obtained by associating a state $s_i$ to each stable marking $m_i$ of the GSPN
2. The transition rate from a state $s_i$ to a state $s_j$ with $i \neq j$ is obtained as sum of the values:
    - the transition rate of transitions T enabled in $m_i$ that enable $m_j$
    - the transition rate of transition T that are enabled in $m_i$ and whose firing generates a vanishing marking m ($m \neq m_i$, $m \neq m_j) multiplied by the probability of reaching $m_j$ from m

### Extensions of GSPNs

Extending the GSPN can make them more flexible and able to represent more different scenarios.

This also come with an increase in complexity of the models.
