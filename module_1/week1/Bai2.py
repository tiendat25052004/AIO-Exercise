import math


def is_number(s):
    try:
        float(s)
    except ValueError:
        return False
    return True


def sigmoid(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def relu(x: float) -> float:
    return max(0, x)


def elu(x: float, alpha = 0.01) -> float:
    if x > 0:
        return x
    return alpha * (math.exp(x) - 1)


def exercise2():
    x = input("Input x: ")
    if not is_number(x):
        print("x must be a number")
        return
    x = float(x)
    name_func = input("Input activation Function (sigmoid|relu|elu): ")
    if name_func not in ['sigmoid', 'relu', 'elu']:
        print(f"{name_func} is not supported")
        return
    if name_func == 'sigmoid':
        print(f"sigmoid: f({x}) = {sigmoid(x)}")
    elif name_func == 'relu':
        print(f"relu: f({x}) = {relu(x)}")
    else:
        print(f"elu: f({x}) = {elu(x)}")
