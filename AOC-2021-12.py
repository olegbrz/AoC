#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from aoc_helper import get_input, benchmark
from collections import defaultdict


def generate_graph(data: List[str]) -> defaultdict:
    G = defaultdict(list)
    for line in data:
        start, end = line.split("-")
        G[start].append(end)
        G[end].append(start)
    return G


def explore_paths(
    graph: defaultdict, path: List[str] = ["start"], re_visit: bool = False
) -> int:

    if path[-1] == "end":
        return 1
    paths = 0
    for adj_node in graph[path[-1]]:
        if not adj_node.islower() or adj_node not in path:
            paths += explore_paths(graph, path + [adj_node], re_visit)
        elif re_visit and adj_node in path and adj_node != "start":
            paths += explore_paths(graph, path + [adj_node], False)
    return paths


@benchmark
def get_paths(data: List[str], re_visit=False) -> int:
    G = generate_graph(data)
    paths = explore_paths(G, re_visit=re_visit)
    return paths


input_ = get_input()

print(f"Part 1: {get_paths(input_)}")
print(f"Part 2: {get_paths(input_, re_visit=True)}")
