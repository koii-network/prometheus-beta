from typing import List, Optional
from collections import deque

def find_shortest_grid_path(grid: List[List[int]]) -> Optional[int]:
    """
    Find the shortest path from top-left to bottom-right in a grid with movement constraints.
    
    Movement rules:
    - Can only move right or down
    - Can only move to an empty cell (0)
    - If right is blocked, must move down
    
    Args:
        grid (List[List[int]]): A 2D grid of 0s and 1s where 0 is an empty cell and 1 is blocked
    
    Returns:
        Optional[int]: Length of the shortest path, or None if no path exists
    
    Raises:
        ValueError: If the grid is empty or not square
    """
    # Validate input
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    # Check if grid is square
    n = len(grid)
    if any(len(row) != n for row in grid):
        raise ValueError("Grid must be square")
    
    # If start or end is blocked, no path exists
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return None
    
    # BFS to find shortest path
    queue = deque([(0, 0, 1)])  # (row, col, path_length)
    visited = set([(0, 0)])
    
    while queue:
        row, col, path_length = queue.popleft()
        
        # Reached bottom-right
        if row == n-1 and col == n-1:
            return path_length
        
        # Try moving right first (if possible)
        if col + 1 < n and grid[row][col+1] == 0 and (row, col+1) not in visited:
            queue.append((row, col+1, path_length + 1))
            visited.add((row, col+1))
        
        # Always try moving down
        if row + 1 < n and grid[row+1][col] == 0 and (row+1, col) not in visited:
            queue.append((row+1, col, path_length + 1))
            visited.add((row+1, col))
    
    # No path found
    return None