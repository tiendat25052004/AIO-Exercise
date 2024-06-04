import math


def approx_sin(x: float, n: int) -> float:
    result = 0.0
    sign = 1
    for i in range(0, n+1):
        result += sign * x**(2*i+1) / math.factorial(2*i+1)
        sign *= -1
    return result


def approx_cos(x: float, n: int) -> float:
    result = 0.0
    sign = 1
    for i in range(0, n+1):
        result += sign * x**(2*i) / math.factorial(2*i)
        sign *= -1
    return result


def approx_sinh(x: float, n: int) -> float:
    result = 0.0
    for i in range(0, n+1):
        result += x**(2*i+1) / math.factorial(2*i+1)
    return result


def approx_cosh(x: float, n: int) -> float:
    result = 0.0
    for i in range(0, n+1):
        result += x**(2*i) / math.factorial(2*i)
    return result


def main():
    x = input("Enter x: ")
    try:
        x = float(x)
    except ValueError:
        print("Invalid input")
        return
    n = input("Enter n: ")
    try:
        n = int(n)
    except ValueError:
        print("Invalid input")
        return
    print(f"approx_sin({x}, {n}) = {approx_sin(x, n)}")
    print(f"approx_cos({x}, {n}) = {approx_cos(x, n)}")
    print(f"approx_sinh({x}, {n}) = {approx_sinh(x, n)}")
    print(f"approx_cosh({x}, {n}) = {approx_cosh(x, n)}")
    return


if __name__ == "__main__":
    main()
