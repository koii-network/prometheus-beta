from typing import List, Tuple, Optional
from collections import deque

def find_shortest_path(grid: List[List[str]]) -> Optional[List[Tuple[int, int]]]:
    """
    Find the shortest path from top-left to bottom-right corner in a grid.
    
    Args:
        grid (List[List[str]]): A 2D grid where:
            '.' represents an empty cell
            'O' represents a blocked cell
            '#' represents a path cell
    
    Returns:
        Optional[List[Tuple[int, int]]]: A list of coordinates representing the 
        shortest path from top-left to bottom-right, or None if no path exists.
    
    Raises:
        ValueError: If the grid is empty or None
    """
    # Input validation
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    rows, cols = len(grid), len(grid[0])
    
    # Check grid is square
    if any(len(row) != cols for row in grid):
        raise ValueError("Grid must be square")
    
    # Possible movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Initialize visited and parent tracking
    visited = [[False] * cols for _ in range(rows)]
    parent = [[None] * cols for _ in range(rows)]
    
    # Start BFS from top-left corner
    queue = deque([(0, 0)])
    visited[0][0] = True
    
    while queue:
        current_row, current_col = queue.popleft()
        
        # Reached bottom-right corner
        if current_row == rows - 1 and current_col == cols - 1:
            # Reconstruct path
            path = []
            while (current_row, current_col) != (0, 0):
                path.append((current_row, current_col))
                current_row, current_col = parent[current_row][current_col]
            path.append((0, 0))
            return list(reversed(path))
        
        # Try all 4 directions
        for dr, dc in directions:
            next_row, next_col = current_row + dr, current_col + dc
            
            # Check bounds and valid move
            if (0 <= next_row < rows and 
                0 <= next_col < cols and 
                not visited[next_row][next_col] and 
                grid[next_row][next_col] != 'O'):
                
                queue.append((next_row, next_col))
                visited[next_row][next_col] = True
                parent[next_row][next_col] = (current_row, current_col)
    
    # No path found
    return None