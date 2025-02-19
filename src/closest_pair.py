def find_closest_pair(numbers):
    """
    Find the closest pair of numbers in the given array.
    
    Args:
        numbers (list): A list of numbers
    
    Returns:
        tuple: A tuple containing the two closest numbers 
               If multiple pairs have the same smallest difference, 
               return the pair with the smallest numbers
    
    Raises:
        ValueError: If the input list has fewer than 2 numbers
    """
    # Validate input
    if not numbers or len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers")
    
    # Sort the numbers first
    sorted_nums = sorted(numbers)
    
    # Initialize variables to track the closest pair
    min_diff = float('inf')
    closest_pair = None
    
    # Iterate through sorted numbers to find the smallest difference
    for i in range(len(sorted_nums) - 1):
        current_diff = abs(sorted_nums[i] - sorted_nums[i+1])
        
        # Update closest pair if:
        # 1. Current difference is smaller than min_diff, or
        # 2. Current difference is equal to min_diff but with smaller numbers
        if (current_diff < min_diff or 
            (current_diff == min_diff and 
             (sorted_nums[i] < closest_pair[0] or 
              (sorted_nums[i] == closest_pair[0] and sorted_nums[i+1] < closest_pair[1])))):
            min_diff = current_diff
            closest_pair = (sorted_nums[i], sorted_nums[i+1])
    
    return closest_pair