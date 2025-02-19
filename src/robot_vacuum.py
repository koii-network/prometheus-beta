from typing import List, Tuple

def cleanRoom(grid: List[List[int]], r: int, c: int, direction: str) -> int:
    """
    Calculate the minimum steps to clean an entire grid-based room.
    
    Args:
    - grid: 2D grid representing the room layout (0: empty, 1: obstacle)
    - r: Starting row position of the robot
    - c: Starting column position of the robot
    - direction: Initial direction of the robot ('N', 'S', 'E', 'W')
    
    Returns:
    - Minimum number of steps required to clean the entire room
    """
    # Validate input
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    
    # Directions: North, East, South, West
    directions = {
        'N': (-1, 0),
        'E': (0, 1),
        'S': (1, 0),
        'W': (0, -1)
    }
    
    # Validate starting position
    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
        raise ValueError("Invalid starting position")
    
    # Track visited cells and steps
    visited = set()
    steps = 0
    
    def is_valid_move(x: int, y: int) -> bool:
        return (0 <= x < rows and 
                0 <= y < cols and 
                grid[x][y] == 0 and 
                (x, y) not in visited)
    
    def backtrack(x: int, y: int, current_dir: str) -> None:
        nonlocal steps
        
        # Mark current cell as visited
        visited.add((x, y))
        
        # Try moving in all 4 directions
        for dir_key, (dx, dy) in directions.items():
            new_x, new_y = x + dx, y + dy
            
            # If the new position is valid and not visited
            if is_valid_move(new_x, new_y):
                steps += 1
                backtrack(new_x, new_y, dir_key)
    
    # Start the cleaning process from initial position
    backtrack(r, c, direction)
    
    return steps