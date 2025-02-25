from typing import List, Tuple
from collections import deque

def find_shortest_path(grid: List[List[str]]) -> List[Tuple[int, int]]:
    """
    Find the shortest path from top-left to bottom-right corner of a grid.
    
    Args:
        grid (List[List[str]]): A 2D grid where:
            '.' represents an empty cell
            'O' represents a blocked cell
            '#' is not used in input, but used in path tracking
    
    Returns:
        List[Tuple[int, int]]: Coordinates of the shortest path from start to end
        
    Raises:
        ValueError: If grid is empty or invalid
        ValueError: If no path exists
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
    
    # Start and end coordinates
    start = (0, 0)
    end = (rows - 1, cols - 1)
    
    # Visited tracking and path reconstruction
    visited = set()
    parent = {}
    
    # BFS queue
    queue = deque([start])
    visited.add(start)
    
    while queue:
        current = queue.popleft()
        
        # Reached the end
        if current == end:
            # Reconstruct path
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return list(reversed(path))
        
        # Check all possible moves
        for dx, dy in directions:
            next_x, next_y = current[0] + dx, current[1] + dy
            
            # Check bounds and validity of move
            if (0 <= next_x < rows and 
                0 <= next_y < cols and 
                grid[next_x][next_y] != 'O' and 
                (next_x, next_y) not in visited):
                
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
                parent[(next_x, next_y)] = current
    
    # No path found
    raise ValueError("No path exists between start and end")