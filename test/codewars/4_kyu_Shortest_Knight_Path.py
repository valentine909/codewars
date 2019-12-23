"""
https://www.codewars.com/kata/shortest-knight-path/train/python
BFS algorithm.
"""
from collections import deque
N = 8


def knight(p1, p2):
    start, end = convert_positions(p1, p2)
    moves = count_moves(start, end)
    return moves


def convert_positions(p1, p2):
    start = (ord(p1[0]) - ord("a") + 1, int(p1[1]))
    end = (ord(p2[0]) - ord("a") + 1, int(p2[1]))
    return start, end


def is_right(position, table):
    if (1 <= position[0] <= N) and (1 <= position[1] <= N) and position not in table:
        return True
    else:
        return False


def count_moves(start, end):
    possible_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    history = [start]
    queue = deque()
    queue.append((start, 0))
    while queue:
        point, moves = queue.popleft()
        if point == end:
            return moves
        for i in possible_moves:
            position = (point[0] + i[0], point[1] + i[1])
            if is_right(position, history):
                history.append(position)
                queue.append((position, moves + 1))




print(knight("a1", "f1"))
# print(convert_positions("a1", "f1"))
