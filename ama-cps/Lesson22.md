# More on PNs

Two types of analysis can be performed on PNs:

- **Qualitative analysis**: this is the analysis performed to verify the properties of the PN, such as liveness, boundedness, and reachability. This type of analysis is performed using the reachability tree, the state space, and the incidence matrix of the PN.
- **Quantitative analysis**: this is the analysis performed to determine the performance of the PN, such as the average time taken to complete a task, the average number of tokens in the system, and the average number of transitions executed in a given time. This type of analysis is performed using the incidence matrix and the state space of the PN.

Moreover there are two kinds of quantitative analysis:

- **Analytical evaluation**: this is the evaluation performed using mathematical equations to determine the performance of the PN.
- **Simulative evaluation**: this is the evaluation performed using simulation tools to determine the performance of the PN.

## Quantitative analysis

The PNs can be evaluated considering the duration of time interval, in particular:

- **cumulative analysis**: evaluated over a period of time
- **immediate analysis**: evaluated in an instance of time

In particular they are referred as:

- **steady-state analysis**: the analysis is performed in an instant of time or in an interval of time that **tends to infinity**
- **transient analysis**: the analysis is performed in an instant of time or in an interval of time that is **finite**

### Steady-state analysis

This kind of analysis is possible if:

- the model converges to stable state as time tends to infinity
- the measure of interest exists

A model converges to a **steady-state** (for t $\to$ $\infty$) when it's possible to find the limit of the state occupancy probability distribution when time tends to infinity

The SPN converges at the steady-state if the underlying CTMC is argodic.

## Measure of interest and performance indices

There are many ways to measure the performance of a PN, we will see into details the **reward variables**

### Reward variables

The reward variables are a way of measuring the performance on dependability characteristics of a model like:

- Expected time until service
- System availability
- Number of misrouted packets
- etc.

#### Reward structure

A reward structure is used to build the reward variables. In particular we have that a reward structure consists of two parts:

- **Impuls reward**: defined on activities. This accumulates reward when the activity fires
- **rate reward**: defined on the number of tokens in places. This accumulates reward when the model is in certain states.

#### Reward variables

A reward variable is the sum of the impulse and the rate reward structures over a certain time.

Considering $[t, t + l]$ to be the interval of time defined for a reward variable then:

- if l = 0 then the reward variable is an **instant-of-time** reward variable
- if l > 0 then the reward variable is a **interval of time** reward variable
- if l > 0 then dividing an interval of time reward variable by l we obtain a **time-averages interval of time** reward variable

A reward structures is composed of two functions:

- $R : RS \to \mathbb{R}$ **rate reward**
- $C : \Tau \to \mathbb{R}$ **impulse reward**

The reward variable **V_t** is defined as:

$$V_t = \sum_{m \in RS} R(m) l^m_t + \sum_{a \in \Tau} C(a) l^a_t$$

Where $I^m_t$ and $I^a_t$ are variables defined as:

$$l^m_t = \begin{cases} 1 & \text{if M(t) = m} \\ 0 & \text{otherwise} \end{cases}$$

$$l^a_t = \begin{cases} 1 & \text{if a is the most recently fired transition at time t} \\ 0 & \text{otherwise} \end{cases}$$

Which means that:

$$E[V_t] = \sum_{m \in RS} R(m) P(M(t) = m) + \sum_{a \in \Tau} C(a) P(A(t) = a)$$

The distribution of the two functions can converge for t $\to$ $\infty$. In that case we have that:

$$V_{t \to \infty} = lim_{t \to \infty} V_t = \sum_{m \in RS} R(m) lim_{t \to \infty} l^m_t + \sum_{a \in \Tau} C(a) lim_{t \to \infty} l^a_t$$

The random variable $T_{[t, t + l]}$ is the time spent in the interval $[t, t + l]$ and is defined as:

$$Y_{[t, t + l]} = \sum_{m \in RS} R(m) J^m_{[t, t + l]} + \sum_{a \in \Tau} C(a) N^a_{[t, t + l]}$$

Where $J^m_{[t, t + l]}$ and $N^a_{[t, t + l]}$ are defined as:

- $J^m_{[t, t + l]}$ is the total time spent by the preocess in m in the time interval [t, t + l]
- $N^a_{[t, t + l]}$ is the number of firings of a in the time interval [t, t + l]

Same as before we can pass to the limits for t and l.

For the **time-averages interval of time** reward variable we have that:

$$W_{[t, t + l]} = \frac{Y_{[t, t + l]}}{l}$$
$$W_{t \to \infty} = lim_{l \to \infty} W_{[t, t + l]} = lim_{l \to \infty} \frac{Y_{[t, t + l]}}{l}$$
$$W_{l \to \infty} = lim_{l \to \infty} W_{[t, t + l]} = lim_{l \to \infty} \frac{Y_{[t, t + l]}}{l}$$

**Objective**: definition of function $R: RS \to \mathbb{R}$, this can be done by using the definition of k couples **predicate-function** $(P_i, R_i), i = 1, \dots k$

Each predicate $P_i$ identifies a disjoint set of markings $RS_i$ and each function $R_i$ associates to each marking of the partition $RS_i$ a real number.

A **predicate** is a function $P_i: RS \to \{0, 1\}$ that associates to each marking a boolean value.  
$RS_i = \{m \in RS | P_i(m) = 1\}$ and $\bigcap_{i = 1}^k RS_i = \empty$

The **function** $R_i: RS_i \to \mathbb{R}$ associates to each marking of the partition $RS_i$ a real number.

The **rate reward** function associates to each marking that satisfies the predicate a rate reward:

$$R(m) = \begin{cases} R_1(m) & \text{if } P_1(m) = 1 \\ ...\\ R_k(m) & \text{if m satisfies} P_k\end{cases}$$

For the **impulse reward** we can simply assign a real number to each transition. If the transition has no number assigned then it's value will be zero.
