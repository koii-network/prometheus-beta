from typing import List
from collections import deque

def find_shortest_path(grid: List[List[int]]) -> int:
    """
    Find the shortest path from top-left to bottom-right in a 2D grid maze.
    
    Args:
        grid (List[List[int]]): An NxN grid where 0 represents open paths and 1 represents walls.
    
    Returns:
        int: Length of the shortest path, or -1 if no path exists.
    """
    # Check input validity
    if not grid or not grid[0]:
        return -1
    
    n = len(grid)
    
    # Boundary checks
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    # Possible move directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Track visited cells and queue for BFS
    visited = [[False]*n for _ in range(n)]
    queue = deque([(0, 0, 0)])  # (row, col, distance)
    visited[0][0] = True
    
    while queue:
        row, col, distance = queue.popleft()
        
        # Reached bottom-right
        if row == n-1 and col == n-1:
            return distance
        
        # Try all 4 directions
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # Check if new position is valid
            if (0 <= new_row < n and 
                0 <= new_col < n and 
                grid[new_row][new_col] == 0 and 
                not visited[new_row][new_col]):
                
                queue.append((new_row, new_col, distance + 1))
                visited[new_row][new_col] = True
    
    # No path found
    return -1