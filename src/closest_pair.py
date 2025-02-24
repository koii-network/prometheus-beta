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
    
    # Sort the input list to help find the closest pair
    sorted_nums = sorted(numbers)
    
    # Initialize variables to track the closest pair
    min_diff = float('inf')
    closest_pair = None
    
    # Compare all possible pairs to find the smallest absolute difference
    for i in range(len(sorted_nums)):
        for j in range(i+1, len(sorted_nums)):
            current_diff = abs(sorted_nums[j] - sorted_nums[i])
            
            # Update closest pair if:
            # 1. Current difference is smaller, or
            # 2. Differences are equal but current pair has smaller numbers
            if (current_diff < min_diff or 
                (current_diff == min_diff and 
                 (sorted_nums[i] < closest_pair[0] or 
                  (sorted_nums[i] == closest_pair[0] and sorted_nums[j] < closest_pair[1])))):
                min_diff = current_diff
                closest_pair = (sorted_nums[i], sorted_nums[j])
    
    return closest_pair