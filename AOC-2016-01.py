#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import get_input, benchmark


class Me:
    directions = [0, 90, 180, 360]

    def __init__(self):
        self.position = {'x': 0, 'y': 0}
        self.facing = 0
        self.visited = {"0,0": 1}
        self.double_visited = []

    def get_hashable_position(self) -> str:
        return f"{self.position['x']},{self.position['y']}"

    def move(self, instruction) -> None:
        turn = instruction[0]
        distance = int(instruction[1:])
        if turn == 'L':
            self.facing = (self.facing - 90) % 360
        else:
            self.facing = (self.facing + 90) % 360
        for _ in range(distance):
            if self.facing == 0:
                self.position['y'] += 1
            elif self.facing == 90:
                self.position['x'] += 1
            elif self.facing == 180:
                self.position['y'] -= 1
            elif self.facing == 270:
                self.position['x'] -= 1

            if self.get_hashable_position() in self.visited.keys():
                self.visited[self.get_hashable_position()] += 1
                self.double_visited.append(
                    [self.position['x'], self.position['y']])
            else:
                self.visited[self.get_hashable_position()] = 1

    def already_visited(self) -> bool:
        return self.visited[self.get_hashable_position()] > 1


@benchmark
def walk_city(data, twice=False):
    dummy = Me()

    for indication in data:
        dummy.move(indication)
        if twice and dummy.double_visited:
            return abs(dummy.double_visited[0][0]) + abs(dummy.double_visited[0][1])

    return abs(dummy.position['x']) + abs(dummy.position['y'])


input_ = get_input(as_string=True)
input_ = input_.replace("\n", "").split(", ")

print(f"Part 1: {walk_city(input_)}")
print(f"Part 2: {walk_city(input_, twice=True)}")
