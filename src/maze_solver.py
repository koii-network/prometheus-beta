from typing import List, Tuple, Optional

def find_shortest_path(maze: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """
    Find the shortest path through a maze from start to end.
    
    Args:
    - maze: 2D list representing the maze ('.' for path, '#' for wall)
    - start: Starting coordinates (row, col)
    - end: Ending coordinates (row, col)
    
    Returns:
    - List of coordinates representing the shortest path, or None if no path exists
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
    
    # Possible movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Queue for BFS
    queue = [(start, [start])]
    
    # Track visited cells to prevent revisiting
    visited = set([start])
    
    while queue:
        (current_row, current_col), path = queue.pop(0)
        
        # Check if reached the end
        if (current_row, current_col) == end:
            return path
        
        # Try all four directions
        for d_row, d_col in directions:
            next_row, next_col = current_row + d_row, current_col + d_col
            
            # Check if next cell is valid
            if (0 <= next_row < rows and 
                0 <= next_col < cols and 
                maze[next_row][next_col] != '#' and 
                (next_row, next_col) not in visited):
                
                new_path = path + [(next_row, next_col)]
                queue.append(((next_row, next_col), new_path))
                visited.add((next_row, next_col))
    
    # No path found
    return None