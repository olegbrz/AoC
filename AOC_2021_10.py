#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from aoc_helper import get_input, benchmark

opening_symbs = ['(', '[', '{', '<']
closing_symbs = [')', ']', '}', '>']
matching = {
    ')': '(', ']': '[', '}': '{', '>': '<',
    '(': ')', '[': ']', '{': '}', '<': '>'
}

illegal_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
missing_score = {')': 1, ']': 2, '}': 3, '>': 4}


def get_illegal_symb(line: List[str]) -> str:
    order = []
    illegal_symb = None
    i = 0
    while not illegal_symb and i < len(line):
        symb = line[i]
        if symb in opening_symbs:
            order.append(symb)
        elif matching[symb] != order.pop(-1):
            illegal_symb = symb
        i += 1
    return illegal_symb


def get_missing_symbs(line: List[str]) -> List[str]:
    symbs_stack = []
    for symb in line:
        if symb in opening_symbs:
            symbs_stack.append(symb)
        else:
            del symbs_stack[-1]
    return list(map(lambda x: matching[x], symbs_stack[::-1]))


@benchmark
def corrupted_scoring(lines: List[str]) -> int:
    ilegal_symbs = filter(None, map(get_illegal_symb, lines))
    return sum(map(lambda x: illegal_score[x], ilegal_symbs))


@benchmark
def incomplete_scoring(lines: List[str]) -> int:
    incomplete_lines = filter(lambda x: not get_illegal_symb(x), lines)
    missing_symbs_lines = map(get_missing_symbs, incomplete_lines)
    scores = []
    for missing_symbs in missing_symbs_lines:
        score = 0
        for symb in missing_symbs:
            score *= 5
            score += missing_score[symb]
        scores.append(score)
    return sorted(scores)[len(scores)//2]


input_ = get_input()


print(f"Part 1: {corrupted_scoring(input_)}")
print(f"Part 2: {incomplete_scoring(input_)}")
