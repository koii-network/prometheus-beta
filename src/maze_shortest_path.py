from collections import deque

def find_shortest_path(maze):
    """
    Find the shortest path from the start cell (2) to the end cell (3) in a maze.
    
    :param maze: 2D grid representing the maze
                 0: empty cell
                 1: wall
                 2: start cell
                 3: end cell
    :return: List of cells representing the shortest path, or None if no path exists
    """
    # Find start and end cells
    start = None
    end = None
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if maze[r][c] == 2:
                start = (r, c)
            elif maze[r][c] == 3:
                end = (r, c)
    
    # If start or end is not found, return None
    if not start or not end:
        return None
    
    # Use BFS to find shortest path
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()
        
        # Check if reached the end
        if current == end:
            return path
        
        # Explore neighbors
        neighbors = get_neighbors(current)
        for neighbor in neighbors:
            # Check if neighbor is valid and not visited
            if is_valid(neighbor, maze) and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    # No path found
    return None

def get_neighbors(cell):
    """
    Get neighboring cells (up, right, down, left)
    
    :param cell: Current cell (row, col)
    :return: List of neighboring cells
    """
    r, c = cell
    return [
        (r-1, c),  # Up
        (r, c+1),  # Right
        (r+1, c),  # Down
        (r, c-1)   # Left
    ]

def is_valid(cell, maze):
    """
    Check if a cell is valid (within maze boundaries and not a wall)
    
    :param cell: Cell to check (row, col)
    :param maze: 2D grid representing the maze
    :return: True if cell is valid, False otherwise
    """
    r, c = cell
    # Check boundaries
    if r < 0 or r >= len(maze) or c < 0 or c >= len(maze[0]):
        return False
    
    # Check if cell is empty (0) or end (3)
    return maze[r][c] == 0 or maze[r][c] == 3