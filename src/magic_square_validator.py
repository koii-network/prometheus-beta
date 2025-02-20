def is_magic_square(nums):
    """
    Determine if a list of 10 integers represents a valid 3x3 magic square.
    
    A magic square must meet these criteria:
    1. Exactly 10 integers are provided
    2. Contains numbers 1-9 with no repeats
    3. When arranged in a 3x3 grid, row, column, and diagonal sums are equal
    
    Args:
        nums (list): A list of 10 integers
    
    Returns:
        bool: True if the list represents a valid 3x3 magic square, False otherwise
    """
    # Check if input is correct length
    if len(nums) != 10:
        return False
    
    # Check if nums contain 1-9 with no repeats
    unique_nums = set(nums)
    if len(unique_nums) != 9 or not all(1 <= num <= 9 for num in unique_nums):
        return False
    
    # Try all 10 nums and check if removing one creates a magic square
    for skip_index in range(10):
        # Create a 3x3 grid by removing one number
        grid = [num for i, num in enumerate(nums) if i != skip_index]
        
        # Check if rows, columns, and diagonals sum to same value
        row1_sum = sum(grid[0:3])
        row2_sum = sum(grid[3:6])
        row3_sum = sum(grid[6:9])
        
        col1_sum = grid[0] + grid[3] + grid[6]
        col2_sum = grid[1] + grid[4] + grid[7]
        col3_sum = grid[2] + grid[5] + grid[8]
        
        diag1_sum = grid[0] + grid[4] + grid[8]
        diag2_sum = grid[2] + grid[4] + grid[6]
        
        sums = [row1_sum, row2_sum, row3_sum, 
                col1_sum, col2_sum, col3_sum, 
                diag1_sum, diag2_sum]
        
        # Check if all sums are equal and the sum is the same
        if len(set(sums)) == 1:
            return True
    
    return False