from collections import deque

def find_shortest_path(maze):
    """
    Find the shortest path from start (2) to end (3) in a 2D maze grid.
    
    Args:
    maze (List[List[int]]): 2D grid representing the maze 
    - 0: empty cell
    - 1: wall
    - 2: start cell
    - 3: end cell
    
    Returns:
    List[tuple]: Shortest path from start to end, or None if no path exists
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
    
    # If start or end not found, return None
    if not start or not end:
        return None
    
    # Queue for BFS
    queue = deque([(start, [start])])
    
    # Track visited cells to avoid cycles
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()
        
        # Check if reached end
        if current == end:
            return path
        
        # Check neighboring cells
        neighbors = get_neighbors(current)
        for neighbor in neighbors:
            # Ensure neighbor is valid and not visited
            if is_valid(maze, neighbor) and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    # No path found
    return None

def get_neighbors(cell):
    """
    Returns neighboring cells (up, right, down, left).
    
    Args:
    cell (tuple): Current cell coordinates (row, col)
    
    Returns:
    List[tuple]: List of neighboring cell coordinates
    """
    r, c = cell
    return [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]

def is_valid(maze, cell):
    """
    Check if cell is within maze boundaries and is an empty cell.
    
    Args:
    maze (List[List[int]]): 2D maze grid
    cell (tuple): Cell coordinates to check
    
    Returns:
    bool: True if cell is valid, False otherwise
    """
    r, c = cell
    return (0 <= r < len(maze) and 
            0 <= c < len(maze[0]) and 
            maze[r][c] != 1)  # Not a wall