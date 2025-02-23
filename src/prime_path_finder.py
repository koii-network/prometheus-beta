def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_path(grid):
    """
    Find a continuous path of prime numbers in the grid.
    
    Args:
        grid (List[List[int]]): 2D grid of numbers
    
    Returns:
        List[tuple]: A list of (row, col) coordinates forming a prime number path, 
                     or an empty list if no prime path is found
    """
    if not grid or not grid[0]:
        return []
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def dfs(row, col, current_path, last_prime=None):
        # Out of bounds or already visited
        if (row < 0 or row >= rows or 
            col < 0 or col >= cols or 
            visited[row][col]):
            return None
        
        current_num = grid[row][col]
        
        # Prime number check
        if not is_prime(current_num):
            return None
        
        # Avoid repeated primes in sequence or break prime path
        if last_prime is not None and not is_prime(last_prime + current_num):
            return None
        
        current_path.append((row, col))
        visited[row][col] = True
        
        # Directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # Try extending the path
            result = dfs(new_row, new_col, current_path, current_num)
            if result:
                return result
        
        # If we get here, this path doesn't work
        current_path.pop()
        visited[row][col] = False
        return None
    
    # Try starting from each cell
    for r in range(rows):
        for c in range(cols):
            path_result = dfs(r, c, [])
            if path_result:
                return path_result
    
    return []