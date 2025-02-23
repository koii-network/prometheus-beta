from typing import List, Tuple
from collections import deque

def find_shortest_path(maze: List[List[int]]) -> int:
    """
    Find the shortest path length in an NxN maze from top-left to bottom-right.
    
    Args:
        maze (List[List[int]]): A 2D grid where 0 represents open paths and 1 represents walls.
    
    Returns:
        int: Length of the shortest path from top-left to bottom-right, 
             or -1 if no path exists.
    
    Raises:
        ValueError: If the maze is empty or not a square grid.
    """
    # Validate input
    if not maze or not maze[0]:
        return -1
    
    n = len(maze)
    
    # Validate maze is a square grid
    if any(len(row) != n for row in maze):
        raise ValueError("Maze must be a square grid")
    
    # Check if start or end is blocked
    if maze[0][0] == 1 or maze[n-1][n-1] == 1:
        return -1
    
    # Possible movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Queue for BFS, storing (row, col, path_length)
    queue = deque([(0, 0, 1)])
    
    # Track visited cells to avoid revisiting
    visited = set([(0, 0)])
    
    while queue:
        row, col, path_length = queue.popleft()
        
        # Reached bottom-right corner
        if row == n - 1 and col == n - 1:
            return path_length
        
        # Explore adjacent cells
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # Check if new position is valid
            if (0 <= new_row < n and 
                0 <= new_col < n and 
                maze[new_row][new_col] == 0 and 
                (new_row, new_col) not in visited):
                
                queue.append((new_row, new_col, path_length + 1))
                visited.add((new_row, new_col))
    
    # No path found
    return -1