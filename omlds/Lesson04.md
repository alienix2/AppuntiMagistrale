# Reachability for control design

## Kalman decomposition

**Theorem:** Subsystem of a system:

Any LTI system can be brought, by means of an appropeirate linear coordinate transformation, to the form:

$$ \begin{bmatrix} \cdot{x_1} & \cdot{x_2} & \cdot{x_3} & \cdot{x_4} \end{bmatrix} = \begin{bmatrix} A_{11} & 0 & A_{13} & 0 \\ A_{21} & A_{22} & A_{23} & A_{24} \\ 0 & 0 & A_{33} & 0 \\ 0 & 0 & A_{43} & A_{44} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} + \begin{bmatrix} B_1 \\ B_2 \\ 0 \\ 0 \end{bmatrix} u $$

Where $eig(A) = \bigcup_{i=1}^{4} eig(A_{ii})$ and the state is partitioned into:

$$ x = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} $$

With $x_1$ reachable + observable, $x_2$ reachable + unobservable, $x_3$ unreachabe + observable, $x_4$ unreachabe + unobservable.

We can then define two subsystems, the **reachable subsystem** and the **unreachable subsystem**. For the **unreachable**/**unobservable** subsystems we cannot control or observe these parts.

*Note:* stability iff:

- $A_{33}$ and $A_{44}$ are unreachable
- $A_{33}$ and $A_{44}$ are stable

## Minimum effort control

We consider $\frac{1}{2}\sum_{i=0}^{T-1} ||u_i||^2$ as the energy of $u(0), u(1), \ldots, u(T-1)$.

**Problem:** Let (A,B) reachable. How to steer the system from $x(0) = x_1$ to $x(T) = x_2, T \geq n$, with the minimum energy control action?

$$x_2 - A^T x_1 = \begin{bmatrix} B & AB & \ldots & A^{T-1}B \end{bmatrix} \begin{bmatrix} u(T-1) \\ u(T-2) \\ \vdots \\ u(0)\end{bmatrix}$$

By **Caley-Hamilton** we have that $rank(R_T) = rank(R) = n \Rightarrow rank([R_TX]) = n$.  
This system admits a solution and $\frac{1}{2}||u||^2 = \frac{1}{2}\sum_{i=0}^{T-1} ||u_i||^2 = \frac{1}{2}U^TU \Rightarrow U^*=argmin_{U} \frac{1}{2}||U||^2$ s.t. $X=R_TU$

*Note:* this comes from the fact that if we write:

$$\frac{1}{2}\sum_{i=0}^{T-1} ||u(j)||^2$$

With $u(j)\in \mathbb{R}^m$ and $U = \begin{bmatrix} u(T-1, u(T-2), \ldots, u(0) \end{bmatrix}^T$ we have that $||x||^2 = x^Tx$ and therefore:

$$\frac{1}{2}||U||^2 = \frac{1}{2}U^TU = \frac{1}{2} \begin{bmatrix} u(T-1) & u(T-2) & \ldots & u(0) \end{bmatrix} \begin{bmatrix} u(T-1) \\ u(T-2) \\ \ldots \\ u(0) \end{bmatrix} = \frac{1}{2} \sum_{i=0}^{T-1} ||u_i||^2$$

From here since we have a problem that is convex we can solve it by using the **Lagrange Multipliers** method:

$$L(U, \lambda) = \frac{1}{2}U^TU + \lambda^T(R_TU - X)$$

$$\frac{\partial L}{\partial U} = U + R_T^T\lambda = 0 \Rightarrow U = -R_T^T\lambda$$

$$\frac{\partial L}{\partial \lambda} = R_TU - X = 0 \Rightarrow R_TU = X$$

From here we can substitute the first equation into the second one and we get:

$$R_TR_T^T\lambda = X \Rightarrow \lambda = (R_TR_T^T)^{-1}X$$

*Note:* $R_TR_T^T$ is invertible since $rank(R_T) = n \forall T \geq n$.  
$U^* = [u^*(T), u^*(T-1), \ldots, u^*(0)]^T$ is an optimal sequence **yet an open loop** meaning that no state/output measurements are used.

## Closed loop dynamics

How can i design a feedback control input to steer an LTI system to a desired state?

We start by focusing on **state measurements** which means that $C = I$.

We consider that $x(k+1) = Ax(k) + Bu(k)$ and $u(k) = Kx \Rightarrow x(k+1) = (A+BK)x(k)$.

**Theorem:** given $(A,B)$ reachable $\Rightarrow eig(A+BK)$ can be placed arbitrarily.

### Controllable canonical form

Given $(A,B)$ reachable, we can find a transformation $T$ such that:

$$\hat{A} = \begin{bmatrix} 0 & 1 & 0 & \ldots & 0 \\ 0 & 0 & 1 & \ldots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \ldots & 1 \\ -a_0 & -a_1 & -a_2 & \ldots & -a_{n-1} \end{bmatrix}, \hat{B} = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{bmatrix}$$

The coefficients $a_0, a_1, \ldots, a_{n-1}$ characterize the characteristic polynomial of $\hat{A}: p_{\hat{A}}(\lambda) = det(\lambda I - \hat{A}) = \lambda^n + a_{n-1}\lambda^{n-1} + \ldots + a_1\lambda + a_0$.

The transformation matrix $T$ is given by:

$$T = R \begin{bmatrix} a_1 & a_2 & \ldots & a_{n-1} & 1 \\ a_2 & a_3 & \ldots & 1 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ a_{n-1} & 1 & \ldots & 0 & 0 \\ 1 & 0 & \ldots & 0 & 0 \end{bmatrix}$$

Where $R$ is the inverse of the matrix:

*Example:*

$\cdot{x} = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \cdot{x} + \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} u$

$T \in \mathbb{R}^{3x3}$, $rank(\begin{bmatrix} 0 & 2 & 4 \\ 2 & 2 & 2 \\ 1 & 2 & 4 \end{bmatrix}$) = 3

$p_{\hat{A}}(\lambda) = det(\lambda I - \hat{A}) = \lambda^3 - 4\lambda^2 + 5 \lambda -2$, with $a_0 = 2, a_1 = 5, a_2 = -4, a_3 = 1$

$$T = \begin{bmatrix} 0 & 2 & 4 \\ 2 & 2 & 2 \\ 1 & 2 & 4 \end{bmatrix} \begin{bmatrix} 5 & -4 & 1 \\ -4 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} -4 & 2 & 0 \\ 4 & -6 & 2 \\ 1 & -2 & 1 \end{bmatrix}$$

$$\hat{A} = T^{-1}AT = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 2 & -5 & 4 \end{bmatrix}, \hat{B} = T^{-1}B = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$

## Pole placement

*Note:* the name comes from the past, we are actually going to place eigenvalues.

We assume to have $(A,B)$ reachable and already in canonical form and m = 1. Then we consider $K = \begin{bmatrix} k_1 & k_2 & \ldots & k_n \end{bmatrix}$ and the closed-loop turns into:

$$A+BK = \begin{bmatrix} 0 & 1 & 0 & \ldots & 0 \\ 0 & 0 & 1 & \ldots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \ldots & 1 \\ -(a_0-k_1) & -(a_1-k_2) & -(a_2-k_3) & \ldots & -(a_{n-1}-k_n) \end{bmatrix}$$

With $p_{A+BK}(\lambda) = \lambda^n + (a_{n-1} - k_n)\lambda^{n-1} + \ldots + (a_1 - k_2)\lambda + (a_0 - k_1)$.

We assume we have a target polynomial $p_d(\lambda) = \lambda^n + d_{n-1}\lambda^{n-1} + \ldots + d_1\lambda + d_0$ and we want to find $K$ such that $p_{A+BK}(\lambda) = p_d(\lambda) \Rightarrow K = \begin{bmatrix} a_0 - d_0 & a_1 - d_1 & \ldots & a_{n-1} - d_{n-1} \end{bmatrix}$.

*Example:*

We consider a CT LTI system with matrices:

$A = \begin{bmatrix} 0 & 1 \\ -1 & 2 \end{bmatrix}, B = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$ we want to place the eigenvalues in $\{-1, -2\}$

$$det(\lambda I - A) = \lambda^2 - 2\lambda + 1 = (\lambda - 1)^2 \Rightarrow eig(A) = \{1, 1\}$$

We realize that these values are unstable and therefore we want them to become stable by bringing them to the imaginary field.

$$n = 2, m = 1 \Rightarrow K = \begin{bmatrix} k_1 & k_2 \end{bmatrix}$$

$$A+BK = \begin{bmatrix} 0 & 1 \\ -1+k_1 & 2+k_2 \end{bmatrix}$$

$$det(\lambda I - A - BK) = \lambda^2 - (2+k_2)\lambda + 1 - k_1 = \lambda^2 + 3\lambda + 2 = p_d(\lambda)$$

$$p_{A+BK}(\lambda) = \lambda^2 - (2 + k_2)\lambda + 1 - k_1 \Rightarrow k_1 = -1, k_2 = -5$$

$$ rank(\begin{bmatrix} 0 & 1 \\ 1 & -1 \end{bmatrix}) = 2 \Rightarrow (A,B) \text{ is reachable}$$

The linear controller is therefore $K = \begin{bmatrix} k_1 & k_2 \end{bmatrix} = \begin{bmatrix} -1 & -5 \end{bmatrix}$ and that is unique.

### MIMO systems

We say that in general for SISO LTI systems it holds:

**Theorem:** given $(A,B)$ reachable, $\forall \lambda_1, \ldots, \lambda_n \in \mathbb{C}$ there exists $K \in \mathbb{R}^{mxn}$ such that $eig(A+BK) = \{\lambda_1, \ldots, \lambda_n\}$.

### Unreachable systems

For unreachable systems we have that:

**Theorem:** $rank(R) = n_r < n \Rightarrow$ the eigenvalues **cannot** be assigned arbitrarily.

**Proof:** If we look at the controllable canonical form we have that the eigenvalues of the unreachable part cannot be changed.  
We can express this part as:

$$\dot{x} = \begin{bmatrix} A_{11} & A_{12} \\ 0 & A_{22} \end{bmatrix} \cdot{x} + \begin{bmatrix} B_1 \\ 0 \end{bmatrix} u$$

This means that the closed loop matrix will be:

$$\begin{bmatrix} A_{11} + BK_v & A_{12} + BK_{ur} \\ 0 & A_{22} \end{bmatrix}$$
  
Where $K_v$ is the part of the controller that is acting on the reachable part and $K_{ur}$ is the part of the controller that is acting on the unreachable part.

As we can see in that case the part of the controller that is acting on the unreachable part will not be able to change the eigenvalues of the unreachable part.

*Note:* The system is called **stabilizable** if the eigenvalues of the unreachable part are stable.
