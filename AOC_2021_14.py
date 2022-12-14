#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Dict, List
from aoc_helper import get_input, benchmark
from collections import defaultdict

input_ = get_input()


def get_counts(chain: str, w: int = 1) -> Dict[str, int]:
    counts = defaultdict(int)
    for i in range(len(chain)-w+1):
        counts[chain[i:i+w] if w > 1 else chain[i]] += 1
    return counts


@ benchmark
def polimerize(data: List[str], days: int) -> int:
    template, rules = data[0], data[2:]
    rules = {r.split(' -> ')[0]: r.split(' -> ')[1] for r in rules}
    char_counts, kmer_counts = get_counts(template), get_counts(template, 2)

    for _ in range(days):
        aux = defaultdict(int)
        for pair in list(kmer_counts):
            e = rules[pair]
            aux[pair[0] + e] += kmer_counts[pair]
            aux[e + pair[1]] += kmer_counts[pair]
            char_counts[e] += kmer_counts[pair]
            kmer_counts[pair] = 0
        kmer_counts = aux

    return max(char_counts.values()) - min(char_counts.values())


print(f"Part 1: {polimerize(input_, 10)}")
print(f"Part 2: {polimerize(input_, 40)}")
