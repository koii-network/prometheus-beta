from typing import List, Tuple

def cleanRoom(grid: List[List[int]], r: int, c: int, direction: int) -> int:
    """
    Clean a room using a robot vacuum cleaner algorithm.
    
    Args:
    - grid: 2D grid representing the room (0 = empty cell, 1 = obstacle)
    - r: Starting row of the robot
    - c: Starting column of the robot
    - direction: Initial direction of the robot (0: North, 1: East, 2: South, 3: West)
    
    Returns:
    - Minimum number of steps required to clean the entire room
    """
    # Directions: North (0), East (1), South (2), West (3)
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    # Get room dimensions
    rows, cols = len(grid), len(grid[0])
    
    # Track visited cells and cleaned cells
    visited = set()
    cleaned = set()
    
    def is_valid_move(x: int, y: int) -> bool:
        """Check if the move is valid (within grid and not an obstacle)"""
        return 0 <= x < cols and 0 <= y < rows and grid[y][x] == 0
    
    def dfs(x: int, y: int, curr_dir: int) -> int:
        """Depth-first search to clean the room"""
        # Mark current cell as visited and cleaned
        visited.add((x, y))
        cleaned.add((x, y))
        
        steps = 0
        
        # Try all 4 directions
        for i in range(4):
            # Calculate new direction and position
            new_dir = (curr_dir + i) % 4
            dx, dy = directions[new_dir]
            new_x, new_y = x + dx, y + dy
            
            # If move is valid and not visited
            if is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
                steps += 1  # Move step
                steps += dfs(new_x, new_y, new_dir)
        
        return steps
    
    # Start cleaning from initial position
    total_steps = dfs(c, r, direction)
    
    # Add 1 to include the starting step
    return total_steps + 1