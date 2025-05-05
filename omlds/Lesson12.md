# Neural networks

## Regression problems for dynamical systems

The discipline that derives dynamical rules $f: \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}^n$ and $h: \mathbb{R}^n \times \mathbb{R}^m \to \mathbb{R}^l$ is called **system identification**.

If we aren't able to exploit physical laws, system models are obtained in a **data-driven** fashion:

1. Design control signal(s) and inject them into the system
2. Collect state/output trajectory
3. Choose parametrization for $f$ and $h$
4. Adjust the parameter for the best input-output fit

Uno degli approcci più usati oggigiorno è quello di usare una rete neurale.

Una cosa da notare è che spesso i controller NL (come gli MPC) funzionano molto meglio di quelli lineari, tuttavia richiedono di risolvere dei problemi di ottimizzazione e di conseguenza non è banale riuscire a risolvere velocemente i sistemi in questione.

L'idea finale è quindi quella di creare una NN surrogata con valutazioni poco costose:

1. Si disegna un certo controllore NL ($k(x)$)
2. Si produce offline input-output data ($x^i$, $k(x^i)$)
3. Si addestra una NN per approssimare $k(x)$

*Nota:* Vedi le slide per un piccolo excursus su come funzionano vagamente i neuroni nel cervello e come la loro struttura si può traslare in una NN.

## Neural network

A neural network is just a parametric, possibly nonlinear, mappung between an input space $\mathbb{R}^n$ and an output space $\mathbb{R}^m$.

### Perceptron

A perceptron can be seen a single neruon with only 1 layer that is the output. We can consider a set of constant each of which has a weight. They are passed through a weighted sum and then through a step function (activation function) to get an ouput.

An activation function $g: \mathbb{R} \to \mathbb{R}$ is called a **step function** if:

$$
g(x) = \begin{cases}
    0 & \text{if } x < 0 \\
    1 & \text{if } x \geq 0
\end{cases}
$$

The **NN width** is given by the number of neurons in parallel and the **NN lenght** is given by the layers of neuron that are in cascade. (*Note:* when we have multiple layers of neurons in cascade we talk about **deep learning**)

*Example:*

We consider a NN with 3 inputs, two hidden layers with 4 neurons each and 1 output. We can count the parameters to learn in this NN as:

- Input layer: $3 \cdot 4 + 4 = 12 + 4 = 16$
- Hidden layer 1: $4 \cdot 4 + 4 = 16 + 4 = 20$
- Hidden layer 2: $4 \cdot 1 + 1 = 4 + 1 = 5$
- Total: $16 + 20 + 5 = 41$ weights in total

*Example 2:* Check the slides for the image of the NN and the explanation on how is the sigmoid applied.

Basically the NNs are just functions chained together. If we keep the activation function linear we can easily calculate our output as linear.

The point is that we can use **non-linear** activation functions to be a lot more **expressive**.

A NN with one hidden layer can approximate any function with arbitrary precision. There are some technical conditions to address even in this condition. For example: the function must be continuous and we need to define the arbitrary precision that we actually want to use.

### Activation functions

The three most popular ones are:

- **Sigmoid**: $g(x) = \frac{1}{1 + e^{-x}}$
- **Tanh**: $g(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$
- **ReLU**: $g(x) = \max(0, x)$

Changing the NN weights changes the shape curvature of the function while changing the biases shifts the position of the function.

### Technical properties of NNs

An NN with L +1 layers and index set $L = \{0, 1, \ldots, L\}$ is a function $f: \mathbb{R}^n \times \mathbb{R}^p\to \mathbb{R}^m$ can be written in **vector form** as:

$$ \begin{cases} x^0 = x \\ x^{i+1} = g_i(W_i x^i + b_i) \end{cases}$$

Where $W_i$ are the weights and $b_i$ are the biases. The function $g_i$ is the activation function of the layer $i$.

#### Sigmoid

The sigmoid produces an output in (0,1) which is great for scenarios were one need to measure probabilities, it's continuously differentiable and smooth which means that the derivative can be always calculated.

One of the main issues is that it's not zero centered. This means that it's biased towards one direction and this might impact the NN ability. This means that it's subject to the **vanishing gradient** problem and it's therefore unsuitable for very deep NNs.

#### Tanh

The hyperbolic tangent is very similar to the sigmoid.

One of the main advantage is that this function is actually zero centered.

#### ReLU

The ReLU produces an output in (0, +inf). It can be evaluated faster and it has been proven that training ReLU networks can be much faster than sigmoid or tanh. It's not subject to the vanishing gradient and it's zero centered.

One of the main issues is that it may suffer from the **dying ReLU** problem. This means that some neurons may become inactive and stop learning. This is because the gradient is zero for negative values. This problem can be solved by using some variations of the ReLU (e.g. Leaky ReLU, softmax)

This means that you actually get a sparse pattern of activation as not all the neurons will be active at once.
