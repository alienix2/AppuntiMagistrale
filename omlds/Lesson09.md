# Model predictive control

## MPC philosophy

To start off we have:

$$\begin{cases} \min_{(u_i)_i \in \tau} \sum_{i \in \tau} \frac{1}{2} (||y_i - y_{i,ref}||_Q^2 + ||u_i - u_{i,ref}||_R^2) \\ \text{s.t.} \; x_{i+1} = Ax_i + Bu_i \; i \in \tau \\ y_i = Cx_i, i \in \tau \\ x_i \in \mathcal{X}, u_i \in \mathcal{U} \; i \in \tau \\ x_0 = x(k)\end{cases}$$

Where:

- $u_i \; x_i$ are the constaints
- $x_0 = x(k)$ is the state/output feedback
- The first two rows represent a **prediction model**

The basic idea is to feed the very first piece of the control signal to the system and then repeat the process at the next time step. This is called **receding horizon control**.

In words the steps are:

1. At time $k$ we measure the state $x(k)$ and we set $x_0 = x(k)$
2. We optimize w.r.t ${u_0, \cdots, u_{T-1}}$
3. We apply $u_0^*$ only as $u(k)$

*Note:* in this approach we are recalculating the best next step at each step. We don't care of the previous calculations. The main drawback that we have is that we need to solve a new system at each step and we might not be able to perform the calculation fast enough. *Example:* A drone cannot be controlled by using this technique.

## Uncostrained MPC

We consider a linear prediction model:

$$\begin{cases} x_{i+1} = Ax_i + Bu_i \\ y_i = Cx_i \end{cases}$$

We consider a discrete time evolution:

$$x(k) = A^kx_0 + \sum_{i=0}^{k-1} A^{k-i-1}Bu_i, x_0 = x(k)$$

We also define a performance index:

$$J(u, x_0) = x_T^TPx_T + \sum_{i=0}^{T-1} (x_i^TQx_i + u_i^TRu_i)$$

With $u$ = $(u_0, \cdots, u_{T-1})^T$

So we can write it in QP form:

$$\begin{cases} \min x_T^TPx_T + \sum_{i=0}^{T-1} (x_i^TQx_i + u_i^TRu_i) \\ \text{s.t.} \; x_{i+1} = Ax_i + Bu_i \; i \in \tau \\ x_0 = x(k)\end{cases}$$

$x_k = A^kx_0 + \sum_{i=0}^{k-1} A^{k-i-1}Bu_i$

The vector of the $x$ is:

$$\begin{bmatrix} x_0 \\ x_1 \\ \vdots \\ x_T \end{bmatrix} = \begin{bmatrix} B & 0 & \cdots & 0 \\ AB & B & \cdots & 0 \\ A^2B & AB & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ A^{T-1}B & A^{T-2}B & \cdots & B \end{bmatrix} \begin{bmatrix} u_0 \\ u_1 \\ \vdots \\ u_{T-1} \end{bmatrix} + \begin{bmatrix} A \\ \vdots \\ A^{T} \end{bmatrix} x_0$$

So $J(u, x_0) = \frac{1}{2} u^T H u + x_0^T F u$

*Note:* The part of the function that would be given by $\frac{1}{2} x_0^TYx_0$ is equal to 0.

The optimum is given by the **standard first-order equation:**

$$\nabla J(u, x_0) = H u + F x_0 = 0 \Rightarrow u^* = -H^{-1}F$$

We are not exploiting the full potential of the MPC because we can find an **optimal state feedback policy** but we didn't include any constraint.

## State-constrained MPC

We add linear constraint of type $Dx_i \leq d$ to the previous problem. We can write the problem as:

$$\begin{cases} \min x_T^TPx_T + \sum_{i=0}^{T-1} (x_i^TQx_i + u_i^TRu_i) \\ \text{s.t.} \; x_{i+1} = Ax_i + Bu_i \; i \in \tau \\ x_0 = x(k) \\ Dx_i \leq d \; i \in \tau\end{cases}$$

We can turn state constraints into input constraints because everything is linear and therefore we end up with:

$$V(x_0) = \min_{u \in \mathcal{U}} \frac{1}{2} u^T H u + x_0^T F u \; \text{s.t.} \; Gu \leq w + Sx_0$$

*Note:* example on the slides.

## Output tracking

We want to force $y(k)$ to follow a reference trajectory $y_{ref}(k)$.

We should parametrize the control input through a **control increment**:

$$\Delta u(k) = u(k) - u_{ref}(k-1)$$

We can consider the modified extended linear system:

$$\begin{cases} \begin{bmatrix} x(k+1) \\ x_a(k+1) \end{bmatrix} = \begin{bmatrix} A & B \\ 0 & I \end{bmatrix} \begin{bmatrix} x(k) \\ x_a(k) \end{bmatrix} + \begin{bmatrix} B \\ I \end{bmatrix} \Delta u(k) \\ y(k) = \begin{bmatrix} C & 0 \end{bmatrix} \begin{bmatrix} x(k) \\ x_a(k) \end{bmatrix}\end{cases}$$

We can write the associated optimal cost problem as:

$$\begin{cases} \min \sum_{i=0}^{T-1} ||y_i - y_{i,ref}||_{W^y}^2 + ||\Delta u_i||_{W^u}^2 \\ \text{s.t.} \; \begin{bmatrix} x(k+1) \\ x_a(k+1) \end{bmatrix} = \begin{bmatrix} A & B \\ 0 & I \end{bmatrix} \begin{bmatrix} x(k) \\ x_a(k) \end{bmatrix} + \begin{bmatrix} B \\ I \end{bmatrix} \Delta u(k) \\ y(k) = \begin{bmatrix} C & 0 \end{bmatrix} \begin{bmatrix} x(k) \\ x_a(k) \\ \end{bmatrix} \\ \Delta u(k) \in \mathcal{U} \end{cases}$$

For control input parametrization, with manipulations we can get:

$$\begin{cases} \min \frac{1}{2} z^T H z + [x^T(k) \; y_{ref}^T(k)u^T(k-1)]F^Tz \\ s.t \; G z \leq w + Sx(k) \\ z = \begin{bmatrix} \Delta u \\ x_a \\ y - y_{ref} \end{bmatrix} \end{cases}$$

Where $z$ is the optimization variable.
