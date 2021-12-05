#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Literal
from requests.api import get
from aoc_helper import get_input, benchmark


class Santa:
    """It's Santa, who doesn't know Santa?"""

    def __init__(self):
        self.p = {'x': 0, 'y': 0}

    def move(self, direction: Literal["^", "v", "<", ">"]) -> None:
        if direction == '^':
            self.p['y'] += 1
        elif direction == 'v':
            self.p['y'] -= 1
        elif direction == "<":
            self.p['x'] -= 1
        elif direction == ">":
            self.p['x'] += 1

    def get_hashable_position(self) -> str:
        return f"{self.p['x']},{self.p['y']}"


class RoboSanta(Santa):
    """Robot version of Santa, inherits all characteristics,
    but with different name :)"""

    def __init__(self):
        super().__init__()


@benchmark
def houses(data: str, robot=False) -> int:
    santa = Santa()
    if robot:
        robo_santa = RoboSanta()

    visited = {f"0,0": 2 if robot else 1}
    for idx, indication in enumerate(data):
        if robot and idx % 2 != 0:
            robo_santa.move(indication)
            position = robo_santa.get_hashable_position()
        else:
            santa.move(indication)
            position = santa.get_hashable_position()

        if position in visited.keys():
            visited[position] += 1
        else:
            visited[position] = 1

    return len(visited)


input_ = get_input(as_string=True)


print(f"Part 1: {houses(input_)}")
print(f"Part 2: {houses(input_, robot=True)}")
