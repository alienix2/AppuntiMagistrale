# More on descrete Markov chains

## Transition probability matrix

We can compute the probability of going from state i to state j in k steps by using the **transition probability matrix** $P^{(k)}$ where:

![](../Screenshots/transition_probability_matrix.png)

## Transient behavior of a DTMC

If we want to evaluate the probability of finding the DTMV in state j at the step k we can procede as follows:

- we compute the $\pi_j(1)$ which is the probability of being in state j at step 1
- we realize that in order to calculate the $\pi_j(k)$ we need to know the $\pi_j(k-1)$
- $\pi_j(k) = \sum_{i=1}^{n} \pi_i(0) \cdot p_{ij}^{(k)}$

*Note:* in general $\pi(1) = \pi(0) \cdot P$, and $\pi(k) = \pi(0) * p^k$

*Example:* weather forecast

I consider the transition rate matrix:

$$P = \begin{bmatrix} 0.80 & 0.15 & 0.05 \\ 0.38 & 0.60 & 0.02 \\ 0.75 & 0.05 & 0.20 \end{bmatrix}$$

I want to know all the probabilities of the weather in 3 days.

I start with the graph:

![sunny_rainy_snowy](../Screenshots/sunny_rainy_snowy.png)

From this I can calculate the probability of the weather in 3 days and also I can estimate which condition is most likely than the other in each day.

*Note:* I always need the initial state to calculate the probabilities in the future.

## Holding time in a state

The **holding time** in a state is the number of steps that the DTMC stays in a state before moving to another state.
The statistical properties still hold:

$$P(T_i = k) = (1-p_{ii})\cdot p_{ii}^{k-1}$$

### Time-limiting behavior

The **time-limiting behavior** corresponds to a **steady-state** behavior. This is the behavior of the system when the time goes to infinity. We want to compute:
$$\lim_{k \to \infty} \pi(k) = \pi_{\infty} | \lim_{k \to \infty} \pi(0)P^k$$

We need to check if this limit exists and if it does we can compute it by using the **eigenvector** of the transition probability matrix.

### Some definitions

We say that j is an **accessible** if there exists a k such that $p_{ij}^{(k)} > 0$.

Two states i and j are **communicating** if i is accessible from j and j is accessible from i.

An MC is called **irreducible** if all the states are communicating. Otherwise, it is called **reducible**.

A state is called **absorbing** if it is impossible to leave it (i.e. $p_{ii} = 1$).

*Note:* an irreducible MC cannot have absorbing states.

We define the **recurrence time** of state i in k steps as the probability of returning to the state i for the first time in k steps. We call it $f_{ii}(k)$

We define as $f_i$ with $i \in {1,2,\dots,n}$ the probability of returning to the state i for the first time in any number of steps.

A state i is called **transient** if $f_i < 1$ and **recurrent** if $f_i = 1$.

When we consider a **recurring state** we are interested in knowing how many steps in takes in average to go back to state i. To do that we can compute the **average recurrence time:**
$$m_i = \sum_{k=1}^{\infty} k \cdot f_{ii}(k)$$

i is called **null recurrent** if $m_i = \infty$ and **positive recurrent** if $m_i < \infty$.

#### Periodicity

A state i is called **periodic** if there exists a number d > 1 such that $p_{ii}^{(k)} > 0$ only if k is a multiple of d. Otherwise, it is called **aperiodic**.

A MC is called **ergodic** if it is irreducible, aperiodic and positive recurrent.

*Note:* if we consider a finite state space, then we only need the MC to be irreducible and aperiodic to be ergodic.

### Existence of the limit

It's easy to find cases in which the limit does not exists.

We can write another limit which always exists **for an irruptible MC**:

$$\lim_{n \to \infty}\sum_{i=1}^{n} \frac{\sum_{i=1}^{n}\pi_i(i)}{n}$$

In **ergotic DTMC** we can write that $\pi = \pi \cdot P$ with the constraint $\sum_{i=1}^{n}\pi_i = 1$.

### Flow equations

The **flow equations** tell us tat the **incoming** probability mass in the state i must be equal to the **outgoing** probability mass in the same state:
$$\sum_{j=1}^{n} \pi_j \cdot p_{ji} = \sum_{j=1}^{n} \pi_i \cdot p_{ij}$$

*Note:* in matrix form we have $\pi \cdot P = \pi$

## Continous-time Markov chains

A continuous-time Markov chain is a stochastic process that has the Markov property and the state space is continuous.

*Note:* many of the properties from the discrete domain can be translated into the continuous domain.

$$P(X(t + \tau) = j | X(t) = i) = p_{ij}(\tau)$$

This is the **memoryless property** in the continuous domain for **stationary** Markov chains.

### CTMC and exponential random variables

A CTMC is described by:

- an initial vector $\pi(0)$
- a transition probability matrix P(t) = $[p_{ij}(t)]$

### Competition between two variables

Given two independent variables A and B we can say that the probability of A being greater than B is:
$$P[A<B] = \frac{\alpha}{(\alpha + \beta)}$$

### State transition-rate matrix

The **state transition-rate matrix** is a matrix that contains the rate of going from state i to state j. An homogeneous CTMC can be completly described by:

- the initial distribution $\pi(0)$
- the state transition-rate matrix Q, which is also called the **infinitesimal generator** matrix, defined as:
$$ q_{ij} = \begin{cases} -\sum_{j \neq i} q_{ij} & \text{if } i = j \\ p_{ij} & \text{if } i \neq j \end{cases}$$
