from typing import List, Tuple

def cleanRoom(grid: List[List[int]], r: int, c: int, direction: int) -> int:
    """
    Clean a grid-based room and return the minimum number of steps required.
    
    Args:
    - grid: 2D grid representing the room layout (0 = empty, 1 = obstacle)
    - r: Starting row position
    - c: Starting column position
    - direction: Initial direction of the robot (0: up, 1: right, 2: down, 3: left)
    
    Returns:
    - Minimum number of steps to clean the entire room
    
    Raises:
    - ValueError: If inputs are invalid
    """
    # Input validation
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        raise ValueError("Starting position out of grid bounds")
    
    if direction < 0 or direction > 3:
        raise ValueError("Invalid direction. Must be 0, 1, 2, or 3")
    
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Track visited cells and total steps
    visited = set()
    steps = 0
    
    def is_valid_move(x: int, y: int) -> bool:
        """Check if move is within grid and not an obstacle"""
        return (0 <= x < len(grid) and 
                0 <= y < len(grid[0]) and 
                grid[x][y] == 0)
    
    def dfs(x: int, y: int, curr_dir: int) -> None:
        """Depth-first search to clean the room"""
        nonlocal steps
        
        # Mark current cell as visited
        visited.add((x, y))
        
        # Try all 4 directions
        for i in range(4):
            # Calculate new direction and position
            new_dir = (curr_dir + i) % 4
            dx, dy = directions[new_dir]
            new_x, new_y = x + dx, y + dy
            
            # If new position is valid and not visited
            if is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
                steps += 1
                dfs(new_x, new_y, new_dir)
    
    # Start cleaning from initial position
    dfs(r, c, direction)
    
    return steps