"""
https://www.codewars.com/kata/5a57faad880385f3b60000d0/train/python
"""


class Cell:
    def __init__(self, position: tuple, monster_health=0):
        self.position = position
        self.monster_health = monster_health

    def __repr__(self):
        return f'(Cell: {self.position}, monster: {self.monster_health})'


class Path:
    def __init__(self, grid: list, monsters: list):
        self.grid = grid
        self.start = self.get_start_position()
        self.path = list(reversed(self.get_path()))
        self.monsters = list(reversed(monsters))
        self.passed = 0

    def __repr__(self):
        return '\n'.join([cell.__repr__() for cell in self.path])

    def __len__(self):
        return len(self.path)

    def get_start_position(self) -> Cell:
        for x, row in enumerate(self.grid):
            for y, cell in enumerate(row):
                if cell == '0':
                    return Cell((x, y))

    def get_path(self) -> list:
        path = [self.start]
        visited = set()
        visited.add(self.start.position)
        to_visit = [self.start.position]
        while to_visit:
            point = to_visit.pop()
            neighbours = self.get_neighbours(point)
            for neighbour in neighbours:
                if neighbour not in visited:
                    path.append(Cell(neighbour))
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

    def move_monsters(self):
        for idx, cell in enumerate(self.path[:-1]):
            cell.monster_health = self.path[idx + 1].monster_health
        if self.monsters:
            self.path[-1].monster_health = self.monsters.pop()
        else:
            self.path[-1].monster_health = 0

    def update_health_of_monsters_that_passed(self):
        self.passed += self.path[0].monster_health

    def is_path_clear(self):
        return not any([cell.monster_health for cell in self.path])

    def is_game_over(self):
        return True if self.is_path_clear() and not self.monsters else False


class Turret:
    def __init__(self, name: str, power: list):
        self.name = name
        self.shots = power[1]
        self.radius = power[0]
        self.position = (0, 0)
        self.cells_under_fire = []
        self.shots_left = self.shots

    def __repr__(self):
        return f'Turret ({self.name}): shots - {self.shots}, radius - {self.radius}, position - {self.position}, ' \
               f'cells - {str(self.cells_under_fire)}'

    def add_cell_under_fire(self, cell: tuple):
        self.cells_under_fire.append(cell)


class TurretManager:
    def __init__(self, turrets):
        self.turrets = []
        for turret in turrets:
            self.turrets.append(Turret(turret, turrets[turret]))
        self.turrets.sort(key=lambda x: x.name)
        self.rounds = max([turret.shots for turret in self.turrets])

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
        for cell in path.path:
            for turret in self.turrets:
                if TurretManager.calculate_distance(cell.position, turret.position) <= turret.radius:
                    turret.add_cell_under_fire(cell)

    def reload_turrets(self):
        for turret in self.turrets:
            turret.shots_left = turret.shots

    def shoot_turrets(self):
        for _ in range(self.rounds):
            for turret in self.turrets:
                if turret.shots_left:
                    for cell in turret.cells_under_fire:
                        if cell.monster_health > 0:
                            cell.monster_health -= 1
                            turret.shots_left -= 1
                            break
        self.reload_turrets()


def tower_defense(grid, turrets, aliens):
    path = Path(grid, aliens)
    turret_manager = TurretManager(turrets)
    turret_manager.update_turrets_position(grid)
    turret_manager.update_turrets_shooting_area(path)
    while not path.is_game_over():
        path.update_health_of_monsters_that_passed()
        path.move_monsters()
        turret_manager.shoot_turrets()
    return path.passed


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


assert tower_defense(g, t, m) == 10
