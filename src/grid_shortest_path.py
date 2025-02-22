from typing import List, Tuple, Optional
from collections import deque

def find_shortest_path(grid: List[List[str]]) -> Optional[List[Tuple[int, int]]]:
    """
    Find the shortest path from top-left to bottom-right corner of a grid.
    
    Args:
    grid (List[List[str]]): A 2D grid where '.' is empty, 'O' is blocking, '#' is path
    
    Returns:
    Optional[List[Tuple[int, int]]]: List of coordinates representing the shortest path,
    or None if no path exists
    """
    # Input validation
    if not grid or not grid[0]:
        return None
    
    rows, cols = len(grid), len(grid[0])
    
    # Check if start or end is blocked
    if grid[0][0] == 'O' or grid[rows-1][cols-1] == 'O':
        return None
    
    # Possible movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Queue for BFS
    queue = deque([(0, 0, [])])
    
    # Set to track visited cells
    visited = set([(0, 0)])
    
    while queue:
        x, y, path = queue.popleft()
        
        # Reached bottom-right corner
        if x == rows - 1 and y == cols - 1:
            return path + [(x, y)]
        
        # Try all 4 directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if new position is valid
            if (0 <= nx < rows and 
                0 <= ny < cols and 
                grid[nx][ny] != 'O' and 
                (nx, ny) not in visited):
                
                visited.add((nx, ny))
                new_path = path + [(x, y)]
                queue.append((nx, ny, new_path))
    
    # No path found
    return None