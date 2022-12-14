#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import *


@parsing_benchmark
def parse_input(data):
    return data


def position_diff(p1: Tuple, p2: Tuple) -> int:
    return p2[0] - p1[0], p2[1] - p1[1]


def are_adjacent(p1: Tuple, p2: Tuple) -> bool:
    d = position_diff(p1, p2)
    return abs(d[0]) <= 1 and abs(d[1]) <= 1


def update_position(p1: Tuple, p2: Tuple) -> Tuple:
    d = position_diff(p1, p2)
    # Distance normalization
    dx = d[0] / abs(d[0]) if d[0] != 0 else 0
    dy = d[1] / abs(d[1]) if d[1] != 0 else 0
    return int(dx), int(dy)


@benchmark
def count_visited_flex(data: List[str], knots: int = 2, viz: bool = False) -> int:
    visited = set((0, 0))
    knots = [[0, 0] for _ in range(knots)]

    for instruction in data:
        d, amount_of_movement = instruction.split()
        amount_of_movement = int(amount_of_movement)
        for _ in range(amount_of_movement):
            # Update head knot position
            knots[0][1 if d in ["U", "D"] else 0] += 1 if d in ["U", "R"] else -1
            # Update tailing knots iteratively
            for i in range(1, len(knots)):
                if not are_adjacent(knots[i], knots[i - 1]):
                    dx, dy = update_position(knots[i], knots[i - 1])
                    knots[i][0] += dx
                    knots[i][1] += dy
            # Add to visited
            visited.add(tuple(knots[-1]))

    return len(visited) if not viz else visited


data = parse_input(get_input())

if __name__ == "__main__":
    print(f"Part 1: {count_visited_flex(data)}")
    print(f"Part 2: {count_visited_flex(data, 10)}")
