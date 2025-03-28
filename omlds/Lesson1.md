# Non linear systems described as linear ones

**Idea:** abstract a nonlinear system with a linear one

**Definition(Equilibrium):** The constant pair $(x_0,u_0)$ is an equilibrium point of the system if, for $x(0) = x_0$ and $u(t) = u_0$ for all $t >= 0$, the solution $x(t)$ satisfies $x(t) = x_0$ for all $t >= 0$.  
**Matematically:** $f(x_0, u_0, t) = 0 \forall t >= 0$.

We want to analyze the trajectory of $\Delta x(t) = x(t) - x_0$ for small perturbations $\Delta u(t) = u(t) - u_0$.  
Using the Taylor expansion of $f(x,u,t)$ around $(x_0,u_0)$, we have:
$$f(x,u,t) = f(x_0,u_0,t) + \frac{\partial f}{\partial x}(x_0,u_0,t)\Delta x + \frac{\partial f}{\partial u}(x_0,u_0,t)\Delta u + \frac{\partial f}{\partial t}(x_0,u_0,t)\Delta t + \dots$$

I can get two Jacobians:

$$A = \frac{\partial f}{\partial x}(x_0,u_0,t) \in \mathbb{R}^{n \times n}$$
$$B = \frac{\partial f}{\partial u}(x_0,u_0,t) \in \mathbb{R}^{n \times m}$$

From which we find that:

$$\Delta \dot{x} = A\Delta x + B\Delta u$$
$$\Delta y(t) = C\Delta x(t) + D\Delta u(t)$$

Where $C = \frac{\partial h}{\partial x}(x_0,u_0,t) \in \mathbb{R}^{p \times n}$ and $D = \frac{\partial h}{\partial u}(x_0,u_0,t) \in \mathbb{R}^{p \times m}$.

So in the vicinity of the equilibrium point, the system can be described by a linear system.

## Why it's important to analyze linear systems?

We consider a state-space description of an LTI system:

$$\dot{x} = Ax + Bu$$
$$y(t) = Cx(t) + Du(t)$$

We want to determine the solution of the system for a given initial condition $x(0) = x_0$ and input $u(t) = u_0$ for all $t >= 0$.

### Existence of a solution

$\dot{x} = f(x,u,t)$ is a nonlinear ODE, this means that for arbitrary choices of $f$ and $u(.)$ a solution might not exist.

Moreover even if a solution exists, it might not be unique.

*Note:* a linear system on the other hand always has a solution and it's also unique.

**Lipschitz continuity:** Given a continuous input signal $u(t)$, for all $x(0) = x_0$ the LTI system:
$$\dot{x} = Ax + Bu$$
$$y(t) = Cx(t) + Du(t)$$
is guaranteed to have a unique solution $x(t) = \phi(t,x_0,u)$ and associated output $y(t)$.

**Proof:** $\dot{x} = Ax + Bu$, $x(0) = x_0$ and $u(t) = u_0$  
$g(x) = Ax + Bu$ is Lipschitz continuous in $x$ with Lipschitz constant $L$ if:
$$||g(x) - g(y)|| \leq L||x - y|| \forall x,y \in \mathbb{R}^n$$  
I consider $x, \tilde{x} \in \mathbb{R}^n$.  
$$||Ax + Bu - A\tilde{x} - Bu|| = ||A(x - \tilde{x})|| = (x-\tilde{x})A^TA(x-\tilde{x})$$
$$\leq \lambda_{max}(A^TA)||x-\tilde{x}||^2$$
$$||Ax + Bu - A\tilde{x} - Bu|| \leq \sqrt{\lambda_{max}(A^TA)}||x-\tilde{x}||$$
Which means that $g(x) = Ax + Bu$ is Lipschitz continuous in $x$ with Lipschitz constant $L = \sqrt{\lambda_{max}(A^TA)}$.

### Characterization of the solution

For LTI systems solutions can also be computed in closed form.

*Example:*

**Particular first order differential equation:** $\dot{x} = ax(t)$, $x(0) = x_0$, solution: $x(t) = x_0e^{at}$

**General first order differential equation:** $\dot{x} = ax(t) + Bu(t)$, $x(0) = x_0$, solution: $x(t) = e^{At}x_0 + \int_0^t e^{A(t-\tau)}Bu(\tau)d\tau$, $y(t) = Ce^{At}x_0 + \int_0^t Ce^{A(t-\tau)}Bu(\tau)d\tau + Du(t)$

**Proof:** I want to prove that $x(t) = e^{At}x_0 + \int_0^t e^{A(t-\tau)}Bu(\tau)d\tau$ is a solution of the system.  

1. I prove that satisfies initial condition: $x(0) = x_0$.  
$x(0) = e^{A0}x_0 + \int_0^0 e^{A(0-\tau)}Bu(\tau)d\tau = x_0 + 0 = x_0$ This is because the integral is zero.
2. I start from the Leibniz rule: $\frac{d}{dt}\int_{a(t)}^{b(t)}f(t,\tau)d\tau = \frac{\partial f}{\partial t}(t,b(t)) - \frac{\partial f}{\partial t}(t,a(t)) + \int_{a(t)}^{b(t)}\frac{\partial f}{\partial t}(t,\tau)d\tau$, with $a(t) = 0$ and $b(t) = t$. From this:  
$\dot{x}(t) = \frac{d}{dt}e^{At}x_0 + Be^{A(t-t)}u(t)\frac{dt}{dt} - Be^{A(t-0)}u(0)\frac{d0}{dt} + \int_0^t\frac{d}{dt}e^{A(t-\tau)}Bu(\tau)d\tau$, which for the chain rule becomes:  
$\dot{x}(t) = Ae^{At}x_0 + Bu(t) + A\int_0^t Be^{A(t-\tau)}u(\tau)d\tau = A(e^{At}x_0 + \int_0^t e^{A(t-\tau)}Bu(\tau)d\tau) + Bu(t) = Ax(t) + Bu(t)$

For a discrete time system I get almost the same but simplified

## Computational aspects

### State transition matrix

The state transition matrix $\Phi(t,t_0)$ is defined as the solution of the system $\dot{x} = Ax$, $x(t_0) = x_0$.

We consider that in this case the state transition matrix = matrix exponential: $\Phi(t,t_0) = e^{At} = \sum_{k=0}^{\infty}\frac{A^k(t-t_0)^k}{k!}$

### How to compute the state transition matrix?

#### Diagonalizable matrix

If the matrix is diagonalizable then I have that:

$$A = W\Lambda W^{-1}$$

Where $\Lambda$ is the diagonal matrix of eigenvalues of $A$ and $W$ is the matrix of eigenvectors of $A$.

$$e^{At} = We^{\Lambda t}W^{-1}$$

Where $e^{\Lambda t}$ is the diagonal matrix of the exponentials of the eigenvalues of $A$.

**Proof:**

In general for a diagonalizable matrix $A$ I have that:

$$A^k = W\Lambda^kW^{-1}$$

This can be proven by induction:

1. For $k = 0$: $A = W\Lambda^0 W^{-1} = W I W^{-1} = W W^{-1} = A^0$
2. I assume that $A^k = W\Lambda^kW^{-1}$ is true and I want to prove that $A^{k+1} = W\Lambda^{k+1}W^{-1}$ is true.  
$A^{k+1} = A^kA = W\Lambda^kW^{-1}W\Lambda W^{-1} = W\Lambda^k\Lambda W^{-1} = W\Lambda^{k+1}W^{-1}$ (because $W^{-1}W = I$)

Moreover I have that by Taylor expansion:

$$e^{At} = I + At + \frac{A^2t^2}{2!} + \dots = WW^{-1} + W\Lambda tW^{-1} + \frac{W\Lambda^2t^2W^{-1}}{2!} + \dots =$$
$$=W(I + \Lambda t + \frac{\Lambda^2t^2}{2!} + \dots)W^{-1} = We^{\Lambda t}W^{-1}$$

*Note:* this is a very simple case that works for discrete-time systems.

*Example:*

I consider A = $\begin{bmatrix} 0 & 2 \\ -1 & -3 \end{bmatrix}$

I compute the eigenvalues and eigenvectors of $A$:

$$det(A - \lambda I) = 0 \Rightarrow det(\begin{bmatrix} 0 & 2 \\ -1 -3 \end{bmatrix} - \begin{bmatrix} \lambda & 0 \\ 0 & \lambda \end{bmatrix}) =$$
$$= det(\begin{bmatrix} -\lambda & 2 \\ -1 & -3-\lambda \end{bmatrix}) = 0 \Rightarrow \lambda^2 + 3\lambda + 2 = 0 \Rightarrow \lambda_1 = -1, \lambda_2 = -2$$

I compute the eigenvectors ($Av_1 = \lambda_1v_1, Av_2 = \lambda_2v_2$):

For $\lambda_1 = -1$ I have that:

$$\begin{bmatrix} 0 & 2 \\ -1 & -3 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = -1\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \Rightarrow \begin{bmatrix} 0 & 2 \\ -1 & -3 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} -x_1 \\ -x_2 \end{bmatrix}$$

From this I get that $x_1 = -2x_2$.

For $\lambda_2 = -2$ I have that:

$$\begin{bmatrix} 0 & 2 \\ -1 & -3 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = -2\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \Rightarrow \begin{bmatrix} 0 & 2 \\ -1 & -3 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} -2x_1 \\ -2x_2 \end{bmatrix}$$

I solve this system and I get that $x_1 = -x_2$.

If I consider $\alpha = 1$ then I get that $v_1 = \begin{bmatrix} -2 \\ 1 \end{bmatrix}$ and $v_2 = \begin{bmatrix} -1 \\ 1 \end{bmatrix}$.

From this I get that: $\Lambda = \begin{bmatrix} -1 & 0 \\ 0 & -2 \end{bmatrix}$ and $e^At = W\begin{bmatrix} e^{-t} & 0 \\ 0 & e^{-2t} \end{bmatrix}W^{-1} = \begin{bmatrix} -2e^{-t} + e^{-2t} & -2e^{-t} + 2e^{-2t} \\ e^{-t} - e^{-2t} & e^{-t} - 2e^{-2t} \end{bmatrix}$

#### Non-diagonalizable matrix

If the matrix is not diagonalizable then I have that W is not invertible.

In this case I have that: $A = \lambda I + N$, where $\lambda$ is the eigenvalue of $A$ and $N$ is the nilpotent matrix.

*Note:* a matrix is nilpotent if there exists an integer $\tilde{k}$ such that $N^k = 0 \forall k > \tilde{k}$.

This property allow to do some simplifications in the computation of the matrix exponential.

In general I can use the Jordan form of the matrix $A$:

$$A = WJW^{-1}$$

Where $J$ is the Jordan form of $A$.

*Note:* we wont' go into details of the Jordan form and we will skip the proof of the matrix exponential for non-diagonalizable matrices. In general we can use a software solution in Python, Julia or Matlab (or even something else actually)

## Eigenvalues, eigenvectors and modes

Starting from an example, we can consider a **two-state autonomous linear system**. We have two (real) eigenvectors $w_1$ and $w_2$ corresponding to two eigenvalues: $\lambda_1$ and $\lambda_2$.

If we consider $x_0 = w_i$ then $Aw_i = \lambda_iw_i \rightarrow \dot{x}(0) = Ax_0 = Aw_i = \lambda_iw_i$.

The direction of $\dot{x}(0)$ is the same as the direction of $w_i$ and the magnitude of $\dot{x}(0)$ is $\lambda_i$ times the magnitude of $w_i$. *I.e:* $||x(t)||$ depends on $sgn(\lambda_i)$.

What happens if we consider $x_0 \neq w_i$? We can decompose $x_0$ in the eigenvectors basis: $x_0 = \alpha_1w_1 + \alpha_2w_2$. Then $x(t) = \alpha_1e^{\lambda_1t}w_1 + \alpha_2e^{\lambda_2t}w_2$.

**In general we have that:** $x(t) = \sum_{i=1}^{n}\alpha_i e^{\lambda_it}w_i$.
The state-trajectory is the natural response for a given $x_0$: $x(t) = e^{At}x_0 = We^{\Lambda t}W^{-1} x_0 = W\begin{bmatrix} e^{\lambda_1t} & 0 \\ 0 & e^{\lambda_2t} \end{bmatrix}\alpha = \sum_{i=1}^{n}\alpha_i e^{\lambda_it}w_i$. P(M(t) = m) + \sum_{a \in \Tau} C(a) lim P(A(t) = a)$$

### In discrete-time systems

In discrete-time systems we have that $x(k+1) = Ax(k)$. We can consider that $A = W\Lambda W^{-1}$ and $x(k) = W\Lambda^kW^{-1}x(0)$. We can consider that $x(0) = \alpha_1w_1 + \alpha_2w_2$ and then $x(t) = \sum_{i=1}^{n}\alpha_i\lambda_i^kw_i$.

*Note:* check the slides for examples about both diagonalizable and non-diagonalizable matrices
