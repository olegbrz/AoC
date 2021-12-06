from aoc_helper import get_input, benchmark

input_ = get_input(as_string=True)[:-1]


@benchmark
def captcha(data, halfway=False):
    valid = []
    step = (len(data) // 2) if halfway else 1
    print(step)
    for i in range(len(data)):
        if data[i] == data[(i+step) % len(data)]:
            valid.append(int(data[i]))
    return sum(valid)


print(f"Part 1: {captcha(input_)}")
print(f"Part 2: {captcha(input_, halfway=True)}")
