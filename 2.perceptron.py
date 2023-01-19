import numpy as np

def simple_AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    else:
        return 1
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.2, 0.2])
    b = -0.1
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1


ls = [[0, 0], [0, 1], [1, 0], [1, 1]]
print("simple AND")
for value in ls:
    print(value[0], value[1], ">", simple_AND(value[0], value[1]))
print("AND")
for value in ls:
    print(value[0], value[1], ">", AND(value[0], value[1]))
print("NAND")
for value in ls:
    print(value[0], value[1], ">", NAND(value[0], value[1]))
print("OR")
for value in ls:
    print(value[0], value[1], ">", OR(value[0], value[1]))
