from typing import List, Tuple

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_sequence_path(grid: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Find a continuous path of cells that form a prime number sequence.
    
    Args:
        grid (List[List[int]]): A 2D grid of integers
    
    Returns:
        List[Tuple[int, int]]: A list of (row, col) coordinates forming a prime sequence path,
                                or an empty list if no such path exists
    """
    if not grid or not grid[0]:
        return []
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def dfs(row: int, col: int, current_sequence: List[int], path: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        # Out of bounds or already visited
        if (row < 0 or row >= rows or 
            col < 0 or col >= cols or 
            visited[row][col]):
            return []
        
        # Current number check
        current_num = grid[row][col]
        
        # Cannot continue if current number doesn't follow prime sequence rule
        if current_sequence and not is_prime(int(''.join(map(str, current_sequence + [current_num])))):
            return []
        
        # Mark as visited
        visited[row][col] = True
        current_path = path + [(row, col)]
        current_sequence.append(current_num)
        
        # If sequence is long enough (more than 1 number), it's a valid result
        max_path = current_path if len(current_sequence) > 1 else []
        
        # Explore 4 directions: up, down, left, right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # Recursively explore
            subpath = dfs(new_row, new_col, current_sequence.copy(), current_path)
            
            # Update max path if longer path is found
            if len(subpath) > len(max_path):
                max_path = subpath
        
        # Backtrack
        visited[row][col] = False
        return max_path
    
    # Try starting from each cell
    best_path = []
    for r in range(rows):
        for c in range(cols):
            path = dfs(r, c, [], [])
            if len(path) > len(best_path):
                best_path = path
    
    return best_path