#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Dict
from aoc_helper import *
import pprint


class Valve:
    def __init__(self, name: str, f_rate) -> None:
        self.name = name
        self.f_rate = f_rate
        self.leads_to = []

    def __repr__(self) -> str:
        return f"Valve(Id=str(ID={self.name} FR={self.f_rate} L={[v.name for v in self.leads_to]})"


# Function that computes the best solution for a Traveling Salesman Problem-like problem.
# The input is a graph of nodes and edges. The distance between two nodes is always 1.
# The objective is to find a path that minimizes the travel distance, maximizing the node values sum.
# The function returns the cost of the best path and the sum of the node values in that path.
def traverse_tree(valve: Valve, valves: Dict[str, Valve], cost: int) -> int:
    if valve.name == "ZZ":
        return cost
    else:
        costs = []
        for v in valve.leads_to:
            costs.append(traverse_tree(v, valves, cost + v.f_rate))
        return min(costs)


@parsing_benchmark
def parse_input(data: List[str]):
    valves = {}
    for valve in data:
        spline = valve.replace(",", "").split()
        vname = spline[1]
        frate = int(spline[4].split("=")[1].replace(";", ""))
        valves[vname] = Valve(vname, frate)
    for valve in data:
        spline = valve.replace(",", "").split()
        vname = spline[1]
        if "valves" in spline:
            splitw = "valves "
        else:
            splitw = "valve "
        vlead = valve.replace(",", "").split(splitw)[1].split()
        for vl in vlead:
            valves[vname].leads_to.append(valves[vl])
    return valves


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    data = get_input()
    tree = parse_input(data)

    print(f"Part 1: {traverse_tree(valve=tree['AA'], valves=tree, cost=0)}")
    print(f"Part 2: {2}")
