# pylint: disable=missing-docstring
def valid_group(values):
    """
    Return True if values contain exactly numbers 1-9 with no repetition.
    """
    if len(values) != 9:
        return False

    for v in values:
        if type(v) is not int:
            return False
        if v <1 and v>9:
            return False
    return set(values) == set(range(1, 10))

def sudoku_validator(grid):
    """
    Check the rows and columns for it is appropariate for sudoku rules.
    """
    # Shape control
    if type(grid) is not list or len(grid) != 9:
        return False

    # Row control
    for row in grid:
        if not isinstance(row, list) or len(row) != 9:
            return False
        if not valid_group(row):
            return False

    # Column control
    for col_idx in range(9):
        column = [grid[row_idx][col_idx] for row_idx in range(9)]

        if not valid_group(column):
            return False

    # 4) 3x3 boxes
    for row_start in (0, 3, 6):
        for column_start in (0, 3, 6):
            box = []
            for r in range(row_start, row_start + 3):
                for c in range(column_start, column_start + 3):
                    box.append(grid[r][c])
            if not valid_group(box):
                return False

    return True
