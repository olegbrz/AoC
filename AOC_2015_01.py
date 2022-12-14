from aoc_helper import get_input

input_ = get_input(as_string=True)


def get_floor(data: str) -> int:
    return data.count('(') - data.count(')')


def get_negative_floor(data: str) -> int:
    floor = 0
    for instruction in range(len(data)):
        if data[instruction] == "(":
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            return instruction + 1


print(f"Part 1: {get_floor(input_)}")
print(f"Part 2: {get_negative_floor(input_)}")
