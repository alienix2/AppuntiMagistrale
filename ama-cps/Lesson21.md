# Stochastic Petri nets

A PN is stochastic when the firing delay assigned to a timed transition is sampled from a random variable.

There are multiple kinds of stochastic PNs, we will see some of them in this course (SPN, GSPN, SAN)

## Stochastic Petri nets in general

Informally the SPN are just P/T PNs with the addition of time. The firing delays are assigned following a **negative exponential distribution**.

The transition firing are statistically independent and the **transition rate** $T_k$ or $\lambda_k$ is the rate of the exponential distribution associated to a transition $T_k$

### Definition

A SPN is a tuple $(P, T, I, O, \bigwedge, m_0)$ where:
$P = {p_1, ..., p_n}$ is the set of places (finite)
$T = {t_1, ..., t_m}$ is the set of transitions (finite)
$P \cap T = \emptyset$ and $P \cup T \neq \emptyset$
$I: (P \times T) \cup (T \times P) \rightarrow N$ is the input function
$O: (P \times T) \cup (T \times P) \rightarrow N$ is the output function
$\bigwedge: T \rightarrow R^+$ is the firing delay function
$m_0: P \rightarrow N$ is the initial marking

### Enabling and firing rules

**Enabling rule**: same as P/T transitions  
**Firing rule**: a transition T, enabled at time t with a firing delay d sampled from an exponentially distributed random variable fires at time t+d only if it remains enabled for the whole interval $[t, t+d)$  
**"race" policy**: with more transitions enabled in the same marking, the transition that fires first is the one reaching first 0

### Conflict and concurrency

The conflict between transitions is solved in a **probabilistic way**. The choice is based on the transition rate of all the transitions in conflict. (race policy)

The concurrecy between transition is described in this way: from the Markovian memoryless property of the exponential distribution, after making a change, the remaining time at the firing of still enabled transitions is exponentially distributed, independently on the memory policy adopted by the transitions.

#### Measures of interest

Some related measures include:

- probability that a transition fires before the others
- minimum firing time of two transitions: holding time of the SPN in marking $m_0$
- probability that two transitions fire at the same time

We consider $X_1$ and $X_"$ as statistically independent random variables, exponentially distributed with rates $\lambda_1$ and $\lambda_2$ which represent the firing delays of $T_1$ and $T_2$

The minimum firing time of the two transitions is $min{X_1, X_2}$, moreover:

$P(Y \leq y) = 1 - P(Y > y) = 1 - e^{-(\lambda_1 + \lambda_2)y}$ so $E[Y] = \frac{1}{\lambda_1 + \lambda_2}$

The probability that $T_1$ fires before $T_2$ is $P(X_1 \leq X_2) = \frac{\lambda_1}{\lambda_1 + \lambda_2}$

The probability that $T_1$ and $T_2$ fire at the same time is $P(X_1 = X_2) = 0$

### Generalization

k transitions $T_1, ..., T_k$ exponentially distributed with rates $\lambda_1, ..., \lambda_k$ all enabled in the same marking $m_0$ with or without conflict:

- $m_i, i=1, ..., k:m_0 \xrightarrow{T_i} m_i$
- $\lambda_i, i = i, ..., k$ rates for moving from $m_0$ to $m_i$
- outgoing transition rate from $m_0$: $\lambda = \sum_{i=1}^{k} \lambda_i$
- probability that $T_i$ fires before the others: $\frac{\lambda_i}{\lambda}$

Firing time of $T_2$ after the firing of $T_1$:

- $T_1$ fires at time d before the firing of $T_2$ with $d \geq 0$
- $m_0 \xrightarrow{T_1} m_1$
- $T_2$ is still enabled in $m_1$

The remaining time of the firing of $T_2$ at the instant of time d is:

$$X^{'}_2 = [X_2 -d | X_2 > d]$$

And it is exponentially distributed with rate $\lambda_2$

$X^{'}_2$ has the same exponential distribution as $X_2$: $P(X^{'}_2 < t) = 1 - e^{-\lambda_2t}$

This means that **the probabilistic behaviour of the SPN is not affected by the memory policy** of the transitions (continue or restart). This conclusion is not true if the transition rate depends on the marking of the network, when the restarting mechanism is used

#### Transition rate depending on the marking

In this model I have that:

- $\lambda(T_k, m) = \lambda_k(m)$: transition rate of $T_k$ in marking m
- the model is more compact
- but it might have some problems from the loose of locality and the need to know all the possible system states

For this reason we might think of reducing the dependence specifying the rates as product of two factors:

- nominal rate (positive real number)
- a function that depends only on the marking of the input places and inhibitor places of the transition that return a positive real number

### SPN and time approach

The stochastic process associated with the making of changes of a SPN: ${M(t), t \geq 0}$ with $M(0) = m_0$ and $M(t)$ is the marking of the SPN at time t

The process ${M(t), t \geq 0}$ is a HCTMC (CTMC for brevity) thanks to the Markovian memoryless property of the exponential distribution.

The reachability graph of a SPN is isomorphic to the stochastic process ${M(t), t \geq 0}$

The state space S of the CTMC corresponds to the reachability set of the SPN, and it's obtained associating to every marking state $m_i$ a state $s_i$.

The transition rate from the state $s_i$ to the state $s_j$ is the sum of the rates of the transitions enabled in $m_i$ and whose firing generate $m_j$.

For analyzing the stochastic behavior of a SPN we should:

- obtain the reachability graph
- solve the corresponding CTMC
