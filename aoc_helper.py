from genericpath import isdir
from sys import argv
from os.path import isfile, isdir
from os import mkdir
from requests import get
from json import load
from typing import List, Tuple, Union
from functools import wraps
import time


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def s_data() -> Tuple[int, int]:
    """s_data gets the AOC script year and data based on a defined script name
    format: "AOC-YYYY-DD.py", where YYYY is year and XX is day number-

    [extended_summary]

    Returns:
        Tuple[int, int]: year and day numbers.
    """
    year, day = map(int, argv[0].split("/")[-1].split(".")[0].split("_")[1:])
    return (year, day)


def get_input(
    year: int = s_data()[0], day: int = s_data()[1], as_string=False
) -> Union[List[str], str]:
    """get_input get the input data for a given year-day challenge of Advent of
    Code. The process is made through HTTP GET request, using AoC's session
    cookie.

    [extended_summary]

    Args:
        year (int, optional): year of challenge. Defaults to s_data()[0].
        day (int, optional): day of challenge. Defaults to s_data()[1].

    Returns:
        List[str]: all lines from input data.
    """
    if not isdir("cache"):
        mkdir("cache")
    possible_file = f"cache/AOC-{year}-{day}.txt"

    if isfile(possible_file):
        print(f"Using cached file {possible_file} as input")
        with open(possible_file) as t:
            res = t.read()
    else:
        # Load the cookie from .json
        with open("aoc_cookie.json") as c:
            data = load(c)
        headers = {"cookie": data["cookie"]}
        url = f"https://adventofcode.com/{year}/day/{day}/input"

        # HTTP GET data
        print(f"HTTP GET: {url}")
        r = get(url, headers=headers)
        res = r.text

        for i in ["Date", "Content-Type", "Content-Length", "Server-Ip"]:
            print(f"{i}: {r.headers[i]}")

        print(
            f"\nGET: {r.status_code}{' OK' if r.ok else ''}\n"
            + f"Input-Length: {len(res)}"
        )

        with open(possible_file, "w") as t:
            t.write(res)

        print(f"Stored input in {possible_file}")

    if not as_string:
        res = res.split("\n")[:-1]
    print("----------------------------------------------------")

    return res


def convert_time(t: float) -> Tuple[int, str]:
    if t < 0.000001:
        t, u = t * 1000000000, "ns"
    elif t < 0.001:
        t, u = t * 1000000, "µs"
    elif t < 1:
        t, u = t * 1000, "ms"
    elif t < 60:
        t, u = t, "sec"
    else:
        t, u = t / 60, "min"
    return (t, u)


def parsing_benchmark(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = function(*args, **kwargs)
        t2 = time.time()
        t, u = convert_time(t2 - t1)
        print(
            f"{bcolors.OKCYAN}┌─📝─PARSING────[{function.__name__ + '()]':─<30}⌛─[{t:6.2f} {u}]",
            end=f"\n└─> {bcolors.ENDC}Not neccesary to print\n",
        )
        return result

    return wrapper


def benchmark(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = function(*args, **kwargs)
        t2 = time.time()
        t, u = convert_time(t2 - t1)
        print(
            f"{bcolors.OKCYAN}┌─🖥️ ─COMPUTING──[{function.__name__ + '()]':─<30}⌛─[{t:6.2f} {u}]",
            end=f"\n└─> {bcolors.ENDC}",
        )
        return result

    return wrapper
