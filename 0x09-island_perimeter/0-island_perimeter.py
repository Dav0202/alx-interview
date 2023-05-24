#!/usr/bin/python3

''' island perimeter module '''


def island_perimeter(grid):
    # Initialize perimeter to 0
    perimeter = 0
    
    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                # Check the cell's neighbors and add to perimeter accordingly
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if i == len(grid)-1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == len(grid[i])-1 or grid[i][j+1] == 0:
                    perimeter += 1
    
    return perimeter
