# More on Convex optimization

## Dual function

Given the same problem discussed in the previous lecture, we can define the **dual function** as:

$$ q:\mathbb{R}^n \to \mathbb{R} \cup \{-\infty\} $$
$$ q(\lambda) = \inf_{x \in \mathcal{X}} \left( f(x) + \sum_{i \in \mathbb{I}} \lambda_i g_i(x) + \sum_{j \in \mathbb{J}} \nu_j h_j(x) \right) $$

Where $\lambda_i$ are the Lagrange multipliers for the inequality constraints and $\nu_j$ are the Lagrange multipliers for the equality constraints.

The domain $\mathcal{D}$ of the dual function is given by the set of all $(\lambda, \nu)$ such that $(\lambda_i, \nu_j) \rightarrow \infty$.

**Theorem (weak duality)**: The dual function is a lower bound for the primal problem. This means that:

$$q(\lambda, \nu) \leq f(x)$$

**Theorem (property of the dual function):** The dual function $q(\lambda, \nu)$ is concave and it's domain is convex.

*Note:* in general the dual function gives information about the primal problem. The dual function is a lower bound for the primal problem. This means that if we find a solution to the dual problem, we can use it to approximate the solution to the primal problem.

*Note:* **strong duality** happens when the dual function is equal to the primal function. The **duality gap** is defined as the difference between the primal and dual functions. The dual gap is defined as:

### Defining a dual problem from an LP

We start from an LP in the form:

$$\begin{cases} \min c^T x \\ s.t. \; Ax \leq b \\ x \geq 0 \end{cases}$$

Where $c$ is the cost vector, $A$ is the constraint matrix, $b$ is the constraint vector and $x$ is the variable vector.

We have that $A \in \mathbb{R}^{m \times n}$, $b \in \mathbb{R}^m$ and $c \in \mathbb{R}^n$.

First of all we want to find the Lagrangian function ($\mathcal{L} = f(x) + \lambda^Tg(x) + \nu^Th(x)$)
of the problem. The Lagrangian function is defined as:

$$L(x, \lambda) = c^T x + \lambda^T (Ax - b)$$

We get that:

$$q(\lambda) = \inf_{x \in \mathcal{X}} L(x, \lambda) =$$
$$= \inf_{x \in \mathcal{X}} (c^T x + \lambda^T (Ax - b)) =$$
$$= -\lambda^T b + \inf_{x \in \mathcal{X}} (c + A^T \lambda)^T x$$

What happens is that this tends to infinity unless the term $(c + A^T \lambda)$ is equal to zero. This means that we get:

$$\begin{cases} -b^T \lambda \; \text{if} \; c + A^T \lambda = 0 \\ -\infty \; \text{otherwise} \end{cases}$$

Then we have that we can define the dual problem as:

$$\max_{\lambda \geq 0} -b^T \lambda \; \text{s.t.} \; A^T \lambda = c$$

## Duality and KKT

**Theorem:** Let $x^*$ be a solution of a convex program with convex constraints. Then any solution of the dual problem is also a solution of the primal problem

**Example (with equality constraints only):** Consider the following problem:

$$\begin{cases} \min_{x \in \mathbb{R}^n} \frac{1}{2} x^T Q x + q^T x \\ s.t. \; Cx = d \end{cases}$$

Where $Q$ is a positive definite matrix, $q$ is a vector, $C$ is a matrix and $d$ is a vector.

We can write the Lagrangian function as:

$$L(x, \nu) = \frac{1}{2} x^T Q x + q^T x + \nu^T (Cx - d)$$

$$\nabla_x L(x, \nu) = Qx + q + C^T \nu$$

We want to evaluate at the point $x^*$:

$$\nabla_x L(x^*, \nu) = Qx^* + q + C^T \nu^* = 0$$
$$Cx^* = d$$

If I put a system of equations together I get:

$$\begin{cases} Qx^* + q + C^T \nu^* = 0 \\ Cx^* = d \end{cases}$$

Solving for $x^*$ gives me:

$$x^* = -Q^{-1} (q + C^T \nu^*)$$
$$-CQ^{-1} (q + C^T \nu^*) = d$$

And I can rewrite everything in terms of $\nu^*$:

$$\begin{cases} x^* = -Q^{-1} (q - C^T (CQ^{-1}C^T)^{-1}CQ^{-1}q) \\ \nu^* = -(CQ^{-1}C^T)^{-1}CQ^{-1}q \end{cases}$$

So we started from a complex problem and we ended up with a close form solution. This is a very powerful result because it allows us to solve the problem in a very efficient way.

$$f(x^*) = \frac{1}{2} x^{*T} Q x^* + q^T x^*$$

**Example (with inequality constraints):** Consider the following problem:

$$\begin{cases} \min_{x \in \mathbb{R}^n} \frac{1}{2} x^T Q x + q^T x \\ s.t. \; Cx = d \\Ax \leq b \end{cases}$$

$$\mathcal{L}(x, \lambda, \nu) = \frac{1}{2} x^T Q x + q^T x + \nu^T (Cx - d) + \lambda^T (Ax - b)$$

$$\nabla_x \mathcal{L}(x, \lambda, \nu) = Qx + q + C^T \nu + A^T \lambda$$

If we evaluate at the point $x^*$ we get:

$$\nabla_x \mathcal{L}(x^*, \lambda, \nu) = Qx^* + q + C^T \nu^* + A^T \lambda^* = 0$$

Writing the KKT conditions we get:

$$\begin{cases} Qx^* + q + C^T \nu^* + A^T \lambda^* = 0 \\ Cx^* = d \\ Ax^* \leq b \\ \lambda^* \geq 0 \\ \lambda_i^* (Ax^* - b) = 0 \end{cases}$$

*Note:* In general solving the KKT conditions using an algorithm will be faster than solving the primal problem.
