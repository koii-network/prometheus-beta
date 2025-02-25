def is_magic_square(numbers):
    """
    Determine if a list of 10 integers represents a valid 3x3 magic square.
    
    A 3x3 magic square has the following properties:
    - Exactly 10 unique integers (1-9)
    - Numbers can be arranged into a 3x3 grid
    - All rows, columns, and diagonals sum to the same magic constant

    Args:
        numbers (list): A list of 10 integers to check

    Returns:
        bool: True if the input represents a valid 3x3 magic square, False otherwise
    """
    # Check input length and uniqueness
    if len(numbers) != 10 or len(set(numbers)) != 10:
        return False
    
    # Check if numbers are in range 1-9
    if any(num < 1 or num > 9 for num in numbers):
        return False
    
    # Try all possible 3x3 grid arrangements
    from itertools import permutations
    
    for perm in permutations(numbers, 9):
        # Convert permutation to 3x3 grid
        grid = [
            perm[0:3],
            perm[3:6],
            perm[6:9]
        ]
        
        # Calculate row sums
        row_sums = [sum(row) for row in grid]
        
        # Calculate column sums
        col_sums = [
            grid[0][0] + grid[1][0] + grid[2][0],
            grid[0][1] + grid[1][1] + grid[2][1],
            grid[0][2] + grid[1][2] + grid[2][2]
        ]
        
        # Calculate diagonal sums
        diag_sums = [
            grid[0][0] + grid[1][1] + grid[2][2],
            grid[0][2] + grid[1][1] + grid[2][0]
        ]
        
        # Combine all sums to check
        all_sums = row_sums + col_sums + diag_sums
        
        # Check if all sums are equal
        if len(set(all_sums)) == 1:
            return True
    
    return False