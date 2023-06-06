import numpy as np
from scipy.stats import poisson
from math import gamma, erf


distributions = ['Normal',
                 'Cauchy',
                 'Laplace',
                 'Poisson',
                 'Uniform']


def sample(distr_type, size):
    if distr_type == 'Normal':
        return np.random.normal(0, 1, size)
    elif distr_type == 'Cauchy':
        return np.random.standard_cauchy(size)
    elif distr_type == 'Laplace':
        return np.random.laplace(0, 1 / np.sqrt(2), size)
    elif distr_type == 'Poisson':
        return np.random.poisson(10, size)
    elif distr_type == 'Uniform':
        return np.random.uniform(-np.sqrt(3), np.sqrt(3), size)
    else:
        print('No such distribution')
        return []


def density_func(distr_type, interval):
    if distr_type == 'Normal':
        return [(1 / np.sqrt(2 * np.pi)) * np.exp(-x ** 2 / 2) for x in interval]
    elif distr_type == 'Cauchy':
        return [(1 / np.pi) * (1 / (1 + x ** 2)) for x in interval]
    elif distr_type == 'Laplace':
        return [(np.sqrt(2) / 4) * np.exp(-1 / np.sqrt(2) * np.fabs(x)) for x in interval]
    elif distr_type == 'Poisson':
        return [10 ** x * np.exp(-10) / gamma(x + 1) for x in interval]
    elif distr_type == 'Uniform':
        return [1 / (2 * np.sqrt(3)) if np.fabs(x) <= np.sqrt(3) else 0 for x in interval]
    else:
        print('No such distribution')
        return []


def distr_func(name, x):
    if name == 'Normal':
        return 0.5 * (1 + erf(x / np.sqrt(2)))
    elif name == 'Cauchy':
        return np.arctan(x) / np.pi + 0.5
    elif name == 'Laplace':
        if x <= 0:
            return 0.5 * np.exp(np.sqrt(2) * x)
        else:
            return 1 - 0.5 * np.exp(-np.sqrt(2) * x)
    elif name == 'Poisson':
        return poisson.cdf(x, 10)
    elif name == 'Uniform':
        if x < -np.sqrt(3):
            return 0
        elif np.fabs(x) <= np.sqrt(3):
            return (x + np.sqrt(3)) / (2 * np.sqrt(3))
        else:
            return 1
    return 0
