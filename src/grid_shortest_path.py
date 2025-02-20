from typing import List, Optional

def find_shortest_constrained_path(grid: List[List[int]]) -> Optional[int]:
    """
    Find the shortest path from top-left to bottom-right with constrained movement.
    
    Movement rules:
    - Can move right or down
    - Can only move to an empty cell (0)
    - If right is blocked, must move down
    
    Args:
        grid (List[List[int]]): N x N grid with 0s (empty) and 1s (blocked)
    
    Returns:
        Optional[int]: Length of the shortest path, or None if no path exists
    """
    if not grid or not grid[0]:
        return None
    
    N = len(grid)
    
    # Dynamic programming to track shortest path
    dp = [[float('inf')] * N for _ in range(N)]
    dp[0][0] = 1 if grid[0][0] == 0 else float('inf')
    
    # Fill first row
    for j in range(1, N):
        if grid[0][j] == 0:
            # Check if we can move right from previous cell
            if dp[0][j-1] != float('inf'):
                dp[0][j] = dp[0][j-1] + 1
    
    # Fill first column
    for i in range(1, N):
        if grid[i][0] == 0:
            # Must move down if right is blocked
            if dp[i-1][0] != float('inf'):
                dp[i][0] = dp[i-1][0] + 1
    
    # Fill the rest of the grid
    for i in range(1, N):
        for j in range(1, N):
            if grid[i][j] == 0:
                # Try moving right from left
                if dp[i][j-1] != float('inf'):
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
                
                # Try moving down from top
                if dp[i-1][j] != float('inf'):
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
    
    # Return path length to bottom-right, or None if unreachable
    return dp[N-1][N-1] if dp[N-1][N-1] != float('inf') else None