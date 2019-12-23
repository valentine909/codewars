"""
https://www.codewars.com/kata/shortest-knight-path/train/python
BFS algorithm.
"""
from collections import deque
N = 8  # Chess desk dimensions.


def knight(p1, p2):
    """
    Main function. Takes starting and ending positions in algebraic notation. Returns minimum number of moves.
    :param p1: Starting position, ex. "a1"
    :param p2: Ending position, ex. "f1"
    :return: Number of moves. Integer.
    """
    start, end = map(convert_positions, (p1, p2))
    return count_moves(start, end)


def convert_positions(point):
    """
    Converts desk position in algebraic notation to integer coordinates as tuple
    """
    return ord(point[0]) - 96, int(point[1])


def is_right(position, table):
    """
    Checks if position is within the desk and hasn't visited yet.
    :param position: Current position. Tuple.
    :param table: Global history of moves. List.
    """
    if (1 <= position[0] <= N) and (1 <= position[1] <= N) and position not in table:
        return True
    else:
        return False


def count_moves(start, end):
    """
    All possible moves are added to queue and processed FIFO.
    When the match with end position is found returns number of moves.
    """
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
