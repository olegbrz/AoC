#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import get_input, benchmark


input_ = get_input()


is_full_overlap = lambda s1, s2: (s1[0] >= s2[0] and s1[1] <= s2[1]) or (
    s2[0] >= s1[0] and s2[1] <= s1[1]
)


is_overlap = lambda s1, s2: (s1[0] <= s2[1] and s1[1] >= s2[0]) or (
    s2[0] <= s1[1] and s2[1] >= s1[0]
)


@benchmark
def count_overlaps(input_):
    c1 = 0
    c2 = 0
    for line in input_:
        p1, p2 = line.split(",")
        p1, p2 = p1.split("-"), p2.split("-")
        secs1, secs2 = [int(p1[0]), int(p1[1])], [int(p2[0]), int(p2[1])]
        c1 += is_full_overlap(secs1, secs2)
        c2 += is_overlap(secs1, secs2)
    return c1, c2


c1, c2 = count_overlaps(input_)

print(f"Part 1: {c1}")
print(f"Part 2: {c2}")
