def is_magic_square(numbers):
    """
    Determine if a list of 10 integers represents a valid 3x3 magic square.
    
    A 3x3 magic square has the following properties:
    - Exactly 10 unique integers 
    - 9 numbers between 1-9
    - 10th number representing the total sum of each line
    - Numbers can be arranged into a 3x3 grid
    - All rows, columns, and diagonals sum to the 10th number

    Args:
        numbers (list): A list of 10 integers to check

    Returns:
        bool: True if the input represents a valid 3x3 magic square, False otherwise
    """
    # Check input length
    if len(numbers) != 10:
        return False
    
    # Check if numbers are unique
    if len(set(numbers)) != 10:
        return False
    
    # Separate base numbers (1-9) and the magic constant
    base_numbers = [n for n in numbers if 1 <= n <= 9]
    magic_constants = [n for n in numbers if n not in base_numbers]
    
    # Ensure we have 9 base numbers and 1 magic constant
    if len(base_numbers) != 9 or len(magic_constants) != 1:
        return False
    
    magic_constant = magic_constants[0]
    
    # Try all possible 3x3 grid arrangements
    from itertools import permutations
    
    for perm in permutations(base_numbers, 9):
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
        
        # Check if all sums are equal to the magic constant
        if len(set(all_sums)) == 1 and all_sums[0] == magic_constant:
            return True
    
    return False