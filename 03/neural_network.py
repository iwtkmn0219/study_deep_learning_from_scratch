import numpy as np
import matplotlib.pylab as plt


def step_function(x: np.ndarray) -> np.ndarray:
    y = x > 0
    return y.astype(np.int)


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


def relu(x: np.ndarray) -> np.ndarray:
    return np.maximum(0, x)


def identity_function(x: np.ndarray) -> np.ndarray:
    return x


def init_network() -> dict:
    network = {
        "W1": np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]),
        "B1": np.array([0.1, 0.2, 0.3]),
        "W2": np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]),
        "B2": np.array([0.1, 0.2]),
        "W3": np.array([[0.1, 0.3], [0.2, 0.4]]),
        "B3": np.array([0.1, 0.2]),
    }
    return network


def forward(network: dict, x: np.ndarray) -> np.ndarray:
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    B1, B2, B3 = network["B1"], network["B2"], network["B3"]

    A1 = np.dot(X, W1) + B1
    Z1 = sigmoid(A1)
    A2 = np.dot(Z1, W2) + B2
    Z2 = sigmoid(A2)
    A3 = np.dot(Z2, W3) + B3
    Y = identity_function(A3)
    return Y


network = init_network()
X = np.array([1.0, 0.5])
Y = forward(network, X)
print(Y)


def softmax(a: np.ndarray) -> np.ndarray:
    c = np.max(a)
    exp_a = np.exp(a - c)
    return exp_a / np.sum(exp_a)
