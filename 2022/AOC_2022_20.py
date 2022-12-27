#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import *


class DoubleLinkedItem:
    def __init__(self, value, prev_item=None, next_item=None):
        self.value = value
        self.has_mixed = False
        self.next = next_item
        self.prev = prev_item

    def get_index(self, first):
        found = False
        s = 0
        it = first
        while not found and it.next != None:
            if it == self:
                found = True
            else:
                it = it.next
            s += 1
        return s - 1

    def jump(self, first, length):
        if self.value > 0:
            self.prev.next = self.next
            self.next.prev = self.prev
        next_index = (self.value + self.get_index(first)) % length
        for _ in range(self.value):
            it = self.next
        self.next = it.next
        it.next.prev = self
        it.next = self
        if self.prev:
            self.prev = it
        self.has_mixed = True

    def is_last(self):
        return self.next == None

    def is_first(self):
        return self.prev == None

    def __repr__(self):
        return f"{'<HEAD>=' if not self.prev else ''}<{self.value}>{'=' if self.next else ''}{self.next if self.next != None else '=<TAIL>'}"


def parse_input(data):
    prev = None
    for line in data:
        value = int(line)
        item = DoubleLinkedItem(value, prev)
        if prev != None:
            prev.next = item
        else:
            first = item
        prev = item
    return first, len(data)


if __name__ == "__main__":
    data = get_input()
    first, length = parse_input(data)
    it = first
    while it.next != None:
        if not it.next.has_mixed:
            it.next.jump(first, length)
            it = it.next
        print(first)
        it = it.next
    print(f"Part 1: {first}")
    print(f"Part 2: {2}")
