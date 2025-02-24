from typing import List, Optional, Tuple

def is_prime(n: int) -> bool:
    """
    Check if a given number is prime.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_number_path(grid: List[List[int]]) -> Optional[List[Tuple[int, int]]]:
    """
    Find a continuous path of cells that form a prime number sequence.
    
    Args:
        grid (List[List[int]]): A 2D grid of integers.
    
    Returns:
        Optional[List[Tuple[int, int]]]: A list of cell coordinates forming a prime path,
        or None if no such path exists.
    """
    if not grid or not grid[0]:
        return None

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def dfs(x: int, y: int, current_path: List[Tuple[int, int]], current_sequence: List[int]) -> Optional[List[Tuple[int, int]]]:
        """
        Depth-first search to find a prime path.
        
        Args:
            x (int): Current row index.
            y (int): Current column index.
            current_path (List[Tuple[int, int]]): Current path of coordinates.
            current_sequence (List[int]): Current sequence of numbers.
        
        Returns:
            Optional[List[Tuple[int, int]]]: Prime path, or None if not found.
        """
        # Check if current number can continue the sequence
        if current_sequence and not is_prime(int(''.join(map(str, current_sequence)))):
            return None

        # Mark current cell as visited
        visited[x][y] = True
        current_path.append((x, y))
        current_sequence.append(grid[x][y])

        # Check if current path forms a prime number
        if is_prime(int(''.join(map(str, current_sequence)))):
            return current_path

        # Try all 4 directions: up, down, left, right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Check boundary and visited conditions
            if (0 <= new_x < rows and 
                0 <= new_y < cols and 
                not visited[new_x][new_y]):
                
                result = dfs(new_x, new_y, current_path.copy(), current_sequence.copy())
                if result:
                    return result

        return None

    # Try starting DFS from each cell
    for i in range(rows):
        for j in range(cols):
            result = dfs(i, j, [], [])
            if result:
                return result

    return None