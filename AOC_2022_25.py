#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import *
from math import floor


def snafu_to_b10(number: int) -> int:
    def snafu_bit_to_10bit(n, idx):
        coeff = 1 if n.isdigit() else -1
        n = "1" if n == "-" else "2" if n == "=" else str(n)
        return coeff * int(n) * 5**idx

    digits = [snafu_bit_to_10bit(n, idx) for idx, n in enumerate(number[::-1])]
    return sum(digits)


def b10_to_snafu(number: int) -> str:
    bits_needed = 0
    while number >= 5**bits_needed - floor(5**bits_needed / 2):
        bits_needed += 1

    bits = [0] * bits_needed
    bit = bits_needed - 1
    r = number
    coeffs = [-2, -1, 0, 1, 2]

    while r != 0:
        remainders = [r - 5**bit * coeff for coeff in coeffs]
        dist_0 = [abs(i) for i in remainders]
        best_idx = dist_0.index(min(dist_0))

        best_c = coeffs[best_idx]
        best_r = remainders[best_idx]
        if abs(best_r) < abs(r):
            r = best_r
            bits[bit] = best_c
        else:
            bits[bit] = 0
        bit -= 1

    # Replace -1 with -, -2 with = and convert to Little Endian SNAFU string
    bits = "".join(
        map(
            lambda x: "-" if x == -1 else "=" if x == -2 else str(x),
            reversed(bits),
        )
    )
    return bits


@benchmark
def get_fuel_sum(data: List[str]) -> str:
    temps = [snafu_to_b10(line) for line in data]
    return b10_to_snafu(sum(temps))


if __name__ == "__main__":
    data = get_input()
    print(f"Part 1: {get_fuel_sum(data)}")
