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

        best_coeff = coeffs[dist_0.index(min(dist_0))]
        best_remainder = remainders[dist_0.index(min(dist_0))]
        if abs(best_remainder) < abs(r):
            r = best_remainder
            bits[bit] = best_coeff
        else:
            bits[bit] = 0
        bit -= 1

    # Replace -1 with -, -2 with =
    replace_neg_coeff = lambda x: "-" if x == -1 else "=" if x == -2 else str(x)
    # Convert to Little Endian SNAFU string
    bits = "".join(map(replace_neg_coeff, reversed(bits)))
    return bits


@benchmark
def get_fuel_sum(data: List[str]) -> str:
    temps = [snafu_to_b10(line) for line in data]
    return b10_to_snafu(sum(temps))


if __name__ == "__main__":
    data = get_input()
    print(f"Part 1: {get_fuel_sum(data)}")
