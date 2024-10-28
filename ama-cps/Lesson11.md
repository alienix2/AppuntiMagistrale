# Probabilities

## Model

A Model is an abstraction of a system. It's a projection of a real system (abstraction) and only contains details that are useful for evaluation purposes. *I.e:* I consider a system and I say that it's working or not working, that's a big abstraction cause there might be multiple parts working or failing.

### Probabilistic model

We consider probabilistic models cause in our case the possibility that the system fails is random, it's not deterministic.

#### Definitions

- A **probabilistic model** (or **stochastic model**) is a model that is based on random variables. It's made out of a list of possible outcomes with their assigned probability of happening.
- A **Random experiment** is an experiment that can have multiple **outcomes,** each with a certain probability of happening. *I.e:* the tossing of a coin.  
- A **trial** is a single execution of a random experiment.
- A **sample space** is the set of all possible outcomes of a random experiment. *I.e:* the sample space of a coin toss is {H, T}.
- An **event** is a subset of the sample space. *I.e:* the event of getting a head is {H}.

### Algebra of events

We consider a sample space S and two events A and B $\subseteq$ S. We can define the following operations:

- **Union** of A and B: $A \cup B = \{x \in S | x \in A \lor x \in B\}$
- **Intersection** of A and B: $A \cap B = \{x \in S | x \in A \land x \in B\}$
- **Complement** of A: $\bar{A} = \{x \in S | x \notin A\}$

We can also give the definition of:

- **Cardinality** of a set A: $|A| = \text{number of elements in A}$
- **Mutually exclusive events**: A and B are mutually exclusive if $A \cap B = \emptyset$
- **Partition of S**: A set of events $A_1, A_2, ..., A_n$ is a partition of S if $A_i \cap A_j = \emptyset$ for $i \neq j$ and $\bigcup_{i=1}^{n} A_i = S$

### Probability

The probability of an event A is a number between 0 and 1 that represents the likelihood of A happening. We denote it as $P(A)$. Given a sample space or random experiments and A an event in that sample space we consider:

- **Probability function:** $P: 2^S \rightarrow [0, 1]$
  - **Axioms of probability:**
    1. $P(A) \geq 0$ for all A
    2. $P(S) = 1$
    3. If $A_1, A_2, ...$ are mutually exclusive events, then $P(\bigcup_{i=1}^{\infty} A_i) = \sum_{i=1}^{\infty} P(A_i)$

The **conditional probability** of A given B is the probability of A happening given that B has happened. We denote it as $P(A|B)$. We can define it as:
$P(A|B) = \frac{P(A \cap B)}{P(B)}$, with $P(B) > 0$

Two events are **Independent** if $P(A \cap B) = P(A) \cdot P(B)$

*Example:* casting a dice, we have event A: get number 4 and event B: get an even number.
$P(A) = \frac{1}{6}$, $P(B) = \frac{3}{6}$, $P(A|B) = \frac{1}{3}$, $P(A \cap B) = \frac{1}{6}$, $P(B|A) = \frac{P(A \cap B)}{P(A)} = \frac{1/6}{1/6} = 1$

## Reliability of parallel and series systems

We consider a system composed of n components. We consider that the system has a series of events happening, $A_1, ..., A_n$ where $A_i$ event means that component i is working properly. We define the **Component reliability** of the component i as the probability that the component i is working correctly.

**Components in series:** the system works if all the components work. The probability of the system working is $P(A_1 \cap ... \cap A_n) = \prod_{i=1}^{n} P(A_i)$

**Components in parallel:** the system works if at least one component works. The probability of the system working is $P(A_1 \cup ... \cup A_n) = 1 - P(\bar{A_1} \cap ... \cap \bar{A_n}) = 1 - \prod_{i=1}^{n} (1 - P(A_i)) = 1 - \prod_{i=1}{n} (1-R_i)$

## Discrete random variables

A **random variable** is a function that assigns a real number to each outcome of a random experiment ($X: S \rightarrow \R$).

*Example:* casting a dice, we define X as the random variable that assigns to each outcome the number of the dice. We have $p_X(1) = \frac{1}{6}$, $p_X(2) = \frac{1}{6}$, $p_X(3) = \frac{1}{6}$, $p_X(4) = \frac{1}{6}$, $p_X(5) = \frac{1}{6}$, $p_X(6) = \frac{1}{6}$

A **discrete random variable** is a random variable that can take a finite number of values (so the sample space is finite or numerable). We define the **expected value** of a discrete random variable X as $E[X] = \sum_{x \in \text{range}(X)} x \cdot p_X(x)$

Given a discrete random variable X, we define the **Probability mass function** as $p_X(x) = P(X = x)$, with $x \in \text{range}(X)$. That is the probability that the value of X associated with a result is equal to x. $p_x(x) = P(X = x) = \sum_{X(s) = x} P(s)$

*Example:* $X = (x mod 2)$, $p_X(0) = \frac{1}{6} + \frac{1}{6} + \frac{1}{6} = \frac{1}{2}$, $p_X(1) = \frac{1}{2}$

A **Cumulative distribution function** is a function that gives the probability that a random variable X is less than or equal to a certain value x. We define it as $F_X(x) = P(X \leq x) = \sum_{y \leq x} p_X(y)$.

### Bernoulli distribution

A **Bernoulli trial** is a random experiment with two possible outcomes: success (1) and failure (0). The probability of success is p and the probability of failure is 1-p. We define the **Bernoulli distribution** as the probability distribution of a random variable X that takes value 1 with probability p and value 0 with probability 1-p. We denote it as $X \sim \text{Bernoulli}(p)$.

If we consider a sequence of n Bernoulli trials, and we count the number of trials before the first success we get:

- **Geometric distribution:** the probability that the first success occurs at trial k is $P(X = k) = (1-p)^{k-1} \cdot p$. $F_Z(k) = 1 - (1-p)^k$

The geometric distribution has the property of being **memoryless**, that is, the probability of the first success occurring at trial k does not depend on the number of failures that have occurred before k.

*Note:* this is the **ONLY** distribution that is memoryless.

#### Markov property

A random variable X has the Markov property if the probability of the next state only depends on the current state. That is, $P(X_{n+1} = x_{n+1} | X_0 = x_0, ..., X_n = x_n) = P(X_{n+1} = x_{n+1} | X_n = x_n)$

Intuitively, let's consider a geometric random variable Z that represents the number of trials before the first success. The probability of the first success occurring at trial k does not depend on the number of failures that have occurred before k. That is, $P(Z = k | Z > n) = P(Z = k)$.

*Note:* if a discrete random variable has the Markov property, then it has the memoryless property and has a geometric distribution.

*Note:* there are many other discrete random variables, like **Binomial**, **Poisson**, **Hypergeometric**, **Negative Binomial**, **Uniform**, **Exponential**, **Normal**, etc. Each has it's use case but we will not analyze them in detail right now cause you can pick the best one depending on the use case reading at the existing literature.

## Continuous random variables

A **continuous random variable** is a random variable that can take any value in a certain interval.

We define the **probability density function** as a function that assigns a probability to each value in the interval. We denote it as $f_X(x)$. The probability that X is in the interval [a, b] is given by $\int_{a}^{b} f_X(x) dx$.

A **cumulative distribution function** is a function that gives the probability that a random variable X is less than or equal to a certain value x. We define it as $F_X(x) = P(X \leq x) = \int_{-\infty}^{x} f_X(t) dt$.

### Exponential distribution

The **Exponential distribution** is the probability distribution of the time between events in a Poisson process. It's defined by a single parameter $\lambda > 0$ that represents the **rate** of events. We denote it as $X \sim \text{Exp}(\lambda)$.

$F_X(x) = 1 - e^{-\lambda x}$, $f_X(x) = \lambda e^{-\lambda x}$ for $x \geq 0$ or $0$ otherwise.

The exponential distribution is used for modeling events such as:

- the time between two successive jobs in a computing center
- the service time of a server in a network of queues
- the time to failure of a component in a system
- the time required to repair a failed component in a system

The exponential distribution is the only continuous distribution that has the memoryless property. That is, $P(X > s + t | X > s) = P(X > t)$

*Note:* this means that the probability of the time to failure of a component in a system is independent of the time that the component has been working. This assumption might not be true cause we are basically a component which is not **aging** and that's obviously not adherent to reality. This also means that if the component fails we are giving as a fact that it wasn't because of the age.

### Minimum of exponential random variables

Let $A, B$ be two independent exponential random variables with rates $\lambda_A, \lambda_B$. We define $C = \min(A, B)$. The probability density function of C is $f_C(x) = \lambda_A e^{-\lambda_A x} + \lambda_B e^{-\lambda_B x}$ for $x \geq 0$ or $0$ otherwise. $F_X(t) = 1 - e^{-(\lambda_A + \lambda_B) t}$

If we want to calculate the probability that the first event occurs before the second event, we have to calculate $P(A < B) = \int_{0}^{\infty} \int_{0}^{x} f_{A, B}(x, y) dy dx = \int_{0}^{\infty} \lambda_A e^{-\lambda_A x} (1 - e^{-\lambda_B x}) dx = \frac{\lambda_A}{\lambda_A + \lambda_B}$

#### Reliability

Applying the above to the concept of reliability, we can say that the reliability of a component in the system is the probability that it survives until time t. $R_X(t) = P(X > t) = 1 - F_X(t)$

#### Instantaneous failure rate

The instantaneous failure rate is the probability that a component fails at time t given that it has survived until time t. We denote it as $\lambda_X(t) = \frac{f_X(t)}{R_X(t)}$. If we consider the exponential distribution we realize that actually $\lambda_x(x) = L$ where L is constant.

*Note:* as per the discrete case, there are many other continuous random variables, like **Uniform**, **Normal**, **Gamma**, **Beta**, **Weibull**, etc. And each has it's use case.

## Mean Mode, Median and Moments

**Median:** the median of a random variable X is the value that divides the distribution into two equal parts. That is: $P(X<x) = \frac{1}{2}$ and $P(X>x) = \frac{1}{2}$
**Mode:** the mode of a random variable X is the value that appears most frequently in the distribution. That is, $f_X(m) = \max f_X(x)$
**Mean:** the mean of a random variable X is the expected value of X. That is, $E[X] = \int_{-\infty}^{\infty} x f_X(x) dx$ in **continuous** or $E[X] = \sum_{x \in \text{range}(X)} x p_X(x)$ in **discrete**

### Mean of exponential

The mean of an exponential random variable X is $E[X] = \frac{1}{\lambda}$ which is exactly the inverse of the rate $\lambda$. The **expected lifetime** of **Mean time to failure** is $\frac{1}{\lambda}$
