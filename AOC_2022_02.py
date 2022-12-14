#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from aoc_helper import benchmark, get_input

input_ = get_input()

"""
A = Rock
B = Paper
C = Scissors
---
X = Rock (1)
Y = Paper (2)
Z = Scissors (3)

0 if lost
3 if draw
6 if won
"""

eq = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}


@benchmark
def compute_score(data: List[str]) -> int:
    score = 0
    for pair in data:
        move_score = 0
        bot, me = pair.split()

        if eq[me] == eq[bot]:
            move_score += 3 + eq[me]
        elif eq[me] - eq[bot] in [1, -2]:
            move_score += 6 + eq[me]
        else:
            move_score += 0 + eq[me]
        score += move_score
    return score


"""
X = lose
Y = draw
Z = win
"""


@benchmark
def compute_score_alt(data: List[str]) -> int:
    score = 0
    for pair in data:
        bot, outcome = pair.split()

        if outcome == "X":
            score += ((eq[bot] + 1) % 3) + 1
        elif outcome == "Y":
            score += eq[bot] + 3
        else:
            score += ((eq[bot]) % 3) + 1 + 6
    return score


print(f"Part 1: {compute_score(input_)}")
print(f"Part 2: {compute_score_alt(input_)}")
