#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Tuple
from aoc_helper import get_input, benchmark
import numpy as np


def neighbours(i: int, j: int, m: int, n: int) -> List[Tuple[int, int]]:
    adjacent_indices = []
    for k in [i-1, i, i+1]:
        for l in [j-1, j, j+1]:
            if 0 <= k < m and 0 <= l < n and (k != i or l != j):
                adjacent_indices.append((k, l))
    return adjacent_indices


def update_energy(grid: np.array) -> np.array:
    has_flashed = np.zeros(shape=(grid.shape), dtype=np.bool)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i, j] += 1
            if grid[i, j] > 9:
                has_flashed[i, j] = True
    return has_flashed


def update_flashes(grid: np.array, has_flashed: np.array) -> int:
    n_of_flashes = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i, j] > 9:
                has_flashed[i, j] = True
                n_of_flashes += 1
                grid[i, j] = 0
                for k, l in neighbours(i, j, *grid.shape):
                    if not has_flashed[k, l]:
                        grid[k, l] += 1
    return n_of_flashes


def compute_step(grid: np.array):
    has_flashed = update_energy(grid)
    n_of_flashes, some_octopus_flashed = 0, True
    while some_octopus_flashed:
        flashes = update_flashes(grid, has_flashed)
        n_of_flashes += flashes
        some_octopus_flashed = flashes > 0
    return n_of_flashes


@benchmark
def simulate_octopuses(data: List[str], days: int = 0, get_sync: bool = False) -> int:
    grid = np.array([list(map(int, list(line))) for line in data])
    total_flashes = 0
    day = 1
    while get_sync or day <= days:
        n_of_flashes = compute_step(grid)
        total_flashes += n_of_flashes
        if get_sync and np.all(grid == 0):
            return day
        day += 1
    return total_flashes


input_ = get_input()

print(f"Part 1: {simulate_octopuses(input_, days=100)}")
print(f"Part 2: {simulate_octopuses(input_, get_sync=True)}")
