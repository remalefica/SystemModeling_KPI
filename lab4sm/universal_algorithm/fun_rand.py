import random
import math


# Generates a random value according to an exponential distribution
# @param timeMean mean value
# @return a random value according to an exponential distribution

def exp(time_mean):
    a = 0.0
    while a == 0:
        a = random.random()
    a = -time_mean * math.log(a)
    return a


# Generates a random value according to a uniform distribution
# @param timeMin
# @param timeMax
# @return a random value according to a uniform distribution

def unif(time_min, time_max):
    a = 0.0
    while a == 0:
        a = random.random()
    a = time_min + a * (time_max - time_min)
    return a


# Generates a random value according to a normal (Gauss) distribution
# @param timeMean
# @param timeDeviation
# @return a random value according to a normal (Gauss) distribution

def norm(time_mean, time_deviation):
    return time_mean + time_deviation * random.gauss(0.0, 1.0)


def erlang(time_mean, k):
    a = 1
    for i in range(k):
        a *= random.random()
    return -math.log(a)/(k/time_mean)


def empirical(x, y):
    n = len(x)
    # throw exception and stop the program if maximum of y array is bigger than 1.0
    if y[n - 1] != 1.0:
        raise Exception('The array of points from empiric distribution is incorrect')

    r = random.random()
    for i in range(1, n-1):
        if y[i - 1] < r <= y[i]:
            a = x[i - 1] + (r - y[i - 1]) * (x[i] - x[i - 1]) / (y[i] - y[i - 1])
            return a

    a = x[n - 2] + (r - y[n - 2]) * (x[n - 1] - x[n - 2]) / (y[n - 1] - y[n - 2])
    if a < 0:
        raise Exception('Negative time delay is generated: check parameters for time delay')
    return a
