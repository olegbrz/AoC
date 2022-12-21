#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Dict
import re
from ast import literal_eval
from aoc_helper import *
from sympy import symbols, solve, sympify


@parsing_benchmark
def parse_input(data: List[str]) -> Dict[str, str]:
    return {k: v for k, v in [line.split(": ") for line in data]}


def is_math_expression(expression: str) -> bool:
    # Check if the string contains only numbers and math operators.
    return re.match(r"^[0-9\+\-\*\/\(\)\=]*$", expression.replace(" ", "")) != None


def get_coeffs(e):
    return (
        e.replace(" + ", " ")
        .replace(" - ", " ")
        .replace(" * ", " ")
        .replace(" / ", " ")
        .replace("(", " ")
        .replace(")", " ")
        .replace("=", " ")
        .split()
    )


@benchmark
def compute_root(values: Dict[str, str], humn: bool = False) -> int:
    v = values.copy()
    root = v.pop("root", None)
    root = root.replace("+", " = ") if humn else root

    while not is_math_expression(root.replace("humn", "0") if humn else root):
        coeffs = get_coeffs(root)
        for c in coeffs:
            needs_replace = not c.isnumeric() and (not humn or not c == "humn")
            if needs_replace:
                root = root.replace(c, "(" + v.pop(c) + ")")
    print(root)
    return (
        solve(sympify("Eq(" + root.replace("=", ",") + ")"))[0]
        if humn
        else int(eval(root))
    )


if __name__ == "__main__":
    values = parse_input(get_input())
    print(f"Part 1: {compute_root(values)}")
    print(f"Part 2: {compute_root(values, humn=True)}")
