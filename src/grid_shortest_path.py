from typing import List, Tuple
from collections import deque

def find_shortest_path(grid: List[List[str]]) -> List[Tuple[int, int]]:
    """
    Find the shortest path from top-left to bottom-right corner of a grid.
    
    Args:
    - grid: A 2D list of strings representing the grid
             '.' represents empty cell
             'O' represents blocked cell
             '#' can represent part of the path (though not used in input)
    
    Returns:
    - A list of (row, col) tuples representing the shortest path
    - Returns an empty list if no path exists
    """
    # Validate input
    if not grid or not grid[0]:
        return []
    
    rows, cols = len(grid), len(grid[0])
    
    # Check if start or end is blocked
    if grid[0][0] == 'O' or grid[rows-1][cols-1] == 'O':
        return []
    
    # Possible movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Queue for BFS
    queue = deque([(0, 0, [(0, 0)])])
    
    # Track visited cells to avoid revisiting
    visited = set([(0, 0)])
    
    while queue:
        curr_row, curr_col, path = queue.popleft()
        
        # Reached the bottom-right corner
        if curr_row == rows - 1 and curr_col == cols - 1:
            return path
        
        # Try all 4 directions
        for d_row, d_col in directions:
            next_row = curr_row + d_row
            next_col = curr_col + d_col
            
            # Check if the next cell is valid
            if (0 <= next_row < rows and 
                0 <= next_col < cols and 
                grid[next_row][next_col] != 'O' and 
                (next_row, next_col) not in visited):
                
                # Create new path by adding the new cell
                new_path = path + [(next_row, next_col)]
                
                # Add to queue and mark as visited
                queue.append((next_row, next_col, new_path))
                visited.add((next_row, next_col))
    
    # No path found
    return []