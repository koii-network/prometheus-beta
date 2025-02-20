from typing import List, Tuple, Optional
from collections import deque

def find_shortest_path(maze: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """
    Find the shortest path through a maze from start to end.
    
    Args:
        maze (List[List[str]]): 2D grid representing the maze
                                 '.' represents a path
                                 '#' represents a wall
        start (Tuple[int, int]): Starting coordinates (row, col)
        end (Tuple[int, int]): Ending coordinates (row, col)
    
    Returns:
        Optional[List[Tuple[int, int]]]: Shortest path as a list of coordinates, 
                                         or None if no path exists
    """
    # Validate inputs
    if not maze or not maze[0]:
        return None
    
    rows, cols = len(maze), len(maze[0])
    
    # Check if start and end are valid
    if (not (0 <= start[0] < rows and 0 <= start[1] < cols) or 
        not (0 <= end[0] < rows and 0 <= end[1] < cols)):
        return None
    
    # Check if start or end are walls
    if (maze[start[0]][start[1]] == '#' or 
        maze[end[0]][end[1]] == '#'):
        return None
    
    # Possible movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Track visited cells and paths
    visited = set()
    queue = deque([(start, [start])])
    
    while queue:
        (current_row, current_col), path = queue.popleft()
        
        # Check if reached the end
        if (current_row, current_col) == end:
            return path
        
        # Mark current cell as visited
        visited.add((current_row, current_col))
        
        # Explore neighboring cells
        for d_row, d_col in directions:
            next_row = current_row + d_row
            next_col = current_col + d_col
            
            # Check if the next cell is valid
            if (0 <= next_row < rows and 
                0 <= next_col < cols and 
                maze[next_row][next_col] != '#' and 
                (next_row, next_col) not in visited):
                
                new_path = path + [(next_row, next_col)]
                queue.append(((next_row, next_col), new_path))
    
    # No path found
    return None