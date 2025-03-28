# Stability

The definition of (Lyapunov) stability is the following:

> **Def:** $\bar{x}$ is stable if and only if $\forall \epsilon > 0$ $\exists \delta > 0$ such that $||x(0) - \bar{x}|| \leq \delta \Rightarrow ||x(t) - \bar{x} || \leq \epsilon \forall t \geq 0$.

And moreover:

- $\bar{x}$ is **asymptotically stable** if it is stable and $\lim_{t \to \infty} x(t) = \bar{x}$.
- Otherwise $\bar{x}$ is **unstable**.

*Note:* the same considerations can be done in discrete time.

*Example:* I consider the matrix:

$$A = \begin{bmatrix} -2 & -4 \\ 2 & 2 \end{bmatrix}\Rightarrow (\lambda I - A) = \begin{bmatrix} \lambda + 2 & 4 \\ -2 & \lambda - 2 \end{bmatrix}$$
$$\Rightarrow (\lambda + 2)(\lambda - 2) + 8 = 0 \Rightarrow \lambda^2 = 0 \Rightarrow \lambda_{1,2} = \pm 2j\sqrt{2}$$

## Lyapunov's direct method

$$\dot{x} = f(x(t)), f(0) = 0$$

Continuous, differentiable function $V: \mathbb{R}^n \to \mathbb{R}$ that satifies:

- $V(0) = 0$
- $V(x) > 0 \forall 0 < ||x|| \leq \delta$ for some $\delta > 0$

V is a **Lyapunov function** if:

- $\dot{V}(x(t)) \leq 0 \forall 0 < ||x|| \leq \delta$

**Theorem:** if there exists a Lyapunov function, then $\bar{x} = 0$ is a (locally) stable equilibrium. If, in addition, $\dot{V}(x(t)) < 0 \forall 0 < ||x|| \leq \delta$, then $\bar{x} = 0$ is an asymptotically stable equilibrium.

*Example:*
$$\dot{x} = \begin{bmatrix} -x_1 & -x_2 \\ x_1 & -x_2^3 \end{bmatrix}, \bar{x}=\begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

$$V(x) = x^T\begin{bmatrix} a & 0 \\ 0 & b \end{bmatrix}x$$

$$\dot{V}(x) = \frac{\partial V}{\partial x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}^T\begin{bmatrix} a & 0 \\ 0 & b \end{bmatrix}\begin{bmatrix} -x_1 & -x_2 \\ x_1 & -3x_2^2 \end{bmatrix} = 2[-ax_1^2 - bx_2^4 +x_1x_2(b-a)] < 0$$

And example of a solution is:

$$a = b = 1 \Rightarrow 2(-x_1^2 - x_2^4) < 0 \Rightarrow \bar{x}$$

So the system is GAS.

**Other example:**

$$\dot{x} = \begin{bmatrix} (x_1-x_2)(x_1^2+x_2^2-1) \\ (x_1+x_2)(x_1^2+x_2^2-1) \end{bmatrix}$$

$$V(x) = x^T \begin{bmatrix} a & 0 \\ 0 & b \end{bmatrix}x$$

$$\bar{x}:f(\bar{x}) = 0 \Rightarrow \bar{x} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

$$\begin{cases} (x_1-x_2)(x_1^2+x_2^2-1) = 0 \\ (x_1+x_2)(x_1^2+x_2^2-1) = 0 \end{cases}$$

I need to find a value for $a$ and $b$ such that $\dot{V}(x) < 0$.

$$\dot{V}(x) = 2[2x_1^2 + bx_2^2 + x_1x_2(b-a)](x_1^2+x_2^2-1)< 0, a,b > 0$$
$$\Rightarrow x_1+ x_2^2 -1 < 0, a=b=\frac{1}{2}$$
