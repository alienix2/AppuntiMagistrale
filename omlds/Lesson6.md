# Linear observer and dynamic compensator

Starting from the last lecture we will try to analyze what happens if the state measurement aren't available.

## Linear observer

The basic problem is that we have a **dynamical system** characterized by the matrices $A, B, C$, we have a $y(k)$ that is some kind of combination of the three matrices but we don't have $x(k)$ (dependent only on $A,B$ that is what we usually need to create a controller.

As we saw in the previous lecture we can also use $u(k)$ which we have as the information from before entering the dynamical system to close the loop.

We want to create what is called a **dynamic compensator**

We consider $? = (A, B)$ and we have:

$$\begin{cases} x(k+1) = Ax(k) + Bu(k) \\ x(k+1) = A\hat{x}(k) + Bu(k) \end{cases}$$

Where $\hat{x}(k)$ is the estimate of the state.

From this description we can also estimate the error:

$$e(k) = x(k) - \hat{x}(k), e(k+1) = x(k+1) - \hat{x}(k+1) = Ae(k) \Rightarrow$$
$$e(k) = A^k(x(0) - \hat{x}(0))$$

Ideally we would like to have $e(k) \rightarrow 0$ pretty fast. However we should note that:

1. $e^k = A^k(x(0) - \hat{x}(0))$ depends on A which is not modifiable
2. $e(k) \rightarrow 0$ asimptotically (iff $eig(A) \in \mathbb{B}_1$)

*Note:* we are not using $y(k)$ yet.

We can integrate a feedback matrix using $y(k)$:

$$\hat{x}(k+1) = A\hat{x}(k) + Bu(k) + L(y(k) - C\hat{y}(k))$$

Where $L \in \mathbb{R}^{n \times l}$ is the **observer gain**.

If we express the $y(k)$ we get:

$$\hat{y}(k) = C\hat{x}(k), y(k) = Cx(k) \Rightarrow$$
$$\hat{x}(k+1) = A\hat{x}(k) + Bu(k) + LC(x(k) - C\hat{x}(k))$$

If we consider that $e(k) = x(k) - \hat{x}(k)$ we can rewrite the equation as:

$$e(k+1) = Ax(k) + Bu(k) - A\hat{x}(k) - Bu(k) -LCe(k) = (A - LC)e(k) \Rightarrow$$
$$e(k) = (A - LC)^k(x(0) - \hat{x}(0))$$

*Note:* in CT we have that $e(t) = e^{(A-LC)t}e(0)$

**Theorem:** Given $(A,C)$ observable, then $eig(A-LC)$ can be placed arbitrarily.

*Note:* this is very similar to what we got for the reachable systems

*Example:*

$$\begin{cases}\cdot{x}(t) = \begin{bmatrix} -1 & 0 \\ 1 & -1 \end{bmatrix}x(t) + \begin{bmatrix} 2 \\ 0 \end{bmatrix}u(t) \\
y(t) = \begin{bmatrix} 0 & \frac{1}{2} \end{bmatrix}x(t) \end{cases}$$

$$u = \begin{bmatrix} C \\ CA \end{bmatrix} = \begin{bmatrix} 0 & \frac{1}{2} \\ \frac{1}{2} & -\frac{1}{2} \end{bmatrix}$$

$$\dot{e}(t) = \dot{x} - \dot{\hat{x}} = (A-LC)e(t)$$

I get two solutions: $\lambda_12 = -4$ from which we get $P_d(\lambda) = (\lambda + 4)^2$

I consider $L \in \mathbb{R}^{n \times l}$ with $n = 2, l = 1$ and I get: $L = \begin{bmatrix} l_1 \\ l_2 \end{bmatrix}$

$$A - LC = \begin{bmatrix} -1 & 0 \\ 1 & -1 \end{bmatrix} - \begin{bmatrix} l_1 \\ l_2 \end{bmatrix}\begin{bmatrix} 0 & \frac{1}{2} \end{bmatrix} = \begin{bmatrix} -1 & 0 \\ 1 & -1 \end{bmatrix} - \begin{bmatrix} 0 & \frac{l_1}{2} \\ 0 & \frac{l_2}{2} \end{bmatrix} = \begin{bmatrix} -1 & -\frac{l_1}{2} \\ 1 & -1 - \frac{l_2}{2} \end{bmatrix}$$

To calculate the characteristic polynomial I must compute:

$$P_{A - LC}(\lambda) = det(\lambda I - (A - LC)) = det\begin{bmatrix} \lambda + 1 & \frac{l_1}{2} \\ -1 & \lambda + 1 + \frac{l_2}{2} \end{bmatrix} =$$
$$= (\lambda + 1)(\lambda + 1 + \frac{l_2}{2}) + \frac{l_1}{2} = \lambda^2 + \lambda + \lambda\frac{l_2}{2} + \lambda + 1 + \frac{l_2}{2} + \frac{l_1}{2} = \lambda^2 + 2\lambda + 1 + \frac{l_1 + l_2}{2}$$

$$P_{A - LC}(\lambda) = P_d(\lambda) = (\lambda + 4)^2$$

From this we get:

$$\begin{cases} 2 + \frac{l_2}{2} = 8 \\ 1 + \frac{l_1 + l_2}{2} = 16 \end{cases} \Rightarrow \begin{cases} l_2 = 12 \\ l_1 = 18 \end{cases}$$

$$\dot{\hat{x}} = A\hat{x} + Bu + LC(x(t) - \hat{x}(t)) =$$
$$= (A - LC)\hat{x}(t) + Bu(t) + Ly(t)$$

So we get that $\hat{y}(t) \rightarrow y(t)$

**Theorem:** SISO LTI system is observable iff for any target set of eigenvalues ${\lambda_1, \lambda_2, \dots, \lambda_n}$, $\exists 1 ! L \in \mathbb{R}^{n \times l}$ such that $eig(A - LC) = \{\lambda_1, \lambda_2, \dots, \lambda_n\}$

*Note:* if the system is unobservable we have that $rank(\Theta) = n_0 < n \Rightarrow n - n_0$, the eigenvalues can't be assigned arbitrarily. We can distinguish some cases:

- The system is observable $\Rightarrow$ a solution exists
- The system is unobservable $\Rightarrow$ then if the eigenvalues of the unobservable part have negative real part then the system is **detectable** and therefore $\exists$ a solution, otherwise not.

## Dynamic compensator

Combining what we saw in the last lecture with what we saw in this one we can get a way to design a **state feedback controller**.

We want to know if we are actually yielding the desired closed-loop performances. Moreover we are also trying to understand if what we do actually destabilizes the original system.

Assuming a completely reachable and observable open-loop system we get a Luenberger observer:

$$\dot{x}(k+1) = Ax(k) + Bu(k) + L(y(k) - C\hat{x}(k))$$

I set $u(k) = Kx(k) + v(k)$ and I get:

$$\begin{cases} x(k+1) = Ax(k) + Bu(k) \\ e(k+1) = A\hat{x}(k) + Bu(k) + L(y(k) - C\hat{x}(k)) \\ u(k) = K\hat{x}(k) + v(k) \\ y(k) = Cx(k) \end{cases}$$

Solving this we get:

$$x(k+1) = Ax(k) + Bu(k), e(k+1) = x(k+1) - \hat{x}(k+1) =$$
$$=Ax(k) + Bu(k) - A\hat{x}(k) - Bu(k) - L(y(k) - C\hat{x}(k)) =$$

$$u(k) = K\hat{x}(k) + v(k)$$
$$y(k) = Cx(k)$$

What we get in the end is:

$$\begin{cases} \begin{bmatrix} x(k+1) \\ e(k+1) \end{bmatrix} = \begin{bmatrix} A + BK & -BK \\ 0 & A - LC \end{bmatrix}\begin{bmatrix} x(k) \\ e(k) \end{bmatrix} + \begin{bmatrix} B \\ 0 \end{bmatrix}v(k) \\ y(k) = \begin{bmatrix} C & 0 \end{bmatrix}\begin{bmatrix} x(k) \\ e(k) \end{bmatrix} \end{cases}$$

What we can see by inspecting the matrix that the K is only influencing the first row of the matrix and therefore:

$$x(k+1) = (A + BK)x(k) - Bke(k) + Bv(k)$$
$$e(k+1) = (A - LC)e(k)$$

So we can see that L is not influencing the original system and therefore it's not destabilizing it. If we have a "wrong" design for L and K then even if your estimates are wrong you won't affect heavily the original system.

This is called the **separation principle**:

$$det\left(\left[\begin{cases} \lambda I - (A + BK) & BK \\ 0 & \lambda I - (A - LC) \end{cases}\right]\right) =$$
$$det(\lambda I - (A + BK))det(\lambda I - (A - LC))$$

This means that we have an **independent design** of the matrices $L$ and $K$.

The dynamic compensator in state-space is:

$$\begin{cases} \hat{x}(k+1) = (A + BK - LC)\hat{x}(k) + Bv(k) + Ly(k) \\ u(k) = K\hat{x}(k) + v(k) \end{cases}$$

*Note:* If we have an exercise we usually start with $A, B, C$ and we have to find $K, L$.

*Note:* by looking at $y(k)$ we can see that L has an effect on the transient, even if it should be noted that asymptotically if the two blocks are stable then everything will be fine.

**Rule of thumb:** place the observer eigenvalues $\approx$ 10 times faster than the controller eigenvalues. (*Note:* this means that we will likely have a very big spike in the beginning but we will also have a fast convergence)
