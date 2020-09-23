import numpy as np
import math


def exp_fun(average, x):
    return 1 - pow(np.exp(1), -(average * x))


def normal_fun(alpha, sigma, x):
    denominator = np.sqrt(sigma) * np.sqrt(2 * np.pi)
    numerator = (np.exp(-pow(x - alpha, 2) / (2 * sigma)))
    val = numerator / denominator
    return val


def dis_fun(alpha, sigma, x):
    return (1 / 2) * (1 + math.erf((x - alpha) / (np.sqrt(sigma) * np.sqrt(2))))
