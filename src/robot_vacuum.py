from typing import List

def cleanRoom(grid: List[List[int]], r: int, c: int, direction: int) -> int:
    """
    Calculate the minimum number of steps required to clean the entire room.
    
    Args:
    - grid: 2D grid representing the room layout (0 = clean, 1 = obstacle)
    - r: Starting row position of the robot
    - c: Starting column position of the robot
    - direction: Initial direction of the robot (0: North, 1: East, 2: South, 3: West)
    
    Returns:
    - Minimum number of steps to clean the entire room
    """
    # Directions: North, East, South, West
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    def is_valid_move(grid, row, col):
        """Check if the move is within grid and not an obstacle"""
        return (0 <= row < len(grid) and 
                0 <= col < len(grid[0]) and 
                grid[row][col] == 0)
    
    def dfs(grid, row, col, curr_dir, visited, path):
        """Depth-first search to explore and clean the room"""
        if (row, col) in visited:
            return path[visited.index((row, col))]
        
        visited.append((row, col))
        path.append(len(visited) - 1)
        
        min_steps = float('inf')
        
        # Try all 4 directions
        for i in range(4):
            new_dir = (curr_dir + i) % 4
            new_row = row + dirs[new_dir][0]
            new_col = col + dirs[new_dir][1]
            
            # If move is valid, explore
            if is_valid_move(grid, new_row, new_col):
                steps = dfs(grid, new_row, new_col, new_dir, visited.copy(), path.copy())
                min_steps = min(min_steps, steps + 1)
        
        return min_steps
    
    # All cells are obstacles
    if not grid or not grid[0] or all(all(cell == 1 for cell in row) for row in grid):
        return 0
    
    # Room is fully clean or starting position is an obstacle
    if grid[r][c] == 1:
        return 0
    
    # Perform depth-first search to find minimum steps
    return dfs(grid, r, c, direction, [], [])