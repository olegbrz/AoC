#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import get_input, benchmark


input_ = get_input()


@benchmark
def get_elves_calories(input_, part=1):
    elves_calories = []
    calories = 0
    for i in input_:
        if i:
            calories += int(i)
        else:
            elves_calories.append(calories)
            calories = 0
    elves_calories.append(calories)
    if part == 1:
        return max(elves_calories)
    elif part == 2:
        return sum(sorted(elves_calories, reverse=True)[:3])


print(f"Part 1: {get_elves_calories(input_)}")
print(f"Part 2: {get_elves_calories(input_, part=2)}")
