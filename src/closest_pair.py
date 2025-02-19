def find_closest_pair(numbers):
    """
    Find the closest pair of numbers in the given array.
    
    Args:
        numbers (list): A list of numbers to find the closest pair from.
    
    Returns:
        tuple: A tuple containing the two closest numbers.
        
    Raises:
        ValueError: If the input list has fewer than 2 numbers.
    """
    # Check if the list has at least 2 numbers
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least 2 numbers")
    
    # Sort the list to help find the closest pair efficiently
    sorted_nums = sorted(numbers)
    
    # Initialize variables to track the closest pair
    min_diff = float('inf')
    closest_pair = None
    
    # Compare adjacent numbers in the sorted list
    for i in range(len(sorted_nums) - 1):
        current_diff = abs(sorted_nums[i] - sorted_nums[i+1])
        
        # Update closest pair if:
        # 1. Current difference is smaller than previous min_diff, or
        # 2. Current difference is equal to min_diff but numbers are smaller
        if (current_diff < min_diff or 
            (current_diff == min_diff and 
             (sorted_nums[i] < closest_pair[0] or 
              (sorted_nums[i] == closest_pair[0] and sorted_nums[i+1] < closest_pair[1])))):
            min_diff = current_diff
            closest_pair = (sorted_nums[i], sorted_nums[i+1])
    
    return closest_pair