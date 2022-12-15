#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import *
import math


class Sensor:
    def __init__(self, sx: int, sy: int, bx: int, by: int) -> None:
        self.sensor_x = sx
        self.sensor_y = sy
        self.beacon_x = bx
        self.beacon_y = by
        self.sens_range()

    def sens_range(self) -> None:
        self.sens_range = manhattan_distance(
            self.sensor_x, self.sensor_y, self.beacon_x, self.beacon_y
        )

    def sens_interval(self, y: int) -> List[int]:
        y_diff = abs(y - self.sensor_y)
        if y_diff > self.sens_range:
            return []
        else:
            remain = self.sens_range - y_diff
            return [
                self.sensor_x - remain,
                self.sensor_x + remain,
            ]

    def get_max_x(self) -> int:
        return max(self.sensor_x, self.beacon_x)

    def get_max_y(self) -> int:
        return max(self.sensor_y, self.beacon_y)

    def get_min_x(self) -> int:
        return min(self.sensor_x, self.beacon_x)

    def get_min_y(self) -> int:
        return min(self.sensor_y, self.beacon_y)

    def __repr__(self) -> str:
        return f"Sensor(id={str(id(self))[-3:]}, pos=[x={self.sensor_x}, y={self.sensor_y}], range={self.sens_range}, assoc_beacon=[{self.beacon_x}, {self.beacon_y}])"


def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def get_limits(sensors: List[Sensor]) -> Tuple[int, int]:
    max_x, max_y = -math.inf, -math.inf
    min_x, min_y = math.inf, math.inf
    for s in sensors:
        s_max_x, s_max_y = s.get_max_x(), s.get_max_y()
        s_min_x, s_min_y = s.get_min_x(), s.get_min_y()
        max_x = s_max_x if s_max_x > max_x else max_x
        max_y = s_max_y if s_max_y > max_y else max_y
        min_x = s_min_x if s_min_x < min_x else min_x
        min_y = s_min_y if s_min_y < min_y else min_y
    return (min_x, max_x, min_y, max_y)


@parsing_benchmark
def parse_input(data):
    sensors = []
    for line in data:
        line = line.replace(",", "").replace(":", "").split()
        sx = int(line[2].replace("x=", ""))
        sy = int(line[3].replace("y=", ""))
        bx = int(line[8].replace("x=", ""))
        by = int(line[9].replace("y=", ""))
        sensors.append(Sensor(sx, sy, bx, by))
    return sensors


def get_beacons(sensors: List[Sensor]) -> List[Tuple[int, int]]:
    beacons = []
    for s in sensors:
        beacons.append((s.beacon_x, s.beacon_y))
    return beacons


@benchmark
def compute_inaccesible(sensors: List[Sensor], y: int = 2_000_000) -> int:
    ranges = get_intersection(
        [s.sens_interval(y) for s in sensors if s.sens_interval(y)]
    )
    return sum([r[1] - r[0] for r in ranges])


# Function that given a list of points in format [start, end] returns the intersection of the intervals in form of non overlapping intervals of same format
def get_intersection(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    intersection = []
    for interval in intervals:
        if not intersection:
            intersection.append(interval)
        else:
            if intersection[-1][1] >= interval[0]:
                intersection[-1][1] = max(intersection[-1][1], interval[1])
            else:
                intersection.append(interval)
    return intersection


def search_lost_beacon(sensors: List[Sensor]) -> int:
    beacon_freq = lambda x, y: x * 4_000_000 + y
    for y in range(3_000_000, 4_000_000):
        intersec = get_intersection(
            [s.sens_interval(y) for s in sensors if s.sens_interval(y)]
        )
        # If the range breaks in two intersections, the beacon can be placed in the middle
        if len(intersec) > 1:
            return intersec[0][-1] + 1, y


@benchmark
def lost_beacon_freq(sensors: List[Sensor]) -> int:
    x, y = search_lost_beacon(sensors)
    return x * 4_000_000 + y


if __name__ == "__main__":
    sensors = parse_input(get_input())
    [print(s) for s in sensors]
    print(f"Part 1: {compute_inaccesible(sensors)}")
    print(f"Part 2: {lost_beacon_freq(sensors)}")
