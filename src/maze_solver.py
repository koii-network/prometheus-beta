from typing import List, Tuple, Optional
from collections import deque

def find_shortest_path(maze: List[List[int]]) -> Optional[List[Tuple[int, int]]]:
    """
    Find the shortest path from start (2) to end (3) in a maze.
    
    Args:
        maze (List[List[int]]): 2D grid representing the maze
            0: empty cell
            1: wall
            2: start cell
            3: end cell
    
    Returns:
        Optional[List[Tuple[int, int]]]: Shortest path from start to end, 
        or None if no path exists
    
    Raises:
        ValueError: If maze is invalid or missing start/end points
    """
    # Validate maze input
    if not maze or not maze[0]:
        raise ValueError("Maze cannot be empty")
    
    # Find start and end positions
    start = None
    end = None
    start_count = 0
    end_count = 0
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 2:
                start = (r, c)
                start_count += 1
            elif maze[r][c] == 3:
                end = (r, c)
                end_count += 1
    
    # Validate start and end exist
    if start_count != 1 or end_count != 1:
        raise ValueError("Maze must have exactly one start (2) and one end (3) point")
    
    # If start and end are the same, return the start
    if start == end:
        return [start]
    
    # BFS to find shortest path
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()
        
        # Check if reached end
        if current == end:
            return path
        
        # Explore neighbors
        neighbors = get_neighbors(current)
        for neighbor in neighbors:
            # Check if neighbor is valid and not visited
            if is_valid(maze, neighbor) and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    # No path found
    return None

def get_neighbors(cell: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Get potential neighboring cells (up, down, left, right).
    
    Args:
        cell (Tuple[int, int]): Current cell coordinates
    
    Returns:
        List[Tuple[int, int]]: List of neighboring cell coordinates
    """
    r, c = cell
    return [
        (r-1, c),  # up
        (r+1, c),  # down
        (r, c-1),  # left
        (r, c+1)   # right
    ]

def is_valid(maze: List[List[int]], cell: Tuple[int, int]) -> bool:
    """
    Check if a cell is valid (within bounds and not a wall).
    
    Args:
        maze (List[List[int]]): 2D grid representing the maze
        cell (Tuple[int, int]): Cell coordinates to check
    
    Returns:
        bool: True if cell is valid, False otherwise
    """
    r, c = cell
    return (
        0 <= r < len(maze) and 
        0 <= c < len(maze[0]) and 
        (maze[r][c] == 0 or maze[r][c] == 3)  # empty or end cell
    )