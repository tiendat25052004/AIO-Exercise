import math
import random


def MAE(y_target: list, y_pred: list) -> float:
    sum = 0
    for i in range(len(y_target)):
        sum += abs(y_target[i] - y_pred[i])
    return sum / len(y_target)


def MSE(y_target: list, y_pred: list) -> float:
    sum = 0
    for i in range(len(y_target)):
        sum += (y_target[i] - y_pred[i])**2
    return sum / len(y_target)


def RMSE(y_target: list, y_pred: list) -> float:
    return math.sqrt(MSE(y_target, y_pred))


def exercise3():
    num_samples = input(
        "Input number of samples (integer number) which are generated: ")
    if not num_samples.isnumeric():
        print("Number of samples must be an integer number")
        return
    num_samples = int(num_samples)
    loss = input("Input loss function (MAE|MSE|RMSE): ")
    if loss not in ['MAE', 'MSE', 'RMSE']:
        print(f"{loss} is not supported")
        return
    list_y_target = []
    list_y_pred = []
    if loss == 'MAE':
        for i in range(num_samples):
            y_pred = random.uniform(0, 10)
            y_target = random.uniform(0, 10)
            print(
                f"loss name: {loss}, y_target: {y_target}, y_pred: {y_pred}, loss: {MAE([y_target], [y_pred])}")
            list_y_target.append(y_target)
            list_y_pred.append(y_pred)
        print(f"final loss: {MAE(list_y_target, list_y_pred)}")
    elif loss == 'MSE':
        for i in range(num_samples):
            y_pred = random.uniform(0, 10)
            y_target = random.uniform(0, 10)
            print(
                f"loss name: {loss}, y_target: {y_target}, y_pred: {y_pred}, loss: {MSE([y_target], [y_pred])}")
            list_y_target.append(y_target)
            list_y_pred.append(y_pred)
        print(f"final loss: {MSE(list_y_target, list_y_pred)}")
    else:
        for i in range(num_samples):
            y_pred = random.uniform(0, 10)
            y_target = random.uniform(0, 10)
            print(
                f"loss name: {loss}, y_target: {y_target}, y_pred: {y_pred}, loss: {RMSE([y_target], [y_pred])}")
            list_y_target.append(y_target)
            list_y_pred.append(y_pred)
        print(f"final loss: {RMSE(list_y_target, list_y_pred)}")
