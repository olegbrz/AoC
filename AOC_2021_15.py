#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from requests.api import get
from aoc_helper import get_input, benchmark
import numpy as np
import sys


def min_cost(cost, m, n):
    if (n < 0 or m < 0):
        return sys.maxsize
    elif (m == 0 and n == 0):
        return cost[m][n]
    else:
        return cost[m][n] + min(min_cost(cost, m-1, n-1),
                                min_cost(cost, m-1, n),
                                min_cost(cost, m, n-1))


def min(x, y, z):
    if (x < y):
        return x if (x < z) else z
    else:
        return y if (y < z) else z


input_ = get_input()
input_ = np.array([list(map(int, list(i))) for i in input_])

# input_ = [[1, 2, 3],
#           [4, 8, 2],
#           [1, 5, 3]]

print(min_cost(input_, 99, 99))
