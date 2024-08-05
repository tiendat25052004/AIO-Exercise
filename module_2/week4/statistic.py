import numpy as np


def compute_mean(X):
    return np.mean(X)


X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
print(" Mean : ", compute_mean(X))


def compute_median(X):
    size = len(X)
    X = np.sort(X)
    print(X)
    if size % 2 == 0:
        return (X[size // 2 - 1] + X[size // 2]) / 2
    else:
        return X[size // 2]


X = [1, 5, 4, 4, 9, 13]
print(" Median : ", compute_median(X))


def compute_std(X):
    mean = np.mean(X)
    variance = 0
    for i in X:
        variance += (i - mean) ** 2
    return np.sqrt(variance/len(X))


X = [171, 176, 155, 167, 169, 182]
print(" Standard deviation : ", compute_std(X))


def compute_correlation_cofficient(X, Y):
    N = len(X)
    numerator = N * np.sum(X * Y) - np.sum(X) * np.sum(Y)
    denominator = np.sqrt((N * np.sum(X ** 2) - np.sum(X) ** 2)
                          * (N * np.sum(Y ** 2) - np.sum(Y) ** 2))
    return np.round(numerator / denominator, 2)


X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
Y = np.asarray([4, 25, 121, 36, 16, 225, 81])
print(" Correlation : ", compute_correlation_cofficient(X, Y))
