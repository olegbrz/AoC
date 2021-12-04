from aoc_helper import benchmark, get_input
import numpy as np

input_ = get_input()
input_ = np.array(
    list(map(lambda x: [int(digit) for digit in str(x)], input_)))


@benchmark
def fuel_consumption(data: np.array) -> int:
    c = [np.unique(data[:, col], return_counts=True)[1]
         for col in range(len(data[0]))]

    gamma_rate = int(''.join(['0' if i[0] > i[1] else '1' for i in c]), 2)
    epsilon = int(''.join(['0' if i[0] < i[1] else '1' for i in c]), 2)

    return gamma_rate * epsilon


@benchmark
def life_support_rating(data: np.array) -> int:
    def binlist2int(x): return int(''.join(map(str, list(x[0]))), 2)
    def filter_array(array, col, val): return array[array[:, col] == val, :]
    o, c = np.copy(data), np.copy(data)

    for col in range(len(data[0])):
        o_col, c_col = list(o[:, col]), list(c[:, col])
        ogr_c, csr_c = [[o_col.count(0), o_col.count(1)], [
            c_col.count(0), c_col.count(1)]]

        o = filter_array(o, col, 0 if ogr_c[0] > ogr_c[1] else 1)

        if csr_c[0] and csr_c[0] <= csr_c[1]:
            c = filter_array(c, col, 0)
        elif csr_c[1]:
            c = filter_array(c, col, 1)

        oxy_gen_r, co2_scr_r = map(binlist2int, [o, c])

    return oxy_gen_r * co2_scr_r


print(f"Part 1: {fuel_consumption(input_)}")
print(f"Part 2: {life_support_rating(input_)}")
