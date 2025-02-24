def is_magic_square(numbers):
    """
    Determine if a list of 10 integers represents a valid 3x3 magic square.
    
    A magic square is a 3x3 grid where:
    - All numbers are unique integers from 1-9
    - The sum of each row, column, and diagonal is the same (magic constant)
    
    Args:
        numbers (list): A list of 10 integers
    
    Returns:
        bool: True if the input represents a valid 3x3 magic square, False otherwise
    
    Raises:
        ValueError: If the input is not a list of 10 unique integers from 1-9
    """
    # Validate input
    if not isinstance(numbers, list):
        return False
    
    # Check if the list contains exactly 10 elements
    if len(numbers) != 10:
        return False
    
    # Check for unique integers from 1-9
    if len(set(numbers)) != 9 or any(num < 1 or num > 9 for num in numbers):
        return False
    
    # Convert the first 9 numbers into a 3x3 grid
    grid = [
        [numbers[0], numbers[1], numbers[2]],
        [numbers[3], numbers[4], numbers[5]],
        [numbers[6], numbers[7], numbers[8]]
    ]
    
    # Calculate magic constant (should be 15 for a 3x3 magic square)
    magic_constant = 15
    
    # Check rows
    for row in grid:
        if sum(row) != magic_constant:
            return False
    
    # Check columns
    for col in range(3):
        if sum(grid[row][col] for row in range(3)) != magic_constant:
            return False
    
    # Check diagonals
    if (grid[0][0] + grid[1][1] + grid[2][2]) != magic_constant:
        return False
    
    if (grid[0][2] + grid[1][1] + grid[2][0]) != magic_constant:
        return False
    
    return True