#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import get_input, benchmark
import numpy as np


def floodfill(matrix, i, j):
    filled = 0
    # "hidden" stop clause - not reinvoking for "c" or "b", only for "a".
    if matrix[i, j] < 9:
        matrix[i, j] = 10
        filled += 1
        # recursively invoke flood fill on all surrounding cells:
        if i > 0:
            filled += floodfill(matrix, i-1, j)
        if i < len(matrix) - 1:
            filled += floodfill(matrix, i+1, j)
        if j > 0:
            filled += floodfill(matrix, i, j-1)
        if j < len(matrix[i]) - 1:
            filled += floodfill(matrix, i, j+1)
    return filled


def neighbours(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1, j))
    if i+1 < m:
        adjacent_indices.append((i+1, j))
    if j > 0:
        adjacent_indices.append((i, j-1))
    if j+1 < n:
        adjacent_indices.append((i, j+1))
    return adjacent_indices


@benchmark
def smoke_basin(data, find_biggest=False):
    d = np.array(data)
    risk = 0
    sizes = []
    for i in range(len(d)):
        for j in range(len(d[0])):
            e = d[i, j]
            indices = neighbours(i, j, *d.shape)
            is_basin = np.all(
                [True if e < d[i[0], i[1]] else False for i in indices])
            if find_biggest and is_basin:
                sizes.append(floodfill(d, i, j))
            elif is_basin:
                risk += (d[i, j] + 1)
    result = np.prod(sorted(sizes, reverse=True)[:3]) if find_biggest else risk
    return result


input_ = list(map(lambda x: list(map(int, list(x))), get_input()))

print(f"Part 1: {smoke_basin(input_)}")
print(f"Part 2: {smoke_basin(input_, find_biggest=True)}")
