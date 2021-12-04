#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Dict, List
from aoc_helper import get_input


def proc_dive(params: Dict, instr: str, val: int) -> None:
    if instr == "forward":
        params["h_pos"] += val
    elif instr == "down":
        params["depth"] += val
    elif instr == "up":
        params["depth"] -= val


def proc_dive_alt(params: Dict, instr: str, val: int) -> None:
    if instr == "forward":
        params["h_pos"] += val
        params["depth"] += (params["aim"] * val)
    elif instr == "down":
        params["aim"] += val
    elif instr == "up":
        params["aim"] -= val


def dive(data: List[str], alt: bool = False) -> int:
    params = {"aim": 0, "depth": 0, "h_pos": 0}
    update_params = proc_dive_alt if alt else proc_dive

    for line in data:
        instr, val = line.split()
        update_params(params, instr, int(val))

    return params["depth"] * params["h_pos"]


input_ = get_input()

print(f"Part 1: {dive(input_)}")
print(f"Part 2: {dive(input_, alt=True)}")
