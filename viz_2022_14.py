#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from typing import Dict
from aoc_helper import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.animation as animation


@parsing_benchmark
def parse_input(data: List[str]) -> List[Dict[str, int]]:
    def strp_to_ditp(strp: str) -> Dict[str, int]:
        x, y = strp.split(",")
        return {"x": int(x), "y": int(y)}

    segments = []
    for line in data:
        line = line.split(" -> ")
        points = list(map(strp_to_ditp, line))
        segments.append(points)
    return segments


def get_limits(segments):
    x = [p["x"] for segment in segments for p in segment]
    y = [p["y"] for segment in segments for p in segment]

    return {
        "min_x": min(x),
        "min_y": min(y),
        "max_x": max(x),
        "max_y": max(y),
    }


def build_cave(segments: List, padd: int = 5):
    lim = get_limits(segments)
    x_offset = -lim["min_x"] + padd

    cave = np.zeros(
        (lim["max_y"] + 1 + 2, lim["max_x"] - lim["min_x"] + padd * 2), dtype=int
    )
    for segment in segments:
        for i in range(1, len(segment)):
            pi, pf = segment[i - 1], segment[i]

            if pi["y"] == pf["y"]:
                # Swap origin and destination if origin is on the greater than destination
                pi, pf = (pf, pi) if pi["x"] > pf["x"] else (pi, pf)
                y = pi["y"]
                x = range(pi["x"] + x_offset, pf["x"] + x_offset + 1)
            else:
                # Swap origin and destination if origin is on the greater than destination
                pi, pf = (pf, pi) if pi["y"] > pf["y"] else (pi, pf)
                x = pi["x"] + x_offset
                y = range(pi["y"], pf["y"] + 1)
            cave[y, x] = 1
    return cave


# Sand fall simulation function.
def sand_fall(
    cave: np.ndarray,
    lim: tuple,
    x: int = 500,
    y: int = 0,
    padd: int = 5,
):
    x_offset = -lim["min_x"] + padd

    # If sand source is blocked, return False or reach the bottom, return False
    if cave[0, x + x_offset] == 2 or y > lim["max_y"] + 1:
        return False

    # If there is something below the sand source, check if sand can fall left or right
    if cave[y + 1, x + x_offset] in [1, 2]:
        # Check if sand can fall left or right
        if cave[y + 1, x + x_offset - 1] == 0:
            if not sand_fall(cave, lim, x - 1, y + 1, padd):
                return False
        # Check if sand can fall right
        elif cave[y + 1, x + x_offset + 1] == 0:
            if not sand_fall(cave, lim, x + 1, y + 1, padd):
                return False
        # Otherwise, sand will stop here
        else:
            cave[y, x + x_offset] = 2
        return True
    else:
        return sand_fall(cave, lim, x, y + 1, padd)


@benchmark
def simulate_sandfall(cave, bounds, void=True, padding=5):
    step, endless = 0, False
    # Fill the bottom row with rock if there is no void (part 2)
    if not void:
        cave[-1:, :] = 1
    while not endless:
        endless = not sand_fall(cave, bounds, padd=padding)
        step += 1
    return step - 1


def update(frame):
    print(f"Generating frame: {frame}")
    sand_fall(cave, limits)
    scat.set_data(cave)


def init():
    pass


if __name__ == "__main__":
    segments = parse_input(get_input())

    limits = get_limits(segments)
    cave = build_cave(segments)
    big_cave_padding = 150
    big_cave = build_cave(segments, padd=big_cave_padding)

    # Animation
    fig = plt.figure(figsize=(8, 16))
    ax = fig.add_axes([0, 0, 1, 1], frameon=False)
    # ax.set_xlim(0, 1), ax.set_xticks([])
    # ax.set_ylim(0, 1), ax.set_yticks([])
    cmap = colors.ListedColormap(["black", "white", "yellow"])
    scat = ax.imshow(
        cave,
        vmin=0,
        vmax=2,
        interpolation="nearest",
    )
    ax.set_xticks([])
    ax.set_yticks([])

    ani = animation.FuncAnimation(
        fig,
        update,
        init_func=init,
        interval=1,
        frames=np.arange(1, 1100, 1),
    )
    FFwriter = animation.FFMpegWriter(fps=60)
    ani.save("animation.mp4", writer=FFwriter)

    print(f"Part 1: {simulate_sandfall(cave, limits)}")
