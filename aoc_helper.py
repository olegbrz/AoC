from genericpath import isdir
from sys import argv
from os.path import isfile, isdir
from os import mkdir
from requests import get
from json import load
from typing import List, Tuple


def s_data() -> Tuple[int, int]:
    """s_data gets the AOC script year and data based on a defined script name
    format: "AOC-YYYY-DD.py", where YYYY is year and XX is day number-

    [extended_summary]

    Returns:
        Tuple[int, int]: year and day numbers.
    """
    year, day = map(int, argv[0].split('/')[-1].split('.')[0].split('-')[1:])
    return (year, day)


def get_input(year: int = s_data()[0], day: int = s_data()[1], as_string=False) -> List[str]:
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
        with open('aoc_cookie.json') as c:
            data = load(c)
        headers = {'cookie': data['cookie']}
        url = f"https://adventofcode.com/{year}/day/{day}/input"

        # HTTP GET data
        print(f"HTTP GET: {url}")
        r = get(url, headers=headers)
        res = r.text

        for i in ["Date", "Content-Type", "Content-Length", "Server-Ip"]:
            print(f"{i}: {r.headers[i]}")

        print(f"\nGET: {r.status_code}{' OK' if r.ok else ''}\n" +
              f"Input-Length: {len(res)}")

        with open(possible_file, "w") as t:
            t.write(res)

        print(f"Stored input in {possible_file}")

    if not as_string:
        res = res.split('\n')[:-1]
    print("----------------------------------------------------")

    return res
