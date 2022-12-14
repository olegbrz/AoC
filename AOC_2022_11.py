#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import *
from functools import reduce
import operator


class Monkey:
    """Monkey class implements the logic of the monkeys in the problem.
    Each monkey has a list of items, its own worry level operation, its own
    test operation, its own monkeys to send the items to.
    """

    def __init__(
        self,
        items: List[int],
        operation: callable,
        operation_value: int,
        test_value: int,
        true_monkey: object,
        false_monkey: object,
        monkey_list: List[object],
    ):
        self.items = items
        self.operation = operation
        self.operation_value = operation_value
        self.test_value = test_value
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.monkey_list = monkey_list

        # Internal variables
        self.items_copy = items[:]
        self.examinated_items = 0
        self.test_func = lambda x: x % self.test_value == 0
        self.relief_func = lambda x: x // 3

    def examinate_items(self, relief: bool = True, factor: int = 1) -> None:
        """examinate_items simulates the examination of the items by the monkey
        as its described in the problem.

        Args:
            relief (bool, optional): if worry level relief is applied or not.
                                    Defaults to True.
            factor (int, optional): Factor calculated as product of all monkeys
                                    test mod values. Defaults to 1.
        """
        for item in self.items:
            # Increment the number of items examinated by the monkey
            self.examinated_items += 1
            worry_level = self.operation(item, self.operation_value)

            if relief:
                worry_level = self.relief_func(worry_level)
            else:
                worry_level %= factor

            passes_test = self.test_func(worry_level)
            target_monkey = self.true_monkey if passes_test else self.false_monkey

            self.monkey_list[target_monkey].items.append(worry_level)

        # Empty the list of items of the monkey
        self.items = []

    def reset_state(self) -> None:
        self.items = self.items_copy[:]
        self.examinated_items = 0

    def __repr__(self) -> None:
        return f"Monkey(Examinated={self.examinated_items}, Items={self.items})"


@parsing_benchmark
def parse_input(data: List[str]) -> List[Monkey]:
    monkeys = []

    for i in range(0, len(data), 7):
        items = map(lambda x: int(x), data[i + 1].split(": ")[1].split(", "))
        value = data[i + 2].split()[-1]

        if value == "old":
            value = None
            if "+" in data[i + 2]:
                operation = lambda x, y: 2 * x
            elif "*" in data[i + 2]:
                operation = lambda x, y: x * x
        else:
            value = int(value)
            if "+" in data[i + 2]:
                operation = lambda x, y: x + y
            elif "*" in data[i + 2]:
                operation = lambda x, y: x * y
        test_value = int(data[i + 3].split()[-1])
        true_monkey = int(data[i + 4].split()[-1])
        false_monkey = int(data[i + 5].split()[-1])
        # Monkey building 🐒🍌
        monkey = Monkey(
            items=list(items),
            operation=operation,
            operation_value=value,
            test_value=test_value,
            true_monkey=true_monkey,
            false_monkey=false_monkey,
            monkey_list=monkeys,
        )
        monkeys.append(monkey)

    return monkeys


@benchmark
def simulate_monkeys(
    monkeys: List[Monkey], rounds: int, relief: bool = True, factors: List[int] = []
) -> int:
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.examinate_items(relief, factors)
    examinated_ranking = sorted([monkey.examinated_items for monkey in monkeys])
    return examinated_ranking[-1] * examinated_ranking[-2]


data = get_input()
monkeys = parse_input(data)
factor = reduce(operator.mul, [m.test_value for m in monkeys])

print(f"Part 1: {simulate_monkeys(monkeys, 20)}")
[x.reset_state() for x in monkeys]
print(f"Part 2: {simulate_monkeys(monkeys, 10_000, False, factor)}")
