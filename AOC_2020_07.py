"""--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. In fact, it
looks like you'll even have time to grab some food: all flights are currently
delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being
enforced about bags and their contents; bags must be color-coded and must
contain specific quantities of other color-coded bags. Apparently, nobody
responsible for these regulations considered how long they would take to
enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types. In this example,
every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded
blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag,
how many different bag colors would be valid for the outermost bag? (In other
words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some
other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of
which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of
which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at
least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? (The
list of rules is quite long; make sure you get all of it.)

--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices,
but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black
bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black
bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags
within it) plus 2 vibrant plum bags (and the 11 bags within each of those):

1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper
than this example; be sure to count all of the bags, even if the nesting
becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
"""

from aoc_helper import get_input
from typing import Dict, List
data = get_input()


def data_to_json(data: List[str]) -> Dict[str, Dict]:
    """data_to_json transforms input data to a dictionary with bag colors and
    the colors they can contain.

    Args:
        data (List[str]): list of strings from the input.

    Returns:
        dict[str, Dict]: dictionary with bag colors as keys and dictionaries
        with the colors the can contain and the number of them as value.
    """
    bags_dict = {}
    for line in data:
        temp = {}
        line = line.split(' bags contain ')
        color = line[0]
        bags = line[1].replace('.', '').replace(
            'bags', '').replace('bag', '').strip().split(' , ')
        if 'no other' not in bags:
            for bag in bags:
                value = int(bag[0])
                key = bag[2:]
                temp[key] = value
        bags_dict[color] = temp
    return bags_dict


def contains(color: str, bags_dict: Dict[str, Dict], counter: int = 0) -> bool:
    """contains returns if the bag of a given color can contain shiny gold
    bags.

    Args:
        color (str): the target color
        bags_dict (Dict[str, Dict]): dictionary with the rules of bags colors.
        counter (int, optional): The variable to count the number of matches.
        Defaults to 0.

    Returns:
        bool: if the color can contain the shiny gold bag or not.
    """
    if any(['shiny gold' in bags_dict[color].keys()]):
        return True
    elif not bags_dict[color].keys():
        return False
    for bag in bags_dict[color]:
        counter += contains(bag, bags_dict, counter)
    return bool(counter)


def contains2(color: str, bags_dict: Dict[str, Dict], counter: int = 0) -> int:
    """contains2 computes the number of bags required inside the shiny golden
    bag.

    Args:
        color (str): target color
        bags_dict (Dict[str, Dict]):  dictionary with the rules of bags colors.
        counter (int, optional): number of bags required. Defaults to 0.

    Returns:
        int: [description]
    """
    if not bags_dict[color]:
        return 1
    for bag in bags_dict[color]:
        counter += (bags_dict[color][bag] * contains2(bag, bags_dict, 0))
    return counter + 1


bags_dict = data_to_json(data)

count1 = sum([contains(color, bags_dict) for color in bags_dict])
count2 = contains2('shiny gold', bags_dict) - 1


print(f'Result: {count1}')
print(f'Result: {count2}')