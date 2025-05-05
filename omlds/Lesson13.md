# Learning in RNNs

## Basics

Given some input data $(x^{(i)}, y^{(i)})$ which constitute the dataset $D=\{(x^{(i)}, y^{(i)})\}_{i=1}^m$, we want to find a value $\Theta^*$ such that the following cost function is minimized:

$$
\Theta^* = \arg\min_\Theta \in \mathbb{R}^p \frac{1}{m} \sum_{i=1}^m l(f_{NN}(x^{(i)}; \Theta), y^{(i)}) + \rho r(\Theta)
$$

A very common function that is chosen to be minimized is the mean squared error (MSE):

$$
l(f_{NN}(x^{(i)}; \Theta), y^{(i)}) = ||f_{NN}(x^{(i)}; \Theta) - y^{(i)}||^2 \rightarrow\\
J(\Theta) = \frac{1}{m} \sum_{i=1}^m ||f_{NN}(x^{(i)}; \Theta) - y^{(i)}||^2
$$

The **goal** is to find the optimal parameters $\Theta^*$ that minimize the cost function ($\nabla_{\Theta}J(\Theta^*) = 0$)

One of the main issues of this approach is that the function might be not convex. What we can always do is to compute the gradient at a specific point and that will give us information on the direction to go by looking at how fast the function is changing.

*Example:* Perceptron learning rule

$$f_{NN}: \mathbb{R}^n \times \mathbb{R}^n+1 \rightarrow \mathbb{R}$$
I consider the case $n=2$

$$ z = w_0 + w_1 x_1 + w_2 x_2 = 0$$
$$x_2 = \frac{-w_1}{w_2} x_1 - \frac{w_0}{w_2}$$

This represents a line and allows us to identify two region on the plane. The first one is the "positives" in respect to the line and the second one is the "negatives" in respect to the line.

When I train a Perceptron I divide the dataset in two classes and I want to find the line that separate the two classes. In this regard the Perception is also defined as a **classifier** as it allows to classify into these two classes of points (two regions of the plane)

The main issue is that the function is not differentiable and therefore it's not so easy to understand if a point is one side or the other, moreover there is a discontinuity point in 0.

The Perceptron learning rule is a supervised learning algorithm for binary classifiers. It is based on the idea of adjusting the weights of the model based on the errors made during predictions. The algorithm iteratively updates the weights to minimize the classification error.

I start from a value and I try to find the optimal one:

$$
\Theta^k+1 = \Theta^k - \eta (y^{(i)} - g(\Theta^k \begin{bmatrix} x^{(i)} \\ 1 \end{bmatrix})) \begin{bmatrix} x^{(i)} \\ 1 \end{bmatrix}, \eta > 0
$$

If the output is correct then I don't update the weights, otherwise I update them.

**Theorem:** If there exists a set of weights $\Theta^*$ that is consistent with the training data the perceptron learning algorithms guarantees that $\Theta^k \rightarrow \Theta^*$

## Gradient based information

The most common algorithm that is used for unconstrained problems is the **gradient descent**:

$$ \forall k \in \mathbb{N} \; \Theta^{k+1} = \Theta^k - \eta \nabla_\Theta J(\Theta^k)$$
  
Where $\eta$ is the learning rate.

The only issues in this method are the fact that it might need to be run multiple times and also for many different initial starting values for $\Theta^0$. This computation is very onerous because we need to evaluate the gradient.

For this reason one of the most common approach is to use the **stochastic gradient descent** (SGD) which is a variant:

$$\Theta^{k+1} = \Theta^k - \eta \nabla_\Theta J(\Theta^k, x^{(i)}, y^{(i)})$$
  
Basically what you do is picking one sample from the dataset and compute the gradient on that sample.

## Backpropagation example

The backpropagation is a methodology to compute the gradient of the cost function with respect to the parameters of the model.

The idea is to propagate the errors backwards through the NN. It should be used in conjunction with an iterative procedure based on the gradient descent to update $\Theta$

*Example:*  
Given an input $x \in \mathbb{R}^n$ and a target $y \in \mathbb{R}^m$

We start given some $\Theta$:

$$ y_{NN} = f_{NN}(wx + b) = g(wx + b), \; w=[w_1, w_2, \ldots, w_n]$$
$$ g(z) = \frac{1}{1+e^{-z}}$$

$$x^{(i)} \Rightarrow y_{NN}^{(i)} = g(wx^{(i)} + b)$$

$$J(\Theta) = (g(wx^{(i)} + b) - y^{(i)})^2$$

$$\nabla_\Theta J(\Theta) = \begin{bmatrix} \frac{\partial J}{\partial w_1} \\ \frac{\partial J}{\partial w_2} \\ \vdots \\ \frac{\partial J}{\partial b} \end{bmatrix}$$

To calculate a generic gradient we use the **chain rule**:
$$\frac{\partial J}{\partial w_j} = \frac{\partial J}{\partial y_{NN}} \frac{\partial y_{NN}}{\partial z} \frac{\partial z}{\partial w_j}$$

Where $z = wx + b$ and $y_{NN} = g(z)$

$$\frac{\partial J}{\partial y_{NN}} = 2(y_{NN} - y^{(i)})$$
$$\frac{\partial y_{NN}}{\partial z} = g(z)(1-g(z))$$

*Note:* this is the derivative of the sigmoid function: ($g'(z) = g(z)(1-g(z))$)
$$\frac{\partial z}{\partial w_j} = x_j$$

*Note:* this is because I'm doing the derivative of a sum where only one element is different from 0 and that is the $ x_j$.

$$\frac{\partial J}{\partial w_j} = 2(y_{NN} - y^{(i)}) y_{NN}(1-y_{NN}) x_j$$

If I compute this for all the elements what I get is:

$$\nabla_\Theta J(\Theta) = \begin{bmatrix} 2(y_{NN} - y^{(i)}) y_{NN}(1-y_{NN}) x_1 \\ 2(y_{NN} - y^{(i)}) y_{NN}(1-y_{NN}) x_2 \\ \vdots \\ 2(y_{NN} - y^{(i)}) y_{NN}(1-y_{NN}) b \end{bmatrix}$$
*Note:* this is because the only part that is changing is the last one.

### In the hidden layers

In the hidden layer I don't have a target output value. What I can do is to compute how much each neuron contributed to the downstream error:

I consider taking the input: $z_i = \sum_{j=1}^n w_{ij} a_j$

$$\frac{\partial J}{\partial z_i} = \sum_{j=1}^n \frac{\partial J}{\partial a_j} \frac{\partial a_j}{\partial z_i}$$

Where $a_j$ is the output of the neuron $j$ and $z_i$ is the input of the neuron $i$.

I can compute the **backpropagation formula**:

$$\delta_i = \frac{\partial J}{\partial z_i} = \frac{\partial g(z_i)}{\partial z_i} \sum_{j=1}^n \frac{\partial J}{\partial a_j} \frac{\partial a_j}{\partial z_i} = g'(z_i) \sum_{j=1}^n w_{ij} \delta_j$$

And the algorithm for the **error backpropagation** is:

1. Evaluate $\delta$ for all the outputs
2. Propagate the error backwards through the network
3. Update the weights using the computed $\delta$ values

With a dataset D: repeat the above for each of the samples in the dataset.

*Example:* (check the slides)
