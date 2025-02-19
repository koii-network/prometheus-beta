from typing import List, Tuple
from collections import deque

def find_shortest_path(grid: List[List[str]]) -> List[Tuple[int, int]]:
    """
    Find the shortest path from top-left to bottom-right corner in a grid.
    
    :param grid: 2D grid with '.' (empty), 'O' (blocking), and '#' (path) cells
    :return: List of coordinates representing the shortest path
    """
    # Check if grid is empty or invalid
    if not grid or not grid[0]:
        return []
    
    rows, cols = len(grid), len(grid[0])
    
    # Validate start and end points are empty
    if grid[0][0] == 'O' or grid[rows-1][cols-1] == 'O':
        return []
    
    # Possible movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Queue for BFS, storing (x, y, path)
    queue = deque([(0, 0, [(0, 0)])])
    
    # Track visited cells to avoid revisiting
    visited = set([(0, 0)])
    
    while queue:
        x, y, path = queue.popleft()
        
        # Reached bottom-right corner
        if x == rows - 1 and y == cols - 1:
            return path
        
        # Explore adjacent cells
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check boundaries, not visited, and not blocking cell
            if (0 <= nx < rows and 
                0 <= ny < cols and 
                (nx, ny) not in visited and 
                grid[nx][ny] != 'O'):
                
                new_path = path + [(nx, ny)]
                queue.append((nx, ny, new_path))
                visited.add((nx, ny))
    
    # No path found
    return []