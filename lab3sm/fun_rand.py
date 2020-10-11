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
