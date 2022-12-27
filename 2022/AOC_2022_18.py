#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


@parsing_benchmark
def parse_input(data: List[str]) -> np.ndarray:
    list_of_slices = []
    max_x = 0
    max_y = 0
    max_z = 0
    for line in data:
        x, y, z = list(map(int, line.split(",")))
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if z > max_z:
            max_z = z
        list_of_slices.append([x, y, z])
    tensor = np.zeros((max_x + 1, max_y + 1, max_z + 1), dtype=bool)
    for s in list_of_slices:
        tensor[s[0], s[1], s[2]] = 1
    return tensor


# Function that given a 3-dimensional numpy boolean array, computes the number of visible faces of the cubes formed by the 1s.
# The function is not optimized, but it works.  It is not optimized because it is not the bottleneck of the solution.
@benchmark
def count_visible_faces(tensor: np.ndarray) -> int:
    faces = 0
    for x in range(tensor.shape[0]):
        for y in range(tensor.shape[1]):
            for z in range(tensor.shape[2]):
                if tensor[x, y, z] == 1:
                    # Check if the cube is visible from the top
                    if y == tensor.shape[1] - 1 or tensor[x, y + 1, z] == 0:
                        faces += 1
                    # Check if the cube is visible from the bottom
                    if y == 0 or tensor[x, y - 1, z] == 0:
                        faces += 1
                    # Check if the cube is visible from the front
                    if z == tensor.shape[2] - 1 or tensor[x, y, z + 1] == 0:
                        faces += 1
                    # Check if the cube is visible from the back
                    if z == 0 or tensor[x, y, z - 1] == 0:
                        faces += 1
                    # Check if the cube is visible from the left
                    if x == 0 or tensor[x - 1, y, z] == 0:
                        faces += 1
                    # Check if the cube is visible from the right
                    if x == tensor.shape[0] - 1 or tensor[x + 1, y, z] == 0:
                        faces += 1
    return faces


def count_trapped(tensor: np.ndarray) -> int:
    trapped = 0
    for x in range(1, tensor.shape[0] - 1):
        for y in range(1, tensor.shape[1] - 1):
            for z in range(1, tensor.shape[2] - 1):
                if tensor[x, y, z] == 0:
                    if (
                        tensor[x - 1, y, z] == 1
                        and tensor[x + 1, y, z] == 1
                        and tensor[x, y - 1, z] == 1
                        and tensor[x, y + 1, z] == 1
                        and tensor[x, y, z - 1] == 1
                        and tensor[x, y, z + 1] == 1
                    ):
                        trapped += 1

    return trapped


def count_only_outside_faces(tensor: np.ndarray) -> int:
    all_visible = count_visible_faces(tensor)
    hidden = count_trapped(tensor)
    return all_visible - hidden * 6


if __name__ == "__main__":
    data = get_input()
    tensor = parse_input(data)
    print(f"Part 1: {count_visible_faces(tensor)}")
    print(f"Part 2: {count_only_outside_faces(tensor)}")  # 3462 too high
