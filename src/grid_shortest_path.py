from typing import List, Tuple, Optional
from collections import deque

def find_shortest_path(grid: List[List[str]]) -> Optional[List[Tuple[int, int]]]:
    """
    Find the shortest path from top-left to bottom-right corner of a grid.
    
    Args:
    grid (List[List[str]]): A 2D grid with '.' (empty), 'O' (blocking), and '#' (path) cells
    
    Returns:
    Optional[List[Tuple[int, int]]]: A list of coordinates representing the shortest path,
    or None if no path exists
    """
    # Check for empty or invalid grid
    if not grid or not grid[0]:
        return None
    
    # Grid dimensions
    rows, cols = len(grid), len(grid[0])
    
    # Check if start or end is blocked
    if grid[0][0] == 'O' or grid[rows-1][cols-1] == 'O':
        return None
    
    # Possible movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Queue for BFS: (row, col, path)
    queue = deque([(0, 0, [(0, 0)])])
    
    # Track visited cells to avoid revisiting
    visited = set([(0, 0)])
    
    while queue:
        curr_row, curr_col, path = queue.popleft()
        
        # Reached bottom-right corner
        if curr_row == rows - 1 and curr_col == cols - 1:
            return path
        
        # Try all 4 directions
        for dx, dy in directions:
            next_row, next_col = curr_row + dx, curr_col + dy
            
            # Check if next cell is valid
            if (0 <= next_row < rows and 
                0 <= next_col < cols and 
                grid[next_row][next_col] != 'O' and 
                (next_row, next_col) not in visited):
                
                # Add to queue with updated path
                new_path = path + [(next_row, next_col)]
                queue.append((next_row, next_col, new_path))
                visited.add((next_row, next_col))
    
    # No path found
    return None