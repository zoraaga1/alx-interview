def island_perimeter(grid):
    # Initialize the perimeter count
    perimeter = 0
    
    # Dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    
    # Iterate over each cell in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell found
                # Check all four possible sides
                
                # Check the top
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                
                # Check the bottom
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                
                # Check the left
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                
                # Check the right
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1
    
    return perimeter
