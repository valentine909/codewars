"""
https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python
"""


def validate_battlefield(field):
    ships = []
    for i, row in enumerate(field):
        for j, cell in enumerate(row):
            if cell == 1:  # Ship first met
                if _connected_diagonals(i, j, field):
                    return False
                cell = 2  # Mark the ship's starting position
                # Get ship's size and update the field with fully marked ship(1 -> 2):
                field, ship_size = _get_ship_size(i, j, field)
                ships.append(ship_size)
    return sorted(ships) == [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]


def _connected_diagonals(row, column, field):
    corners = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for i, j in corners:
        if 0 <= row + i <= 9 and 0 <= column + j <= 9:
            if field[row + i][column + j] > 0:
                return True
    return False


def _get_ship_size(i, j, field):  # ship can expand only to the right or bottom from the first accounted position
    field, ship_size_vertical = _label_ship(i, j, field, (0, 1))
    field, ship_size_horizontal = _label_ship(i, j, field, (1, 0))
    ship_size = max(ship_size_vertical + 1, ship_size_horizontal + 1)  # +1 to consider the starting cell
    return field, ship_size


def _label_ship(i, j, field, direction, size=0):
    if i + direction[0] <= 9 and j + direction[1] <= 9:
        if field[i + direction[0]][j + direction[1]] == 1:
            field[i + direction[0]][j + direction[1]] = 2  # Mark the ship to skip it later
            size += 1
            field, size = _label_ship(i + direction[0], j + direction[1], field, direction, size=size)
    return field, size


battleField1 = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

battleField = [[0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 1, 1, 1, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 1, 0]]

print(validate_battlefield(battleField1))
print(validate_battlefield(battleField))
