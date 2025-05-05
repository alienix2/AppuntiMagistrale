# Solving problems in the Training of a NN

## Overfitting

In general if we want to have a better predicting model we want to have a high number of layers. In this regard it should also be noted that the trade-off is that the NNs might become easily **overfitted**.

In order to avoid overfitting one of the first things that we can try to use is **regularization**:

- we can add a penalty to the loss function
- discouraging overly complex models
- improving generalization to **unseen data**

## Examples of regularization

- **L1 regularization**: add a penalty equal to the absolute value of the magnitude of coefficients
- **L2 regularization**: add a penalty equal to the square of the magnitude of coefficients
- **Dropout**: randomly set a fraction of input units to 0 at each update during training time, which helps prevent overfitting
- **Early stopping**: stop training when the validation loss starts to increase, even if the training loss is still decreasing
- **Data augmentation**: artificially increase the size of the training dataset by creating modified versions of the single datapoints.

*Note:* the L2 regularization is also called **weight decay**.

### L2 regularization

The training cost is splitted into two parts:

$$J'(\theta) = \frac{1}{N} \sum_{i=1}^{N} ||f_{NN}(x^{(1)}, \theta) - y^{(1)}||^2 + \frac{\rho}{2}||\theta||_2^2 = J(\theta) + \frac{\rho}{2}||\theta||_2^2$$

We compute:

$$\nabla_{\theta} J' = \nabla_{\theta} J(\theta) + \frac{\rho}{2} \nabla_{\theta} ||\theta||_2^2 = \nabla_{\theta} J(\theta) + \rho \theta$$

This means that every gradient-based update will read as:

$$\theta^{k+1} = \theta^k - \alpha (\nabla_{\theta} J'(\theta^k) = (1 - \alpha \rho) \theta^k - \alpha \nabla_{\theta} J(\theta^k)$$

All the weights are scaled down based on their own magnitude so the larger weights will be subjected to a higher degree of penalization.

NNs with lower weights usually tend to have better generalization properties.

### L1 regularization

The training cost is splitted into two parts:

$$J'(\theta) = J(\theta) + \rho ||\theta||_1$$

We compute:

$$\nabla_{\theta} J' = \nabla_{\theta} J(\theta) + \rho \nabla_{\theta} ||\theta||_1 = \nabla_{\theta} J(\theta) + \rho \text{sign}(\theta)$$

This means that every gradient-based update will read as:

$$\theta^{k+1} = \theta^k - \alpha (\nabla_{\theta} J'(\theta^k) = \theta^k - \alpha \nabla_{\theta} J(\theta^k) - \alpha \rho \text{sign}(\theta^k)$$

In this case we are subtracting or adding a constant amount that is determined by the sign of the weight and the value of the regularization parameter.

This can easily create **sparse NNs** meaning that the small weights will rapidly become zero and the NN will be forced to use only a small number of weights.

## Use in dynamical systems

The NN is useful if we don't know the physical model or if the model is too complex to be derived.

We want to train a NN s.t: $x(k+1) \approx f(x(k), u(k))$.

We give an input of the current state/output and an input of the current control input and we want to predict the next state/output.

*Example:*

We want to learn the system:

$$x(k+1) = \begin{bmatrix} x_1(k) + x_2^2(k) + 0.3u(k) \\ sin(x_1(k)) + 0.5x_2(k) + 2u(k) \end{bmatrix}$$

What we usually do is integrate some kind of **noise** so that the NN can actually learn to understand how to use data produced by a real sensor.

We use a ReLU activation function with $L=3$ layers and $N=2$ neurons in each layer.

*Note:* check the slides for Matlab code.
