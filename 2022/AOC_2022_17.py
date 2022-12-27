#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import *
import numpy as np


class Rock:
    def place(self, tower):
        for p in self.points:
            tower[p[1], p[0]] = 1

    def move(self, direction):
        if direction in ["left", "right"]:
            x_diff = -1 if direction == "left" else 1
        else:
            x_diff = 0
        y_diff = 0 if direction in ["left", "right"] else -1
        for p in self.points:
            p[0] += x_diff
            p[1] += y_diff

    def can_fall(self, tower):
        for p in self.points:
            if p[1] == 0 or tower[p[1] - 1, p[0]] == 1:
                return False
        return True

    def can_move(self, tower, direction):
        for p in self.points:
            if (p[0] == 0 and direction == "left") or (
                p[0] == 6 and direction == "right"
            ):
                return False
            if tower[p[1], p[0] - 1 if direction == "left" else p[0] + 1] == 1:
                return False
        return True

    def heighest_point(self):
        return max([p[1] for p in self.points])

    def __repr__(self) -> str:
        return f"Rock: {self.points}"


class VerticalRock(Rock):
    def __init__(self, x, y) -> None:
        self.left_bound = x
        self.right_bound = x
        self.points = [
            [x, y],
            [x, y + 1],
            [x, y + 2],
            [x, y + 3],
        ]


class HorizontalRock(Rock):
    def __init__(self, x, y) -> None:
        self.left_bound = x
        self.right_bound = x + 3
        self.points = [
            [x, y],
            [x + 1, y],
            [x + 2, y],
            [x + 3, y],
        ]


class LRock(Rock):
    def __init__(self, x, y) -> None:
        self.left_bound = x
        self.right_bound = x + 2
        self.points = [
            [x + 2, y + 2],
            [x + 2, y + 1],
            [x + 2, y],
            [x + 1, y],
            [x, y],
        ]


class CrossRock(Rock):
    def __init__(self, x, y) -> None:
        self.left_bound = x
        self.right_bound = x + 2
        self.points = [
            [x + 1, y],
            [x, y + 1],
            [x + 1, y + 1],
            [x + 2, y + 1],
            [x + 1, y + 2],
        ]


class SquareRock(Rock):
    def __init__(self, x, y) -> None:
        self.left_bound = x
        self.right_bound = x + 1
        self.points = [
            [x, y],
            [x + 1, y],
            [x, y + 1],
            [x + 1, y + 1],
        ]


@parsing_benchmark
def parse_input(data: List[str]):
    return data.strip()


def build_tower(rocks_num):
    MAXIMUM_ROCK_HEIGHT = 4
    height = MAXIMUM_ROCK_HEIGHT * rocks_num
    WIDE = 7
    tower = np.zeros((height, WIDE), dtype=int)
    return tower


@benchmark
def simulate_falling_rocks(rocks_num, streams, world=None):
    cycling = -1
    order = [HorizontalRock, CrossRock, LRock, VerticalRock, SquareRock]
    found = False
    stream_indexes = {0: [], 1: [], 2: [], 3: [], 4: []}
    stream_i = 0
    heighest = -1
    for i in range(rocks_num):
        if not found:
            if stream_i % len(streams) in stream_indexes[i % len(order)]:
                print(
                    f"Cycling at i={i} at rock {i % len(order)} and stream {stream_i % len(streams)}"
                )
                found = True
                cycling = i
            else:
                stream_indexes[i % len(order)].append(stream_i % len(streams))
        rock = order[i % len(order)](2, heighest + 4)
        placed = False
        while not placed:
            stream_dir = streams[stream_i % len(streams)]
            stream_dir = "left" if stream_dir == "<" else "right"
            stream_i += 1
            if rock.can_move(world, stream_dir):
                rock.move(stream_dir)
            if rock.can_fall(world):
                rock.move("down")
            else:
                rock.place(world)
                heighest = (
                    rock.heighest_point()
                    if rock.heighest_point() > heighest
                    else heighest
                )
                placed = True
    print(stream_indexes)
    return world, heighest + 1, cycling


def simulate_falling_rocks_mathematic(streams):
    needed_simulation = len(streams) * 5
    world, heighest = simulate_falling_rocks(needed_simulation, streams)
    heighest1 = heighest * (1_000_000_000_000 // needed_simulation)
    print(heighest)
    remaining = 1_000_000_000_000 % needed_simulation
    world, heighest2 = simulate_falling_rocks(remaining, streams)
    return heighest1 + heighest2


def check_height(world):
    for i in range(world.shape[0], -1, -1):
        if np.sum(world[i, :]) != 0:
            return i
    return 0


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    data = parse_input(get_input(as_string=True))
    world = build_tower(2022)
    world, heighest1, cycling = simulate_falling_rocks(50, data, world)
    world, heighest2, cycling = simulate_falling_rocks(85, data, world)
    world, heighest3, cycling = simulate_falling_rocks(120, data, world)
    world = np.flipud(world)
    # plt.imshow(world, interpolation="nearest")
    # plt.show()
    print(f"Cycling at {cycling}")
    print(f"Part 1: {heighest1, heighest2, heighest3}")

    # print(f"Part 2: {simulate_falling_rocks_mathematic(data)}")
