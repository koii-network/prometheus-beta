from typing import List, Tuple, Optional
from collections import deque

def find_shortest_path(maze: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """
    Find the shortest path through a maze from start to end.
    
    Args:
        maze (List[List[str]]): 2D grid representing the maze
        start (Tuple[int, int]): Starting coordinates (row, col)
        end (Tuple[int, int]): Ending coordinates (row, col)
    
    Returns:
        Optional[List[Tuple[int, int]]]: Shortest path as a list of coordinates, 
        or None if no path exists
    
    Rules:
    - '.' represents an open path
    - '#' represents a wall
    - Path can move up, down, left, right (4-directional movement)
    - Coordinates are zero-indexed
    """
    # Input validation
    if not maze or not maze[0]:
        return None
    
    rows, cols = len(maze), len(maze[0])
    
    # Validate start and end coordinates
    if not (0 <= start[0] < rows and 0 <= start[1] < cols and
            0 <= end[0] < rows and 0 <= end[1] < cols):
        return None
    
    # Check if start or end is a wall
    if (maze[start[0]][start[1]] == '#' or 
        maze[end[0]][end[1]] == '#'):
        return None
    
    # Possible movement directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Track visited cells and previous steps
    visited = set()
    previous = {}
    
    # BFS queue
    queue = deque([start])
    visited.add(start)
    
    while queue:
        current = queue.popleft()
        
        # Reached the end
        if current == end:
            # Reconstruct path
            path = []
            while current in previous:
                path.append(current)
                current = previous[current]
            path.append(start)
            return list(reversed(path))
        
        # Try all 4 directions
        for dx, dy in directions:
            next_row, next_col = current[0] + dx, current[1] + dy
            
            # Check if new position is valid
            if (0 <= next_row < rows and 
                0 <= next_col < cols and 
                maze[next_row][next_col] == '.' and 
                (next_row, next_col) not in visited):
                
                queue.append((next_row, next_col))
                visited.add((next_row, next_col))
                previous[(next_row, next_col)] = current
    
    # No path found
    return None