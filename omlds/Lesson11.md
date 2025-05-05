# MPC and LQR

## Uncostrained LQR

The LQR controller is a state-feedback controller that is designed to minimize an infinite quadratic cost function:

$$J(x_0) = \sum_{i=0}^{\infty} x_i^TQx_i + u_i^TRu_i$$

And reads as:

$$K_{lqr} = -(R + B^T P_{lqr}B)^{-1}B^T P_{lqr}A$$

Where $P_{lqr}$ is the solution of the **Riccati equation**:

$$P = A^TPA - A^TPB(B^TPB + R)^{-1}B^TPA + Q$$

## Constrained LQR

If we add a constraint to the input we get:

$$\begin{cases} \min_u x_T^TPx_T + \sum_{i=0}^{T-1} x_i^TQx_i + u_i^TRu_i \\ \text{s.t.} \; x_{i+1} = Ax_i + Bu_i \; i \in \tau \\ u_{min} \leq u_i \leq u_{max} \\ y_{min} \leq Cx_i \leq y_{max} \\ u_j = Kx_j, j \in \tau \end{cases}$$

For any choice of $T, N, R = R^T > 0, Q = Q^T > 0$ in a polyhedral region around the origin: **constrained MPC = constrained LQR**

*Note:* check the slides on how to use this.
