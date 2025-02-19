from typing import List
from collections import deque

def find_shortest_path(grid: List[List[int]]) -> int:
    """
    Find the shortest path in a 2D grid maze from top-left to bottom-right.
    
    Args:
    grid (List[List[int]]): An NxN grid where 0 represents open paths and 1 represents walls.
    
    Returns:
    int: Length of the shortest path from top-left to bottom-right, or -1 if no path exists.
    """
    # Check for invalid input
    if not grid or not grid[0]:
        return -1
    
    n = len(grid)
    
    # Check if start or end is blocked
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    # Possible movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Initialize visited set and queue for BFS
    visited = set([(0, 0)])
    queue = deque([(0, 0, 1)])  # (row, col, path_length)
    
    while queue:
        row, col, path_length = queue.popleft()
        
        # Reached bottom-right corner
        if row == n-1 and col == n-1:
            return path_length
        
        # Explore adjacent cells
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # Check if new position is valid
            if (0 <= new_row < n and 
                0 <= new_col < n and 
                grid[new_row][new_col] == 0 and 
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, path_length + 1))
    
    # No path found
    return -1