from typing import List, Tuple
from collections import deque

def find_shortest_path(maze: List[List[int]]) -> int:
    """
    Find the shortest path through a maze from top-left to bottom-right.
    
    Args:
        maze (List[List[int]]): A 2D grid where 0 represents empty spaces 
                                and 1 represents walls.
    
    Returns:
        int: Length of the shortest path, or -1 if no path exists.
    
    Raises:
        ValueError: If maze is empty, None, or has irregular row lengths
    """
    # Validate input
    if not maze or not maze[0]:
        raise ValueError("Maze cannot be empty")
    
    # Check for irregular row lengths
    row_lengths = set(len(row) for row in maze)
    if len(row_lengths) > 1:
        raise ValueError("Maze must have consistent row lengths")
    
    rows, cols = len(maze), len(maze[0])
    
    # Check if start or end is blocked
    if maze[0][0] == 1 or maze[rows-1][cols-1] == 1:
        return -1
    
    # All 8 possible moves (including diagonals)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    
    # Track visited cells and path length
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(0, 0, 1)])  # (row, col, path_length)
    visited[0][0] = True
    
    while queue:
        curr_row, curr_col, path_length = queue.popleft()
        
        # Reached bottom-right corner
        if curr_row == rows - 1 and curr_col == cols - 1:
            return path_length
        
        # Explore 8 possible directions
        for dx, dy in directions:
            new_row, new_col = curr_row + dx, curr_col + dy
            
            # Check if new position is valid
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                maze[new_row][new_col] == 0 and 
                not visited[new_row][new_col]):
                
                queue.append((new_row, new_col, path_length + 1))
                visited[new_row][new_col] = True
    
    # No path found
    return -1