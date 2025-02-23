from typing import List, Tuple, Optional
from collections import deque

def find_shortest_path(maze: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """
    Find the shortest path through a maze from start to end.
    
    Args:
        maze (List[List[str]]): 2D grid representing the maze
            '#' represents walls
            '.' represents open paths
        start (Tuple[int, int]): Starting coordinates (row, col)
        end (Tuple[int, int]): Ending coordinates (row, col)
    
    Returns:
        Optional[List[Tuple[int, int]]]: Shortest path as a list of coordinates, 
        or None if no path exists
    """
    if not maze or not maze[0]:
        return None
    
    rows, cols = len(maze), len(maze[0])
    
    # Validate start and end points
    if (not (0 <= start[0] < rows and 0 <= start[1] < cols) or 
        not (0 <= end[0] < rows and 0 <= end[1] < cols)):
        return None
    
    if maze[start[0]][start[1]] == '#' or maze[end[0]][end[1]] == '#':
        return None
    
    # Possible movement directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Track visited cells and path
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
        
        # Explore neighbors
        for dx, dy in directions:
            next_x, next_y = current[0] + dx, current[1] + dy
            
            # Check if next cell is valid
            if (0 <= next_x < rows and 0 <= next_y < cols and 
                maze[next_x][next_y] != '#' and 
                (next_x, next_y) not in visited):
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
                parent[(next_x, next_y)] = current
    
    # No path found
    return None