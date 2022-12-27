#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import get_input


def analyze_packet(data):
    binary = bin(int(data, 16))
    version = int(binary[2:5], 2)
    type_id = int(binary[5:8], 2)
    print(version, type_id)


input_ = get_input(as_string=True)

print(analyze_packet(input_))
