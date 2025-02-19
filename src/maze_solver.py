from typing import List, Tuple, Optional
from collections import deque

def find_shortest_path(maze: List[List[int]]) -> Optional[List[Tuple[int, int]]]:
    """
    Find the shortest path from start (2) to end (3) in a maze.
    
    Args:
        maze (List[List[int]]): 2D grid where:
            0 = empty cell
            1 = wall
            2 = start cell
            3 = end cell
    
    Returns:
        Optional[List[Tuple[int, int]]]: Shortest path from start to end, 
        or None if no path exists
    """
    # Find start and end cells
    start = None
    end = None
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 2:
                start = (r, c)
            elif maze[r][c] == 3:
                end = (r, c)
    
    # Validate start and end exist
    if not start or not end:
        return None
    
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
    Get 4-directional neighbors of a cell.
    
    Args:
        cell (Tuple[int, int]): Current cell coordinates
    
    Returns:
        List[Tuple[int, int]]: List of neighboring cell coordinates
    """
    r, c = cell
    return [
        (r-1, c),  # Up
        (r+1, c),  # Down
        (r, c-1),  # Left
        (r, c+1)   # Right
    ]

def is_valid(maze: List[List[int]], cell: Tuple[int, int]) -> bool:
    """
    Check if a cell is within maze boundaries and is an empty cell or end cell.
    
    Args:
        maze (List[List[int]]): 2D grid maze
        cell (Tuple[int, int]): Cell coordinates to validate
    
    Returns:
        bool: True if cell is valid, False otherwise
    """
    r, c = cell
    
    # Check boundary conditions
    if r < 0 or r >= len(maze) or c < 0 or c >= len(maze[0]):
        return False
    
    # Check cell is empty or end cell
    return maze[r][c] == 0 or maze[r][c] == 3