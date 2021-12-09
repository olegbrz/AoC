from aoc_helper import benchmark, get_input
from concurrent import futures
from os import cpu_count
import hashlib


def brute_force_md5(secret_key, number_of_zeroes, interval):
    for i in interval:
        result = hashlib.md5(f"{secret_key}{i}".encode('utf-8')).hexdigest()
        if result.startswith('0' * number_of_zeroes):
            return i


@benchmark
def md5bf_multithread(secret_key, number_of_zeroes, max_lookup_value):
    threads = cpu_count()
    with futures.ProcessPoolExecutor(max_workers=threads) as executor:
        results, pool = [], []
        for thread in range(threads):
            interval = range(
                1 + thread, max_lookup_value + thread, threads)
            process = executor.submit(brute_force_md5, secret_key,
                                      number_of_zeroes, interval)
            pool.append(process)
        futures.wait(pool, return_when=futures.ALL_COMPLETED)
        results = [process.result() for process in pool if process.result()]

    return min(results)


input_ = get_input(as_string=True).replace('\n', '')

print(f"Part 1: {md5bf_multithread(input_, 5, 1_000_000)}")
print(f"Part 2: {md5bf_multithread(input_, 6, 10_000_000)}")
