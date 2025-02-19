from collections import deque

def solve_maze(maze):
    """
    Find the shortest path from start (2) to end (3) in a maze grid.
    
    Args:
        maze (List[List[int]]): 2D grid representing the maze
            0: empty cell
            1: wall
            2: start cell
            3: end cell
    
    Returns:
        List[tuple]: Shortest path from start to end, or empty list if no path exists
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
    
    if not start or not end:
        return []
    
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
            if is_valid(neighbor, maze) and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    # No path found
    return []

def get_neighbors(cell):
    """
    Return neighboring cells (up, right, down, left).
    
    Args:
        cell (tuple): Current cell coordinates (row, col)
    
    Returns:
        List[tuple]: List of neighboring cell coordinates
    """
    r, c = cell
    return [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]

def is_valid(cell, maze):
    """
    Check if cell is within maze boundaries and is an empty cell.
    
    Args:
        cell (tuple): Cell coordinates (row, col)
        maze (List[List[int]]): 2D grid representing the maze
    
    Returns:
        bool: True if cell is valid, False otherwise
    """
    r, c = cell
    # Check boundaries and cell type
    return (0 <= r < len(maze) and 
            0 <= c < len(maze[0]) and 
            maze[r][c] in [0, 3])  # Can move through empty cells and end cell