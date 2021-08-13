"""
https://www.codewars.com/kata/5a57faad880385f3b60000d0/train/python
"""
# TODO 1. get path. 2. get turrets. 3. get controlable
# 1. get path
#


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __repr__(self):
        return f'Pos: x={self.x}, y={self.y}'


def tower_defense(grid, turrets, aliens):
    pass


def get_turrets_position(grid):
    turret_positions = {}
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell.isalpha():
                turret_positions[cell] = Pos(x, y)
    return turret_positions


def get_start_position(grid:list):
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == '0':
                return Pos(x, y)


def get_neighbours(start: Pos, grid: list):
    neighbours = []
    directions = (Pos(-1, 0), Pos(1, 0), Pos(0, -1), Pos(0, 1))
    for direction in directions:
        x = start.x + direction.x
        y = start.x + direction.y
        if x < 0 or y < 0:
            continue
        try:
            neighbour = grid[x][y]
        except IndexError:
            pass
        else:
            if neighbour == '1':
                neighbours.append(Pos(x, y))
    return neighbours


def get_path(grid: list, start: Pos):
    path = {start: 0}
    visited = set()
    visited.add(start)
    to_visit = [start]
    while to_visit:
        point = to_visit.pop()
        neighbours = get_neighbours(point, grid)
        for neighbour in neighbours:
            if neighbour not in visited:
                path[neighbour] = 0
                to_visit.append(neighbour)
                visited.add(neighbour)
    return path


grid_1 = [
    '0111111',
    '  A  B1',
    ' 111111',
    ' 1     ',
    ' 1C1111',
    ' 111 D1',
    '      1']

s = get_start_position(grid_1)
print(s)
print(get_path(grid_1, s))
