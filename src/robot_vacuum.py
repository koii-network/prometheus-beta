from typing import List, Tuple

def cleanRoom(grid: List[List[int]], r: int, c: int, direction: int) -> int:
    """
    Clean a room using a robot vacuum algorithm.
    
    Args:
    - grid (List[List[int]]): 2D grid representing the room 
      (0 = empty cell, 1 = obstacle)
    - r (int): Starting row position of the robot
    - c (int): Starting column position of the robot
    - direction (int): Initial direction of the robot 
      (0: North, 1: East, 2: South, 3: West)
    
    Returns:
    - int: Minimum number of steps required to clean the entire room
    
    Raises:
    - ValueError: If inputs are invalid
    """
    # Input validation
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        raise ValueError("Starting position is out of grid bounds")
    
    if direction < 0 or direction > 3:
        raise ValueError("Invalid direction. Must be 0, 1, 2, or 3")
    
    # Directions: North, East, South, West
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Track visited cells and total clean cells
    visited = set()
    total_cells = sum(row.count(0) for row in grid)
    
    def is_valid_move(x: int, y: int) -> bool:
        """Check if move is valid and cell is not an obstacle."""
        return (0 <= x < len(grid) and 
                0 <= y < len(grid[0]) and 
                grid[x][y] == 0)
    
    def dfs(x: int, y: int, curr_dir: int) -> int:
        """
        Depth-first search to clean the room.
        
        Args:
        - x (int): Current row
        - y (int): Current column
        - curr_dir (int): Current direction
        
        Returns:
        - int: Minimum steps to clean the room from this position
        """
        # Mark current cell as visited
        visited.add((x, y))
        
        # Try all 4 directions
        steps = 0
        for i in range(4):
            # Calculate new direction and position
            new_dir = (curr_dir + i) % 4
            dx, dy = directions[new_dir]
            new_x, new_y = x + dx, y + dy
            
            # If move is valid and cell not visited
            if is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
                steps += 1  # Move
                steps += dfs(new_x, new_y, new_dir)
        
        return steps
    
    # If starting cell is an obstacle, return 0
    if grid[r][c] == 1:
        return 0
    
    # Run DFS from starting position
    total_steps = dfs(r, c, direction)
    
    # Check if all cleanable cells were visited
    if len(visited) != total_cells:
        return -1  # Unable to clean entire room
    
    return total_steps