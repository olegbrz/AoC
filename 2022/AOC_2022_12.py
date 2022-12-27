#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queue import PriorityQueue
from aoc_helper import *
import numpy as np


data = get_input()


@parsing_benchmark
def parse_input(data: List[str]) -> np.ndarray:
    def letter_idx(letter: str) -> int:
        if letter == "S":
            return -1
        elif letter == "E":
            return -2
        else:
            return ord(letter) - ord("a")

    a = []
    for line in range(len(data)):
        temp_line = []
        for char in range(len(data[0])):
            temp_line.append(letter_idx(data[line][char]))
            if data[line][char] == "S":
                start = (line, char)
            elif data[line][char] == "E":
                end = (line, char)
        a.append(list)

    a = [list(map(letter_idx, line)) for line in data]

    return np.array(a, dtype=np.int8), start, end


def is_valid_move(current_position, target_position, grid):
    if grid[current_position] == -1:
        current_position = 0
        return grid[target_position] - current_position <= 1
    if grid[target_position] == -2:
        target_position = ord("z") - ord("a")
        return target_position - grid[current_position] <= 1
    return (grid[target_position] - grid[current_position]) <= 1


def is_valid_position(position, grid):
    return (
        position[0] >= 0
        and position[0] < len(grid)
        and position[1] >= 0
        and position[1] < len(grid[0])
    )


# Function that implements Dijkstra's algorithm to find the shortest path between two given positions in a 2D grid. The grid is represented as a 2D numpy array, but not all points are connected. The function returns the shortest path as a list of positions.
def dijkstra(grid, start, end):
    # Initialize the distance and visited arrays
    distance = np.full(grid.shape, np.inf)
    distance[start] = 0
    visited = np.full(grid.shape, False)
    # Initialize the queue
    queue = PriorityQueue()
    queue.put((0, start))
    # Loop until the queue is empty
    while not queue.empty():
        # Get the position with the lowest distance
        current_distance, current_position = queue.get()
        # If the position is already visited, skip it
        if visited[current_position]:
            continue
        # Mark the position as visited
        visited[current_position] = True
        # If the position is the target, return the distance
        if current_position == end:
            return current_distance
        # Get the neighbors of the current position
        neighbors = []
        for i in [1, 2, 3, 4]:
            if i == 1:
                new_position = (current_position[0], current_position[1] + 1)
            elif i == 2:
                new_position = (current_position[0] + 1, current_position[1])
            elif i == 3:
                new_position = (current_position[0], current_position[1] - 1)
            else:
                new_position = (current_position[0] - 1, current_position[1])
            if not is_valid_position(new_position, grid):
                continue
            else:
                neighbors.append(new_position)
        # Loop through the neighbors
        for neighbor in neighbors:
            # If the neighbor is not valid, skip it
            if not is_valid_move(current_position, neighbor, grid):
                continue
            # Calculate the new distance
            new_distance = current_distance + 1
            # If the new distance is lower than the old distance, update the distance and add the neighbor to the queue
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                queue.put((new_distance, neighbor))
    # If the queue is empty, the target is unreachable
    return np.inf


@benchmark
def find_minimum_cost(grid, start, end):
    shortest = dijkstra(grid, start, end)
    return shortest


@benchmark
def find_abs_minimum_cost(grid, end):
    points = [
        (i, j)
        for i in range(len(grid))
        for j in range(len(grid[0]))
        if grid[i, j] in [-1, 0]
    ]

    shortest_paths = [dijkstra(grid, p, end) for p in points]
    return min(shortest_paths)


if __name__ == "__main__":
    grid, start, end = parse_input(data)
    print(f"Part 1: {find_minimum_cost(grid, start, end)}")
    print(f"Part 2: {find_abs_minimum_cost(grid, end)}")
