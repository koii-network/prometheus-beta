from collections import deque

def find_shortest_path(maze):
    """
    Find the shortest path from start to end in a maze.
    
    :param maze: 2D grid representing the maze
    :return: List of cells representing the shortest path, or None if no path exists
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
    
    # Queue for BFS
    queue = deque([(start, [start])])
    
    # Set to track visited cells
    visited = set([start])
    
    # BFS traversal
    while queue:
        current, path = queue.popleft()
        
        # Check if reached end
        if current == end:
            return path
        
        # Explore neighbors
        neighbors = get_neighbors(current)
        for neighbor in neighbors:
            # Check if neighbor is valid and not visited
            if neighbor not in visited and is_valid(neighbor, maze):
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    # No path found
    return None

def get_neighbors(cell):
    """
    Get neighboring cells for a given cell.
    
    :param cell: Current cell coordinates (row, col)
    :return: List of neighboring cell coordinates
    """
    r, c = cell
    # Four directional neighbors: up, right, down, left
    return [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]

def is_valid(cell, maze):
    """
    Check if a cell is valid in the maze.
    
    :param cell: Cell coordinates (row, col)
    :param maze: 2D grid representing the maze
    :return: Boolean indicating if cell is valid
    """
    r, c = cell
    
    # Check if cell is within maze boundaries
    if r < 0 or r >= len(maze) or c < 0 or c >= len(maze[0]):
        return False
    
    # Check if cell is not a wall
    return maze[r][c] != 1