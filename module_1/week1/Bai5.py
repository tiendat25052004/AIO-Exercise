import math


def md_nre_single_sample(y: list, y_hat: list, n, p):
    if type(y) == int or type(y) == float:
        y = [y]
    if type(y_hat) == int or type(y_hat) == float:
        y_hat = [y_hat]
    MD_nRE = 0
    m = len(y)
    for i in range(m):
        MD_nRE += pow(pow(y[i], 1/n) - pow(y_hat[i], 1/n), p)
    return MD_nRE / m
