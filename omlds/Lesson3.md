# Stability of LTI systems (Lyapunov's indirect method) and Reachability

## Stability of LTI systems

**Natural response:** $x(t) = e^{At}x(0)$ (depends on A only) we talk about **system stability** for LTI systems

> **Theorem**: let $\lambda1 \cdots \lambda_r, r \leq n$ eigenvalues of A. The system $\cdot(x) = Ax$ is:
>
> - **asymptotically stable** if and only if $\Re(\lambda_i) < 0 \forall i = 1 \cdots r$
> - **unstable** if and only if $\Re(\lambda_i) > 0$ for at least one $i = 1 \cdots r$
> - **marginally stable** if and only if $\Re(\lambda_i) \leq 0$ for all $i = 1 \cdots r$ and for those h so that $\Re(\lambda_h) = 0 it holds that $\mu_a(\lambda_h) = \mu_g(\lambda_h)$

*Note*: if A diagonalizable all the ifs are iff.

*Example:*

$$\cdot(x) = \begin{bmatrix} -x_1 - x_2 \\ x_1 - x_2^3 \end{bmatrix} \Rightarrow \begin{cases} -\lambda_1 - \lambda_2 = -\lambda \\ \lambda_1 - \lambda_2^3 = -\lambda \end{cases} \Rightarrow \lambda^2 = 0 \Rightarrow \lambda_{1,2} = 0$$
$$A = \frac{\partial f}{\partial x} = \begin{bmatrix} -1 & -1 \\ 1 & -3x_2^2 \end{bmatrix} = \begin{bmatrix} -1 & -1 \\ 1 & 0 \end{bmatrix}$$

$$det(\lambda I - A) = \begin{vmatrix} \lambda + 1 & 1 \\ -1 & \lambda \end{vmatrix} = \lambda^2 + \lambda + 1 = 0 \Rightarrow \lambda_{1,2} = \frac{-1 \pm j\sqrt{3}}{2}$$

The real part is negative so the system is locally asymptotically stable.

## Reachability

> **Definition**: a system is said to be **reachable** if for any initial state $x(0)$ there exists a finite time $T$ such that $x(T) = 0$.

How can I determine a sequence of inputs given $x_1, x_2 and T=n$?

$$x_2 - A^nx_1 = [B AB, \cdots, A^{n-1}B]u \begin{bmatrix} u(n-1) \\ u(n-2) \\ \cdots \\ u(0) \end{bmatrix}$$
I solve $X = RU$ for $U$.

R is called **reachability matrix**, by **rouche-capelli** theorem it is full rank if and only if the system is reachable if and only if $Im(R) = \mathbb{R}^n$.

**Proof**:  
$(\Rightarrow)$I assume that $(A,B)$ is reachable,  
$\begin{cases} x_1 = 0 \\ x_2 = \bar{x} \end{cases} \Rightarrow \exists T, u(T-1), \cdots, u(0)$

$\bar{x} = \sum_{i=0}^{T-1}A^iBu(T-1-i) = \begin{bmatrix} B & AB & \cdots & A^{T-1}B \end{bmatrix} \begin{bmatrix} u(T-1) \\ \cdots \\ u(0) \end{bmatrix}$

We have two cases:

1. $T > n$, by Cayley-Hamilton theorem $x \in Im(R)$
2. $T < n$, $x \in Im(R_T) \subset Im(R)$

$(\Leftarrow)$ I assume that $Rank(R) = n$  
$$ \Rightarrow Im(R) = \mathbb{R}^n \Rightarrow X = RU \Rightarrow \exists u(T-1), \cdots, u(0) \Rightarrow \exists T$$

*Note:* $Im(R)$ is the set of states that are reachable from the origin. A system is completly reachable $Im(R) = R^n$ iff all states are reachable from the origin in n steps.

### Reachability in CT systems

The definition is almost the same:

$$\cdot(x) = Ax + Bu \Rightarrow x(t) = e^{At}x(0) + \int_0^t e^{A(t-\tau)}Bu(\tau)d\tau$$

### Controllability

What we would like to have in order to have controllability is to have an output of $x(k)$, which represents the state of the system at time $k$, and an input $u(k)$, which represents the input at time $k$.

In real life we usually cannot get $x(k)$ and therefore we must rely on another state called $y(k)$ which are measurement that (practically) represent the system and then we try to approximate the $x(k)$ using that value.

### Observability

We consider:

$$\begin{cases} x(k+1) = Ax(k) + Bu(k) \\ y(k) = Cx(k) \end{cases}$$

For a given $x(0) = x_0, T \in \mathbb{N}$ and an input sequence $u(0), \cdots, u(T-1)$, if we consider $y(T, u) = Cx(T, u)$, we can say that the system is observable if for any $x_0$ and $T$ there exists a unique input sequence $u(0)$.

Two state are called **indistinguishable** if they have the same output for any input sequence.

Formally (ToDo):

Considering $y(T, x_0, u(.)) = CA^Tx_0 + \sum_{i=0}^{T-1}CA^{T-1-i}Bu(i)$, we can say that two states are indistinguishable if $y(T, x_0, u(.)) = y(T, x_0', u(.)) \forall u(.)$.

If we fix $T = n$, if we consider $u(0), \cdots, u(n-1)$, we can reconstruct $x_0$ in this way:

$$\begin{bmatrix} y(0) \\ y(1) - CBu(0) \\ \cdots \\ y(n-1) - \sum_{i=0}^{n-2}CA^{n-1-i}Bu(i) \end{bmatrix} = \begin{bmatrix} C \\ CA \\ \cdots \\ CA^{n-1} \end{bmatrix}x_0$$

$$ \Rightarrow \text{i can solve } Y = \Theta x_0$$

$\Theta$ is called **observability matrix** and the system is observable if and only if $Y = \Theta x_0$ if and only if $rank(Y) = rank(\Theta Y)$.

**Proof**:  
$(\Rightarrow)$ I assume that the system (A,B,C) is observable,  
FTSOC I assume that $rank(\Theta) < n$  
$\Rightarrow \exists x_0 \neq 0$ such that $\Theta x_0 = 0 \Rightarrow \begin{bmatrix} C \\ CA \\ \cdots \\ CA^{n-1} \end{bmatrix}x = 0$
$Cx = CAx = \cdots = CA^{n-1}x = 0$

By Cayley-Hamilton theorem $CA^Tx = 0, \forall T \geq n-1 \Rightarrow x \text{ is indistinguishable from } 0$ and this is a contradiction.

$(\Leftarrow)$ I assume that $rank(\Theta) = n$  
FTSOC $\Rightarrow \exist x_1 \neq x_2 \Rightarrow CA^Tx_1 = CA^Tx_2 \Rightarrow CA^T(x_1 - x_2) = 0 \Rightarrow C\tilde{x} = CA\tilde{x} = \cdots = CA^{n-1}\tilde{x} = 0$

We picked $T = n$ as this should hold for all the T and we have a contradiction.

*Example:*

I consider a fully observable system:

$$\begin{bmatrix} A = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix} & C = \begin{bmatrix} 1 & 0 & 0 \end{bmatrix} \end{bmatrix}$$

$$\Theta = \begin{bmatrix} C \\ CA \\ CA^2 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

Since the rank of $\Theta$ is 3, the system is fully observable.

What would happen if I consider: $C = \begin{bmatrix} 0 & 0 & 1 \end{bmatrix}$?

$$\Theta = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$
