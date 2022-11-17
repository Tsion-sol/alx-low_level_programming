#!/usr/bin/python3

"""
Island Perimeter module
"""


def island_perimeter(grid):
    """
    islan_perimeter(grid)

    Function that returns the perimeter of the island described in @grid
    grid is a list of list of integers:
    0 represents a water zone
    1 represents a land zone
    One cell is a square with side length 1
    Grid cells are connected horizontally/vertically (not diagonally).
    Grid is rectangular, width and height dont exceed 100
    Grid is completely surrounded by water, and there's one island (or nothing)
    The island doesnt have lakes.
    """
    if grid is None or grid == [] or grid == [[]]:
        return 0

    f_perim = sum([sum(r) for r in grid])
    f_perim = f_perim * 4
    rmv = 0
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == 1:
                if (r - 1) >= 0 and grid[r - 1][c] == 1:
                    rmv += 1
                    if (c - 1) >= 0 and grid[r][c - 1] == 1:
                        rmv += 1
                        rmv = rmv * 2
                        return f_perim - rmv
