from typing import List, Tuple
from collections import deque

def find_shortest_path(grid: List[List[str]]) -> List[Tuple[int, int]]:
    """
    Find the shortest path from top-left to bottom-right corner of a grid.
    
    Args:
        grid (List[List[str]]): A 2D grid with '.' (empty), 'O' (blocking), '#' (path)
    
    Returns:
        List[Tuple[int, int]]: Coordinates of the shortest path from top-left to bottom-right
        Returns an empty list if no path exists.
    """
    # Check if grid is empty
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
        x, y, path = queue.popleft()
        
        # Reached bottom-right corner
        if x == rows - 1 and y == cols - 1:
            return path
        
        # Explore all 4 directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if new position is valid
            if (0 <= nx < rows and 
                0 <= ny < cols and 
                grid[nx][ny] != 'O' and 
                (nx, ny) not in visited):
                
                # Add new position to queue
                new_path = path + [(nx, ny)]
                queue.append((nx, ny, new_path))
                visited.add((nx, ny))
    
    # No path found
    return []