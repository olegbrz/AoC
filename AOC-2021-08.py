#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import get_input, benchmark


def sort_string(x): return ''.join(sorted(x))


def contains(x, y):
    return x[0] in y and x[1] in y


def non_intersection(x, y):
    return sort_string(set(x) ^ set(y))


@benchmark
def get_1478(data):
    numbers = 0
    for line in data:
        for digit in line.split(" | ")[1].split():
            if len(digit) in [2, 3, 4, 7]:
                numbers += 1
    return numbers


@benchmark
def get_mappings(data):
    sum_of_outputs = 0
    for line in data:
        m = {}
        p, output_digits = line.split(" | ")
        p = list(map(sort_string, sorted(p.split(), key=lambda x: len(x))))
        output_digits = list(map(sort_string, output_digits.split()))

        # Map unique numbers (1, 4, 7, 8)
        m[1], m[4], m[7], m[8] = p[0], p[2], p[1], p[9]
        # Get number 3 segments by comparing 2, 3
        # and 5 (length 5) with 1 (segments C and E)
        m[3], t = [(p[i], i) for i in [3, 4, 5] if contains(m[1], p[i])][0]
        # Get segments B and E by performing non-intersecion of known 8 and 3
        segm_be = non_intersection(m[8], m[3])

        # Get 6, 9, 0 segments (possible eindices 6, 7, 8)
        for i in [6, 7, 8]:
            if contains(segm_be, p[i]) and contains(m[1], p[i]):
                m[0] = p[i]
            elif contains(segm_be, p[i]):
                m[6] = p[i]
            else:
                m[9] = p[i]

        # Get segment C as we know 6 and 8
        segm_c = non_intersection(m[6], m[8])

        # Get 2 and 5 segments (possible indices 3, 4, 5)
        for i in [x for x in [3, 4, 5] if x != t]:
            m[2 if segm_c in p[i] else 5] = p[i]

        reverse_map = {v: k for k, v in m.items()}
        digits = [str(reverse_map[digit]) for digit in output_digits]
        sum_of_outputs += int(''.join(digits))

    return sum_of_outputs


input_ = get_input()

print(f"Part 1: {get_1478(input_)}")
print(f"Part 2: {get_mappings(input_)}")
