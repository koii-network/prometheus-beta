from typing import List, Tuple, Optional
from collections import deque

def find_shortest_path(maze: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """
    Find the shortest path through a maze from start to end.
    
    Args:
        maze (List[List[str]]): 2D grid representing the maze
                                '#' represents walls
                                '.' represents open path
        start (Tuple[int, int]): Starting coordinates (row, col)
        end (Tuple[int, int]): Ending coordinates (row, col)
    
    Returns:
        Optional[List[Tuple[int, int]]]: Shortest path from start to end, 
                                         or None if no path exists
    """
    # Validate input
    if not maze or not maze[0]:
        return None
    
    rows, cols = len(maze), len(maze[0])
    
    # Validate start and end are within maze and not walls
    if (not (0 <= start[0] < rows and 0 <= start[1] < cols) or 
        not (0 <= end[0] < rows and 0 <= end[1] < cols) or 
        maze[start[0]][start[1]] == '#' or 
        maze[end[0]][end[1]] == '#'):
        return None
    
    # Possible move directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Track visited cells and path
    visited = set([start])
    queue = deque([(start, [start])])
    
    while queue:
        current, path = queue.popleft()
        
        # Check if reached end
        if current == end:
            return path
        
        # Try all 4 directions
        for dx, dy in directions:
            next_row, next_col = current[0] + dx, current[1] + dy
            
            # Check if next cell is valid and not visited
            if (0 <= next_row < rows and 
                0 <= next_col < cols and 
                maze[next_row][next_col] != '#' and 
                (next_row, next_col) not in visited):
                
                new_path = path + [(next_row, next_col)]
                queue.append(((next_row, next_col), new_path))
                visited.add((next_row, next_col))
    
    # No path found
    return None