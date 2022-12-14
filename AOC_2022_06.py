#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import get_input, benchmark, parsing_benchmark


@benchmark
def get_packet(data: str, window_size: int) -> int:
    i = window_size - 1
    found = False
    while not found:
        window = data[i - (window_size - 1) : i + 1]
        found = len(set(window)) == window_size
        i += 1
    return i


@parsing_benchmark
def parse_data(data):
    return data


data = parse_data(get_input(as_string=True))

print(f"Part 1: {get_packet(data, 4)}")
print(f"Part 2: {get_packet(data, 14)}")
