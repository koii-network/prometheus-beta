from typing import List
from collections import deque

def shortest_path_in_maze(grid: List[List[int]]) -> int:
    """
    Find the shortest path in an NxN grid from top-left to bottom-right.
    
    Args:
        grid (List[List[int]]): A 2D grid where 0 represents open paths and 1 represents walls
    
    Returns:
        int: Length of the shortest path or -1 if no path exists
    """
    # Check for empty or invalid grid
    if not grid or not grid[0]:
        return -1
    
    n = len(grid)
    
    # Check if start or end is blocked
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    # Possible moves: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Create a queue for BFS
    queue = deque([(0, 0, 1)])  # (row, col, path_length)
    
    # Track visited cells to avoid revisiting
    visited = set([(0, 0)])
    
    while queue:
        row, col, path_length = queue.popleft()
        
        # Reached bottom-right
        if row == n - 1 and col == n - 1:
            return path_length
        
        # Try all four directions
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # Check if new position is valid
            if (0 <= new_row < n and 
                0 <= new_col < n and 
                grid[new_row][new_col] == 0 and 
                (new_row, new_col) not in visited):
                
                queue.append((new_row, new_col, path_length + 1))
                visited.add((new_row, new_col))
    
    # No path found
    return -1