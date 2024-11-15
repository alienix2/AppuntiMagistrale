# Markov chain

The **Markov chain** approach is a **state-based** and random processes approach. This allows to relax the assumptions of independence that we had with the previous models analyzed.

This means that the fail of a component can affect the fail of another component and also that restoration can cause other components to be "failed" for some time. This is a more realistic approach to model the behavior of a system.

## Random processes

A **random process** is a sequence of random variables indexed according to the time:
$$X = \{X(t) | t \in T\}$$
Each value of the random variable is a **state** of the system.

The state space is the set of all possible states of the system:
$$S = \{y:X(t) = y, t \in X\}$$

*Example:* I consider a stochastic process X which is obtained by considering the set or random variables $X(t)$ with $t = 1,2,\dots$ each defined as the minimum between the result of the toss of a dice and the value 4.

In this example: $S = \{1,2,3,4\}$, $X(1) = 1$, $X(2) = 3$, $X(3) = 4$, $X(4) = 2$, $X(5) = 4$, $X(6) = 4$, so $P(X(t) = 4) = \frac{1}{2}$

A random variable $yS is a function that maps the element from a space $\Omega$ to the real numbers:
$$Y: \Omega \rightarrow \mathbb{R}$$

A random process maps the element from a two-dimensional space to the real numbers:
$$X:T \times \Omega \rightarrow \mathbb{R}$$

Given a random variable $X$ we can describe it by using the **cumulative distribution function**: $F_x$

### Discrete and continuous random processes

**Time:**

- **Discrete time random process:** $|T|$ is finite or countable
- **Continuous time random process:** $|T|$ is uncountable

**Space:**

- **Discrete state random process:** $|S|$ is finite or countable
- **Continuous state random process:** $|S|$ is uncountable

*Note:* in the course only the first 3 of these will be analyzed

**Example of classification:**

|  | Continous states | Discrete states |
| --------------- | --------------- | --------------- |
| **Continous time** | generator's power at time t | number of sysem's failures until time t |
| **Discrete time** | queing time of the $t^{th}$ task | $t^{th}$ number of the Fibonacci sequence |

## Markov process and Markov chain

A **Markov process** is a random process informally defined as: give a state of a Markov process $X$ at the time t, the future behavior of X can be completely described by X(t).

A Markov process is **memory less** cause the future behavior of the process depends only on the current state and not on the past states.

A **Markov chain** is a Markov process with a discrete space state:

**DCMC (Discrete time, Countable state, Markov chain)**
**DTMC (Discrete time, Time state, Markov chain)**

### Formal definition

A **Discrete Time Markov Chain (DTMC)** is a sequence of random variables $X_0, X_1, X_2, \dots$ having a finite or countable state $S$ such that:

for each instant $t \in T$, and for every integer $k \geq 0$, and for each couple of states $i,j \in S$ and for each sequence of states $n_0,n_1,\dots,n_{t-1} \in S$:
$$P(X_{t+k} = j | X_t = i, X_{t-1} = n_{t-1}, \dots, X_0 = n_0) = P(X_{t+k} = j | X_t = i)$$

*Note:* The condition probability $P(X_{t+k} = j | X_t = i)$ is called the **transition probability** from state i to state j in k steps at time t.

#### Homogeneous Markov chain

A Markov chain is called **homogeneous** if the transition probability is independent of the time t:
$$P(X_{t+k} = j | X_t = i) = P(X_{k} = j | X_0 = i)=p_{ij}^{(k)} \forall t\geq 0$$

*Note:* this can also be interpreted as the probability of going from state i to state j in k steps. $p_{ij}^{(1)}$ is often referred as $p_{ij}$

*Note:* from now on we will assume to deal with homogeneous Markov chains and that the state-space is homogeneous.

### State occupancy probability vector

We consider $\pi$ a row vector and $\pi_i$ the $i_{th}$ element of the vector. we define the **state occupancy probability vector** at step k as $\pi(k)$ where: $\pi_i(k)$ is the probability that a DTMC is in state i at time-step k.
