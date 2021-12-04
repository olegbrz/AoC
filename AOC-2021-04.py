from typing import List
from aoc_helper import get_input
import numpy as np

input_ = get_input()


def get_numbers(data: List[str]) -> List[int]:
    return list(map(int, data[0].split(',')))


def get_boards(data: List[str]) -> List[np.array]:
    boards, tmp_board = [], []
    for line in data[2:]:
        if line:
            tmp_board.append(list(map(int, line.split())))
        else:
            boards.append(np.array(tmp_board))
            tmp_board = []
    if tmp_board:
        boards.append(np.array(tmp_board))
    return boards


def check_board(board: np.array) -> bool:
    for row in board:
        if np.all(row < 0):
            return True
    for col in range(board.shape[1]):
        if np.all(board[:, col] < 0):
            return True
    return False


def giant_squid(data: List[str], find_last: bool = False) -> int:
    numbers, boards = get_numbers(data), get_boards(data)
    wins = []
    found = False
    i = 0
    while (find_last or not found) and i < len(numbers):
        winners = []
        for idx, board in enumerate(boards):
            board[np.where(board == numbers[i])] = -1
            if check_board(board):
                found = True
                wins.append(np.sum(board[board > 0] * numbers[i]))
                winners.append(idx)
        if find_last and winners:
            [boards.pop(j) for j in sorted(winners, reverse=True)]
        i += 1
    return wins[-1]


print(f"Part 1: {giant_squid(input_)}")
print(f"Part 2: {giant_squid(input_, find_last=True)}")
