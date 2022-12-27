#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Dict, List, Tuple
from aoc_helper import get_input, benchmark


def sense_input(data: List[str]) -> Tuple[int, int]:
    found, i = False, 0
    while not found:
        line = data[i]
        if not line:
            found = True
        i += 1

    return int(data[i - 2].split()[-1]), i - 2


def parse_stacks(data: List[str]) -> Tuple[Dict[int, List], List[str]]:
    crt_cols, crt_rows = sense_input(data)
    stacks = {i: [] for i in range(1, crt_cols + 1)}
    for line in data[0:crt_rows][::-1]:
        for i in range(0, crt_cols):
            if line[(i * 4) + 1] != " ":
                stacks[i + 1].append(line[(i * 4) + 1])
    instructions = data[crt_rows + 2 :]
    return stacks, instructions


@benchmark
def process_stacks(stacks: Dict[int, List], instr: List[str], alt: bool = False) -> str:
    def get_sol(stacks):
        return "".join([stacks[i][-1] for i in stacks.keys()])

    stacks = stacks.copy()
    for line in instr:
        l = line.split()
        qty, fr, to = int(l[1]), int(l[3]), int(l[5])
        move_buff = []
        for _ in range(qty):
            move_buff.append(stacks[fr].pop())
        move_buff = move_buff[::-1] if alt else move_buff
        for crate in move_buff:
            stacks[to].append(crate)
    return get_sol(stacks)


if __name__ == "__main__":
    data = get_input()

    print(f"Part 1: {process_stacks(*parse_stacks(data))}")
    print(f"Part 2: {process_stacks(*parse_stacks(data), alt=True)}")
