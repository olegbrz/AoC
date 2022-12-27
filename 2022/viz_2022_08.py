#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import aoc_helper as ah
from AOC_2022_08 import tree_scenic_score, parse_input, is_visible
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np


data = ah.get_input()

forest = parse_input(data)
scores = [
    [tree_scenic_score(forest, i, j) for j in range(len(forest[0]))]
    for i in range(len(forest))
]

visibles = [
    [is_visible(forest, i, j) for j in range(len(forest[0]))]
    for i in range(len(forest))
]

scores = np.array(scores)
print(scores.min())
max_idx = np.where(scores == np.amax(scores))
print(max_idx)

plt.suptitle("Advent of Code: day 8")
plt.subplot(131)
plt.title("Forest tree heights")
plt.imshow(
    forest,
    cmap="YlGn",
    interpolation="nearest",
)
plt.colorbar(fraction=0.046, pad=0.04)

plt.subplot(132)
plt.title("Visible trees")
plt.imshow(
    visibles,
    cmap="gray",
    interpolation="nearest",
)
plt.colorbar(fraction=0.046, pad=0.04)

plt.subplot(133)
plt.title("Tree scenic scores (log scale)")
plt.imshow(
    scores,
    cmap="viridis",
    interpolation="none",
)
plt.annotate(
    f"Max tree score {scores.max()}",
    xy=(max_idx[1] + 0.5, max_idx[0] + 0.5),
    xytext=(max_idx[1] + 0.5, max_idx[0] + 0.5 + 40),
    arrowprops=dict(arrowstyle="->"),
    arrowprops=dict(arrowstyle="->"),
)

pcm = plt.pcolor(scores, norm=colors.LogNorm())

plt.colorbar(pcm, fraction=0.046, pad=0.04)
plt.show()
