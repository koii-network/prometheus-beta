from typing import List, Tuple

def cleanRoom(grid: List[List[int]], r: int, c: int, direction: int) -> int:
    """
    Clean a room represented by a grid using a robot vacuum cleaner.
    
    Args:
    - grid: 2D grid representing the room (0 = clean, 1 = dirty)
    - r: Starting row of the robot
    - c: Starting column of the robot
    - direction: Initial direction of the robot (0: North, 1: East, 2: South, 3: West)
    
    Returns:
    - Minimum number of steps required to clean the entire room
    """
    # Validate inputs
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    
    # Validate starting position
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return 0
    
    # Directions: North, East, South, West
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Track cleaned cells and visited cells
    cleaned = set()
    visited = set()
    
    def is_valid_move(x: int, y: int) -> bool:
        """Check if the move is within grid and not a wall"""
        return (0 <= x < rows and 
                0 <= y < cols and 
                grid[x][y] == 0)
    
    def backtrack(x: int, y: int, curr_dir: int) -> int:
        """
        Recursive backtracking to clean the room
        
        Args:
        - x: Current row
        - y: Current column
        - curr_dir: Current direction
        
        Returns:
        - Minimum steps to clean the room from this point
        """
        # Mark current cell as cleaned and visited
        cleaned.add((x, y))
        visited.add((x, y))
        
        steps = 0
        
        # Try moving in all 4 directions
        for i in range(4):
            # Calculate new direction and new position
            new_dir = (curr_dir + i) % 4
            dx, dy = directions[new_dir]
            new_x, new_y = x + dx, y + dy
            
            # If not already cleaned and move is valid
            if (new_x, new_y) not in cleaned and is_valid_move(new_x, new_y):
                steps += 1  # Move step
                steps += backtrack(new_x, new_y, new_dir)
                
                # Backtrack: move back to original position
                steps += 2  # Two steps to go back to original position
        
        return steps
    
    # Ensure entire grid is cleaned
    total_dirty_cells = sum(row.count(0) for row in grid)
    
    # Start cleaning
    min_steps = backtrack(r, c, direction)
    
    # Check if all cells were cleaned
    if len(cleaned) != total_dirty_cells:
        return -1  # Impossible to clean entire room
    
    return min_steps
