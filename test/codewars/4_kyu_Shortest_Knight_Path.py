"""
https://www.codewars.com/kata/shortest-knight-path/train/python
max moves = 6
"""
possible_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


def knight(p1, p2):
    x, y = subtract_points(p1, p2)
    _, _, moves = count_moves(x, y, 0)
    return moves


def subtract_points(p1, p2):
    y = abs(int(p1[1]) - int(p2[1]))
    x = abs(ord(p1[0]) - ord(p2[0]))
    return x, y


def count_moves(x, y, count):
    if x + y < 3:
        x, y = max(x, y), min(x, y)
        if x == 0:
            pass
        elif x == 1:
            count += 3
        elif x == 2:
            count += 3
        else:
            count += 2
        return x, y, count
    else:
        x, y = max(x, y), min(x, y)
        _, _, count = count_moves(abs(x - 2), abs(y - 1), count + 1)
        return x, y, count




print(knight("a1", "f1"))
print(subtract_points("a1", "f1"))
