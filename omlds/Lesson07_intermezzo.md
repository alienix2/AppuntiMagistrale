# Intermezzo: Convex optimization

## Basic definition of optimization

The definition of **optimization** can be obtained by looking at a real world example. For instance if we look at an electrical car we can theorize that:

- Speed is the optimization/decision parameter
- Fuel consumption is the cost function to minimize
- Engine type, chassis shape, gear etc. are the parameters that allow to solve the decision-making problem

If we have a graph that shows the relationship between fuel consumption and the speed we can easily find which is the optimal speed to minimize the fuel consumption.

Then we can impose some **constraint** that can limit the possibilities that we have in order to solve our problem.

## General form of an optimization problem

$$\begin{cases} min f(x) \\ s.t. \; g(x) \leq 0 \\ h(x) = 0 \end{cases}$$

Where:

- $x = (x_1, x_2, \ldots, x_n)^T$ is the vector of decision variables
- $f(x)$ is the objective function to minimize
- $g(x)$ is the vector of inequality constraints
- $h(x)$ is the vector of equality constraints

*Note:* $g(x)$ and $h(x)$ are functions that map the decision variables to the constraints. The constraints can be linear or non-linear, depending on the problem.

We define the **feasible set** as the set of all points that satisfy the constraints. The feasible set is defined as:

$$\mathcal{X} = \{x \in \mathbb{R}^n | g(x) \leq 0, h(x) = 0\}$$

An **optimizer** is a point in the feasible set that minimizes the objective function. The set of all optimizers is called the **optimal set** and is defined as:

$$\mathcal{X}^* = \{x^* \in \mathcal{X} | f(x^*) \leq f(x) \; \forall x \in \mathcal{X}\}$$

The **optimal value** is the minimum value of the objective function over the feasible set:

$$f^* = \min_{x \in \mathcal{X}} f(x)$$

### Things to always note

- Any optimization problem can be transformed into a minimization problem. For instance, if we want to maximize a function $f(x)$ we can minimize $-f(x)$.
- **Scaling** the objective function does not change the optimal solution. For instance, if we want to minimize $f(x)$ we can minimize $k f(x)$ where $k$ is a positive constant. Same goes for the inequality constraints. For instance, if we want to minimize $f(x)$ subject to $g(x) \leq 0$ we can minimize $k f(x)$ subject to $k g(x) \leq 0$ where $k$ is a positive constant. *Note:* This is not true for equality constraints.
- **Shifting** the objective function does not change the optimal solution. For instance, if we want to minimize $f(x)$ we can minimize $f(x) + c$ where $c$ is a constant. Same goes for equality constraints.
- Adding constraints to the problem can only make the objective function worse or equal to the original one.
- Strict inequalities can be approximated into non-strict inequalities. For instance, if we want to minimize $f(x)$ subject to $g(x) < 0$ we can minimize $f(x)$ subject to $g(x) \leq -\epsilon$ where $\epsilon$ is a small positive constant.

### Feasibility

Given a $x \in \mathcal{X}$ we say that $x$ is **feasible** $\iff x \in \mathcal{X}$.

If $\mathcal{X}$ is empty we say that the problem is **infeasible**. If $\mathcal{X}$ is not empty we say that the problem is **feasible**.

A problem is called **unbuonded** if $\forall M > 0 \; \exists x \in \mathcal{X} \; s.t. \; f(x) < -M$. In this case we have that $\min_{x \in \mathcal{X}} f(x) = -\infty$.

We can define **local** and **global** solutions:

- A point $x^* \in \mathcal{X}$ is a **local optimizer** of the problem if $x \in \mathcal{X}$ and $f(x^*) \leq f(x)$ for all $x$ in $\mathcal{X}$ in a neighborhood of $x^*$.
- A point $x^* \in \mathcal{X}$ is a **strict global optimizer** of the problem if $f(x^*) < f(x)$ for all $x \in \mathcal{X}$.
- A point $x^* \in \mathcal{X}$ is a **global optimizer** of the problem if $f(x^*) \leq f(x)$ for all $x \in \mathcal{X}$.

### Convex optimization

In this case we will consider only the case of convex optimization problems. A problem is called **convex** if:

- The objective function $f(x)$ is a convex function.
- The feasible set $\mathcal{X}$ is a convex set.

These problems are particularly relevant for a few reasons:

- **Local** and **global** solutions are the same. This means that if we find a local solution we can be sure that it is also a global solution.
- Efficient solution algorithms are available
- They are very common in control engineering.

#### Convex set and convex function

A set $S \subseteq \mathbb{R}^n$ is called **convex** if $\forall x, y \in S$ and $\forall \lambda \in [0, 1]$ we have that:

$$\lambda x + (1 - \lambda) y \in S$$

A function $f: \mathcal{X} \to \mathbb{R}$ is called **convex** if $\mathcal{X}$ is convex and $\forall x, y \in \mathcal{X}$ and $\forall \lambda \in [0, 1]$ we have that:

$$f(\lambda x + (1 - \lambda) y) \leq \lambda f(x) + (1 - \lambda) f(y)$$

### Optimality conditions for constrained problems

$$\begin{cases} min f(x) \\ s.t. \; g_i(x) \leq 0 \\ h_j(x) = 0 \end{cases}$$

With $i \in \mathbb{I}$ and $j \in \mathbb{J}$

A specific $i \in \mathbb{I}$ is called **active** at $x$ if $g_i(x) = 0$ and **inactive** if $g_i(x) < 0$.

### Karush-Kuhn-Tucker (KKT) conditions

The KKT conditions are a set of necessary conditions for a solution to be optimal for a constrained optimization problem. They are given by:

$$\begin{cases} \nabla f(x^*) + \sum_{i \in \mathbb{I}} \lambda_i^* \nabla g_i(x^*) + \sum_{j \in \mathbb{J}} \mu_j^* \nabla h_j(x^*) = 0 \\ g_i(x^*) \leq 0 \\ h_j(x^*) = 0 \\ \lambda_i^* g_i(x^*) = 0 \\ \lambda_i^* \geq 0 \\ i \in \mathbb{I} \\ j \in \mathbb{J} \end{cases}$$

Where:

- $x^*$ is the optimal solution
- $\lambda_i^*$ are the Lagrange multipliers for the inequality constraints
- $\mu_j^*$ are the Lagrange multipliers for the equality constraints
- $\nabla f(x^*)$ is the gradient of the objective function at the optimal solution
- $\nabla g_i(x^*)$ is the gradient of the $i$-th inequality constraint at the optimal solution
- $\nabla h_j(x^*)$ is the gradient of the $j$-th equality constraint at the optimal solution
- $g_i(x^*)$ is the value of the $i$-th inequality constraint at the optimal solution
- $h_j(x^*)$ is the value of the $j$-th equality constraint at the optimal solution
- $\lambda_i^* g_i(x^*) = 0$ is called the **complementary slackness** condition. It states that if the $i$-th inequality constraint is active at the optimal solution then the corresponding Lagrange multiplier must be positive. If the $i$-th inequality constraint is inactive at the optimal solution then the corresponding Lagrange multiplier must be zero.
- $\lambda_i^* \geq 0$ is called the **non-negativity** condition. It states that the Lagrange multipliers for the inequality constraints must be non-negative.
- $i \in \mathbb{I}$ and $j \in \mathbb{J}$ are the indices of the inequality and equality constraints respectively.

*Note:* The KKT conditions are necessary for optimality, but not sufficient. This means that if a point satisfies the KKT conditions then it is a candidate for being an optimal solution, but it is not guaranteed to be an optimal solution. In order to guarantee that a point is an optimal solution we need to check the second-order conditions.

**What does that mean:**

We consider the following optimization problem:

$$\begin{cases} min f(x) \\ s.t. \; g_i(x) \leq 0 \; \forall i \in {1, \ldots, m} \end{cases}$$

We call the **active set** a subset of the constraints that put some $g_i(x) = 0$.

We define the **Lagrangian** function as:

$$L(x, \lambda) = f(x) + \sum_{i \in \mathbb{I}} \lambda_i g_i(x)$$

Moreover we define the **Lagrange multipliers** as the vector $\lambda = (\lambda_1, \ldots, \lambda_m)^T$.

*Note:* for completeness we should also add the equality constraints to the Lagrangian function, but we will not do that here. The reason is that they are always satisfied. (More on this later)

We want to find $(x^*, \lambda^*)$ such that:

$$KKT: \begin{cases} \nabla_x L(x^*, \lambda^*) = 0 \\ g_i(x^*) \leq 0 \; \forall i \in {1, \ldots, m} \\ \lambda_i^* g_i(x^*) = 0 \; \forall i \in {1, \ldots, m} \\ \lambda_i^* \geq 0 \; \forall i \in {1, \ldots, m} \end{cases}$$

Where $S$ is the feasible set.

*Note:* in a convex setting these conditions are both necessary and sufficient.

*Note:* The Lagrangian multipliers can be seen as the **penalty** that you get for not having the $g_i(x^*) = 0$

#### Geometrically

Check the slides for a graphical representation of the KKT conditions.
