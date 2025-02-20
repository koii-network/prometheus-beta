def cleanRoom(grid, r, c, direction):
    """
    Calculate the minimum number of steps required to clean an entire grid-based room.
    
    Args:
    - grid (list[list[int]]): 2D grid representing the room layout
    - r (int): Starting row position of the robot
    - c (int): Starting column position of the robot
    - direction (int): Initial direction of the robot (0: Up, 1: Right, 2: Down, 3: Left)
    
    Returns:
    - int: Minimum number of steps to clean the entire room
    """
    # Directions: Up, Right, Down, Left
    DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    def is_valid_move(grid, x, y):
        """Check if the move is within grid bounds and cell is not blocked."""
        return (0 <= x < len(grid[0]) and 
                0 <= y < len(grid) and 
                grid[y][x] != 1)  # Assuming 1 represents a blocked cell
    
    def dfs(x, y, curr_dir, visited, steps):
        """
        Depth-first search to clean the room with minimum steps.
        
        Args:
        - x (int): Current x coordinate
        - y (int): Current y coordinate
        - curr_dir (int): Current direction
        - visited (set): Set of visited cells
        - steps (int): Number of steps taken
        
        Returns:
        - int: Minimum steps to clean the remaining room
        """
        # Mark current cell as visited
        visited.add((x, y))
        
        min_steps = float('inf')
        
        # Try all 4 directions
        for i in range(4):
            # Calculate new direction and position
            new_dir = (curr_dir + i) % 4
            dx, dy = DIRECTIONS[new_dir]
            new_x, new_y = x + dx, y + dy
            
            # Check if the new position is valid and not visited
            if (new_x, new_y) not in visited and is_valid_move(grid, new_x, new_y):
                # Recursive call to clean the room from this position
                curr_steps = dfs(new_x, new_y, new_dir, visited.copy(), steps + 1)
                min_steps = min(min_steps, curr_steps)
        
        # If all cells are visited, return current steps
        return steps if len(visited) == sum(row.count(0) for row in grid) else min_steps
    
    # Start cleaning from initial position with initial direction
    result = dfs(c, r, direction, set(), 0)
    
    # Return -1 if not all cells could be cleaned
    return result if result != float('inf') else -1