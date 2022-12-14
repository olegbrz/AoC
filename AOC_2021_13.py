#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Tuple, Union
from aoc_helper import get_input, benchmark
import numpy as np
import matplotlib.pyplot as plt


def parse_data(data: List[str]) -> Tuple[List[List], List[str]]:
    points = [[int(i.split(",")[0]), int(i.split(",")[1])]
              for i in data[:data.index("")]]
    instructions = data[data.index("")+1:]

    return points, instructions


def fold_grid(grid: np.array, along: str, value: int) -> np.array:
    if along == "y":
        grid, folding = grid[:value, ], grid[value+1:, ]
        folding = np.flip(folding, axis=0)
    elif along == "x":
        grid, folding = grid[:, :value], grid[:, value+1:]
        folding = np.flip(folding, axis=1)
    return grid + folding


def grid_to_string(grid: np.array) -> str:
    str_representation = '\n'
    for i in range(len(grid)):
        str_representation += ' '
        for j in range(len(grid[0])):
            if grid[i, j]:
                str_representation += '█'
            else:
                str_representation += ' '
        str_representation += '\n'
    return str_representation


@benchmark
def compute_dots(data: List[str], first_only: bool = True) -> Union[int, str]:
    points, instructions = parse_data(data)
    x_max, y_max = max([i[0] for i in points]), max([i[1] for i in points])

    grid = np.zeros((y_max+1, x_max+1), dtype=np.bool)
    for point in points:
        x, y = point
        grid[y, x] = 1
    if first_only:
        instructions = [instructions[0]]
    for instruction in instructions:
        fold = instruction.split()[-1]
        axis, value = fold.split("=")
        value = int(value)
        grid = fold_grid(grid, axis, value)
    if not first_only:
        return grid_to_string(grid)
    else:
        return len(grid[grid == True])


input_ = get_input()

print(f"Part 1: {compute_dots(input_)}")
print(f"Part 2:\n{compute_dots(input_, False)}")
