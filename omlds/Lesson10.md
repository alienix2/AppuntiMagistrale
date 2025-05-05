# Feasibility, stability and convergence

## Feasibility

We consider the general definition of the MPC problem:

$$\begin{cases} \min_z \sum_{i=0}^{T-1} ||y_i - y_{i,ref}||_{W^y}^2 + ||\Delta u_i||_{W^u}^2 \\ \text{s.t.} \; \begin{bmatrix} x(k+1) \\ x_a(k+1) \end{bmatrix} = \begin{bmatrix} A & B \\ 0 & I \end{bmatrix} \begin{bmatrix} x(k) \\ x_a(k) \end{bmatrix} + \begin{bmatrix} B \\ I \end{bmatrix} \Delta u(k) \\ y(k) = \begin{bmatrix} C & 0 \end{bmatrix} \begin{bmatrix} x(k) \\ x_a(k) \\ \end{bmatrix} \\ z = \begin{bmatrix}\Delta u_0 \\ \vdots \\ \Delta u_{T-1} \end{bmatrix} \end{cases}$$

But will the QP be feasible at any instant?

If we consider input constraints only then **QP is always feasible** (if the constraints on u or $\Delta U$ are consistent.

If we include the output/state constraints then the QP may be infeasible:

- T < $\infty$: there are no guarantees that QP will remain feasible
- T = $\infty$: OK, but working with infinite number of constraints is not practical

We will mostly work with problems that are **recursively feasible**.

## Stability

For the basic convergence result we can consider the **Theorem:**

Let the MPC problem be defined as:

$$V(x(k)) = \min_{u \in \mathcal{U}} \sum_{i=0}^{T-1} x_i^TQx_i + u_i^TRu_i$$

$$\text{s.t.} \; x_{i+1} = Ax_i + Bu_i \; i \in \tau$$

$$x_T = 0$$

$$R = R^T > 0, Q = Q^T >0$$

If it is feasible at $k = 0$ then $lim_{k \to \infty} x(k) = 0$ and $lim_{k \to \infty} u(k) = 0$ and the constraints are satisfied.

**Proof:**

$$x(k+1) = Ax(k) + Bu(k)$$

We want to prove that $\lim_{k \to \infty} x(k) = 0$.

$$V(x(k)) = \sum_{i=0}^{T-1} x_i^TQx_i + u_i^TRu_i$$
$$\text{s.t.} \; x_{i+1} = Ax_i + Bu_i \; i \in \tau \; x_0 = x(k), u \in \mathcal{U}, x \in \mathcal{X}, x_T = 0$$

What we want to do is use the **Lyapunov function**.

I consider the vector:

$$u_k^* = \begin{bmatrix} u_0^k \\ u_1^k \\ \vdots \\ u_{T-1}^k \end{bmatrix}$$

And also the new vector:

$$u_{k+1} = \begin{bmatrix} u_1^{k} \\ u_2^k \\ \vdots \\ u_{T-1}^k \\ 0 \end{bmatrix}$$

Which will be feasible because it's obtained from the previous one in all it's component except for the last one.

$$V(x(k+1)) = V(x(k+1)), u_{k+1}) =$$
$$x_1^TQx_1 + \cdots + x_T^TQx_T + u_1^{k^T}Ru_1^k + \cdots + u_{T-1}^{k^T}Ru_{T-1}^k$$
$$\geq V(x(k+1), u_{k+1}^*)$$

If we write:

$$V(x(k), u_k^*) = x_0^TQx_0 + x_{T-1}^TQx_{T-1} + \cdots + u_0^{k^T}Ru_0^k + \cdots + u_{T-1}^{k^T}Ru_{T-1}^k$$

We realize that this is very similar to the other one, except for the first of the $x$ terms and the first of the $u$ terms.

$$V(x(k+1), u_{k+1}) = V(x(k), u_k^*) - x_0^TQx_0 - u_0^{k^T}Ru_0^k=$$
$$= V(x(k), u_k^*) - x_0^TQx_0 - u(k)^TRu(k)$$

*Note:* Bot the components that we are subtracting are positive.

So the optimal value is monotonically decreasing.

$$\Rightarrow 0 \leq x^T(k)Qx(k) + u^T(k)Ru(k) \leq V(x(k), u_k^*) - V(x(k+1), u^*_{k+1})$$

So knowing that both the first and last term go to 0 we can conclude that:

$$\lim_{k \to \infty} x^T(k)Qx(k) + u^T(k)Ru(k) = 0$$

And this can happen only if:

$$\lim_{k \to \infty} x^T(k)Qx(k) = 0 \Rightarrow x(k) \rightarrow 0$$
$$\lim_{k \to \infty} u^T(k)Ru(k) = 0 \Rightarrow u(k) \rightarrow 0$$

*Note:* we know that $x(T) = Ax(T-1) + Bu^k_{T-1} = 0$ not depending on the value of $x(T-1)$ because we imposed that $x_T = 0$.

## Convergence

We want to track a constant reference trajectory. We assume that $x_{ref}$ and $u_{ref}$ exist s.t:

$$\begin{cases} x_{ref}(k+1) = Ax_{ref}(k) + Bu_{ref}(k) \\ y_{ref}(k) = Cx_{ref}(k) \end{cases}$$

I can then formulate the MPC problem as:

$$\min_u \sum_{i=0}^{T-1} (y_i - y_{i,ref})^T W^y (y_i - y_{i,ref}) + (u_i - u_{i,ref})^T W^u (u_i - u_{i,ref})$$

*Note:* there are other possible stability constraints that can produce meaningful results but we won't see them in the course.
