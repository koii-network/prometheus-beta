from typing import List, Tuple

def cleanRoom(grid: List[List[int]], r: int, c: int, direction: int) -> int:
    """
    Clean a room using a robot vacuum cleaner algorithm.
    
    Args:
    - grid: 2D grid representing the room (0 = clean, 1 = obstacle)
    - r: starting row of the robot
    - c: starting column of the robot
    - direction: initial direction of the robot (0: North, 1: East, 2: South, 3: West)
    
    Returns:
    - Minimum number of steps required to clean the entire room
    """
    # Validate inputs
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    
    # Validate starting position
    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
        return 0
    
    # Directions: North, East, South, West
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Track cleaned cells and visited states
    cleaned = set()
    visited = set()
    
    def is_valid_move(x: int, y: int) -> bool:
        """Check if the move is valid (within grid and not an obstacle)"""
        return (0 <= x < rows and 0 <= y < cols and grid[x][y] == 0)
    
    def dfs(x: int, y: int, curr_dir: int) -> int:
        """Depth-first search to clean the room"""
        # Create a unique state to avoid revisiting
        state = (x, y, curr_dir)
        if state in visited:
            return 0
        
        visited.add(state)
        cleaned.add((x, y))
        
        steps = 1
        
        # Try moving in 4 directions
        for i in range(4):
            # Rotate and calculate new direction
            new_dir = (curr_dir + i) % 4
            dx, dy = directions[new_dir]
            
            new_x, new_y = x + dx, y + dy
            
            # If move is valid and cell is not cleaned
            if is_valid_move(new_x, new_y) and (new_x, new_y) not in cleaned:
                steps += dfs(new_x, new_y, new_dir)
        
        return steps
    
    # Start cleaning from initial position and direction
    total_steps = dfs(r, c, direction)
    
    # Return total steps or number of cleaned cells if impossible
    return min(total_steps, rows * cols)