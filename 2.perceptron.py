def simple_AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    else:
        return 1


ls = [[0, 0], [0, 1], [1, 0], [1, 1]]
print("simple AND")
for value in ls:
    print(value[0], value[1], ">", simple_AND(value[0], value[1]))
