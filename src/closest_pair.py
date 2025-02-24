def find_closest_pair(numbers):
    """
    Find the closest pair of numbers in the given array.
    
    Args:
        numbers (list): A list of numbers to search through.
    
    Returns:
        tuple: A tuple containing the two closest numbers.
        
    Raises:
        ValueError: If the input list has fewer than 2 numbers.
    """
    # Check for invalid input
    if not numbers or len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers")
    
    # Sort the input list
    sorted_nums = sorted(numbers)
    
    # Initialize variables to track the closest pair
    min_diff = float('inf')
    closest_pair = None
    
    # Compare adjacent numbers in the sorted list
    for i in range(len(sorted_nums) - 1):
        # Calculate the difference between adjacent numbers
        current_diff = sorted_nums[i+1] - sorted_nums[i]
        
        # Update closest pair if current difference is smaller
        if current_diff < min_diff:
            min_diff = current_diff
            closest_pair = (sorted_nums[i], sorted_nums[i+1])
        
    return closest_pair