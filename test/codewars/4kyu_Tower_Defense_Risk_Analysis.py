"""
https://www.codewars.com/kata/5a57faad880385f3b60000d0/train/python
"""


# TODO 1. get path. 2. get turrets. 3. get controlable
# 1. get path
#


class Path:
    def __init__(self, grid: list):
        self.grid = grid
        self.start = self.get_start_position()
        self.path = self.get_path()

    def get_start_position(self) -> tuple:
        for x, row in enumerate(self.grid):
            for y, cell in enumerate(row):
                if cell == '0':
                    return x, y

    def get_path(self) -> dict:
        path = {self.start: 0}
        visited = set()
        visited.add(self.start)
        to_visit = [self.start]
        while to_visit:
            point = to_visit.pop()
            neighbours = self.get_neighbours(point)
            for neighbour in neighbours:
                if neighbour not in visited:
                    path[neighbour] = 0
                    to_visit.append(neighbour)
                    visited.add(neighbour)
        return path

    def get_neighbours(self, point) -> list:
        neighbours = []
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for direction in directions:
            x = point[0] + direction[0]
            y = point[1] + direction[1]
            if x < 0 or y < 0:
                continue
            try:
                neighbour = self.grid[x][y]
            except IndexError:
                pass
            else:
                if neighbour == '1':
                    neighbours.append((x, y))
        return neighbours


class Turret:
    def __init__(self, name: str, power: list):
        self.name = name
        self.shots = power[1]
        self.radius = power[0]
        self.position = (0, 0)
        self.cells_under_fire = []

    def __repr__(self):
        return f'Turret ({self.name}): shots - {self.shots}, radius - {self.radius}, position - {self.position}, cells - {str(self.cells_under_fire)}'

    def add_cell_under_fire(self, cell: tuple):
        self.cells_under_fire.append(cell)


class TurretManager:
    def __init__(self, turrets):
        self.turrets = []
        for turret in turrets:
            self.turrets.append(Turret(turret, turrets[turret]))

    def __repr__(self):
        return '\n'.join(turret.__repr__() for turret in self.turrets)

    def update_turrets_position(self, grid: list):
        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if cell.isalpha():
                    for turret in self.turrets:
                        if turret.name == cell:
                            turret.position = (x, y)

    @staticmethod
    def calculate_distance(first_point, second_point):
        return ((first_point[0] - second_point[0]) ** 2 + (first_point[1] - second_point[1]) ** 2) ** 0.5

    def update_turrets_shooting_area(self, path: Path):
        for cell in reversed(path.path):
            for turret in self.turrets:
                if TurretManager.calculate_distance(cell, turret.position) <= turret.radius:
                    turret.add_cell_under_fire(cell)


def tower_defense(grid, turrets, aliens):
    path = Path(grid)
    turret_manager = TurretManager(turrets)
    turret_manager.update_turrets_position(grid)
    turret_manager.update_turrets_shooting_area(path)
    print(turret_manager)


g = [
    '0111111',
    '  A  B1',
    ' 111111',
    ' 1     ',
    ' 1C1111',
    ' 111 D1',
    '      1']
t = {'A': [3, 2], 'B': [1, 4], 'C': [2, 2], 'D': [1, 3]}
m = [30, 14, 27, 21, 13, 0, 15, 17, 0, 18, 26]


tower_defense(g, t, m)
