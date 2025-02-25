"""
Identifying Invasive Weeds in the Park


Challenge

Medium
Create a function named identify_invasive_weeds that receives park_grid and weed_patterns as its parameters.

This function aims to identify invasive weeds in a park based on their growth patterns. The park is represented as a 2D grid, where each cell contains a single character representing a plant species. The function will search the grid for specific weed patterns provided and mark the cells that are part of a weed pattern with 'W'.

To solve this challenge, you need to:

Iterate through each cell in the park_grid.
For each cell, check if it is the starting point of any of the weed_patterns.
If a cell is the starting point of a weed pattern, mark all the cells that are part of that pattern with 'W'.
If a cell is not part of any weed pattern, keep the original character in the cell.
Return the updated park_grid with the invasive weeds marked.
Consider the following:

The weed patterns can be found horizontally, vertically, or diagonally in the grid.
A cell can be part of multiple weed patterns.
The grid dimensions can vary, but you can assume it is always rectangular.
Parameters:

park_grid (list of lists of str): A 2D grid representing the park, where each cell contains a single character representing a plant species.
weed_patterns (list of str): A list of strings, where each string represents the growth pattern of a different invasive weed.
The function returns a 2D list of strings (list of lists of str) which is the updated park grid with 'W' marking the cells that are part of an invasive weed pattern.
"""

def identify_invasive_weeds(park_grid, weed_patterns):
    rows = len(park_grid)
    cols = len(park_grid[0])

    def mark_weed(row, col, pattern):
        for i in range(len(pattern)):
            if row + i < rows and col + i < cols and park_grid[row + i][col + i] == pattern[i]:
                park_grid[row + i][col + i] = 'W'
            else:
                return

    for row in range(rows):
        for col in range(cols):
            for pattern in weed_patterns:
                if park_grid[row][col] == pattern[0]:
                    # Check horizontally
                    if col + len(pattern) <= cols:
                        mark_weed(row, col, pattern)
                    # Check vertically
                    if row + len(pattern) <= rows:
                        mark_weed(col, row, pattern)
                    # Check diagonally
                    if row + len(pattern) <= rows and col + len(pattern) <= cols:
                        mark_weed(row, col, pattern)

    return park_grid
