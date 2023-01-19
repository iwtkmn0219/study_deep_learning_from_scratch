import numpy as np
import matplotlib.pylab as plt


def step_function(x: np.ndarray) -> np.ndarray:
    y = x > 0
    return y.astype(np.int)


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


def relu(x: np.ndarray) -> np.ndarray:
    return np.maximum(0, x)


x = np.arange(-5, 5, 0.1)
plt.plot(x, step_function(x), x, sigmoid(x), x, relu(x))
plt.ylim(-0.1, 2)
plt.show()
