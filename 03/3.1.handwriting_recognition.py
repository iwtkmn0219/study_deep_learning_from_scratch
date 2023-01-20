import sys, os
import numpy as np
from mnist import load_mnist
from PIL import Image
import pickle
from neural_network import sigmoid, softmax

sys.path.append(os.pardir)


def img_show(img: np.ndarray) -> None:
    pil_img = Image.fromarray(np.uint8(img))  # PIL Object
    pil_img.show()


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
    print(x_train.shape, t_train.shape)
    print(x_test.shape, t_test.shape)
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", "rb") as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    B1, B2, B3 = network["b1"], network["b2"], network["b3"]

    A1 = np.dot(x, W1) + B1
    Z1 = sigmoid(A1)
    A2 = np.dot(Z1, W2) + B2
    Z2 = sigmoid(A2)
    A3 = np.dot(Z2, W3) + B3
    Y = softmax(A3)
    return Y


x, t = get_data()
network = init_network()

accuracy_count = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)
    if p == t[i]:
        accuracy_count += 1
print(f"Accuracy: {accuracy_count / len(x)}")
