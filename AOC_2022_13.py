#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import *
import json

# Function to parse a list of strings formatted as Python list to a Python list using json module
@parsing_benchmark
def parse_list(data):
    return [json.loads(line) for line in data if line]


# This function has to compare if to items are in the right order. The items are lists of numbers and other lists. The function has to compare the lists element-wise, and return False when the first element not in order is found. If the elements inside are lists, they have to be compared recursively.
def compare_packets(left_o, right_o, recursive=False):
    # Make a copy of the lists so we don't modify the original lists
    left = left_o[:]
    right = right_o[:]

    # Trivial cases
    if not left and right:
        return True
    elif left and not right:
        return False

    # Compare the lists element-wise
    for i in range(max([len(left), len(right)])):
        # If the right list is shorter, the left list is bigger
        if i >= len(right):
            return False
        elif i >= len(left):
            return True

        # If the types are different, we have to convert the list to a list of lists
        if type(left[i]) != type(right[i]):
            if type(left[i]) == list:
                right[i] = [right[i]]
            elif type(right[i]) == list:
                left[i] = [left[i]]

            # If the types are still different, we have to compare the lists recursively
        if type(left[i]) == list and type(right[i]) == list:
            result = compare_packets(left[i], right[i], True)
            if result == True:
                return True
            elif result == None and i == len(left) - 1 and recursive:
                return None
            elif result == None and i == len(left) - 1:
                return False
            elif result == False:
                return False

        # If the types are the same, we can compare the elements
        elif type(left[i]) == int and type(right[i]) == int:
            if left[i] > right[i]:
                return False
            elif left[i] < right[i]:
                return True
    return None if recursive else False


@benchmark
def decode_key(packets):
    first, second = 1, 2
    for p in packets:
        first += 1 if compare_packets(p, [[2]]) else 0
        second += 1 if compare_packets(p, [[6]]) else 0
    return first * second


@benchmark
def count_right_order(packets):
    count = 0
    for i in range(0, len(packets), 2):
        left = packets[i]
        right = packets[i + 1]

        in_order = compare_packets(left, right)
        if in_order:
            count += (i + 1) - (i // 2)
    return count


if __name__ == "__main__":
    data = get_input()
    packets = parse_list(data)
    print(f"Part 1: {count_right_order(packets)}")
    print(f"Part 2: {decode_key(packets)}")
