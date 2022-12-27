#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import *
import numpy as np
from functools import reduce


@parsing_benchmark
def parse_input(data: List[str]) -> np.ndarray:
    """Convert list of strings to numpy 2D array of ints.
    Example ['12','34'] would be parsed as [[1,2], [3,4]]"""
    return np.array([list(map(lambda x: int(x), list(line))) for line in data])


def get_edge_trees(forest: np.ndarray) -> int:
    return (forest.shape[0] * 4) - 4


def get_view(forest: np.ndarray, i: int, j: int, direction: int) -> np.ndarray:
    """get_view computes all visible trees of given tree in a given direction"""
    if direction == 0:
        view = np.flip(forest[:i, j])
    elif direction == 1:
        view = forest[i, j + 1 :]
    elif direction == 2:
        view = forest[i + 1 :, j]
    elif direction == 3:
        view = np.flip(forest[i, :j])
    return view


def is_visible(forest: np.ndarray, i: int, j: int) -> bool:
    """is_visible computes if a tree is visible in any of the 4 directions"""
    tree_height = forest[i, j]
    return any([all(tree_height > get_view(forest, i, j, d)) for d in [0, 1, 2, 3]])


@benchmark
def count_visible_trees(forest: np.ndarray) -> int:
    # Edge trees are always visible
    visible = get_edge_trees(forest)
    # Count inner visible trees
    for i in range(1, len(forest) - 1):
        visible += sum(is_visible(forest, i, j) for j in range(1, len(forest[0]) - 1))
    return visible


def tree_scenic_score(forest: np.ndarray, i: int, j: int) -> int:
    """tree_scenic_score computes scenic score of a tree, by exploring his views"""
    tree_height = forest[i, j]
    views = [get_view(forest, i, j, d) for d in [0, 1, 2, 3]]
    directional_scores = [max_view(tree_height, view) for view in views]
    scenic_score = reduce(lambda x, y: x * y, directional_scores)

    return scenic_score


def max_view(tree_height: int, view: np.ndarray) -> int:
    blocked, i = False, 0
    while not blocked and i < len(view):
        blocked = view[i] >= tree_height
        i += 1
    return i


@benchmark
def get_max_score(forest: np.ndarray) -> int:
    max_score = 0
    for i in range(len(forest)):
        for j in range(len(forest[0])):
            tree_score = tree_scenic_score(forest, i, j)
            if tree_score > max_score:
                max_score = tree_score
    return max_score


data = get_input()
forest = parse_input(data)

print(f"Part 1: {count_visible_trees(forest)}")
print(f"Part 2: {get_max_score(forest)}")
