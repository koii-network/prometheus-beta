def find_closest_pair(numbers):
    """
    Find the closest pair of numbers in an array.
    
    Args:
        numbers (list): A list of numbers
    
    Returns:
        tuple: A tuple containing the two closest numbers 
        
    Raises:
        ValueError: If the input list has less than 2 numbers
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least 2 numbers")
    
    # Sort the numbers to help with finding the closest pair
    sorted_nums = sorted(numbers)
    
    # Initialize variables to track the closest pair
    min_diff = float('inf')
    closest_pair = None
    
    # Compare adjacent numbers in the sorted list
    for i in range(len(sorted_nums) - 1):
        current_diff = abs(sorted_nums[i] - sorted_nums[i+1])
        
        # Update if current difference is smaller
        if current_diff < min_diff:
            min_diff = current_diff
            closest_pair = (sorted_nums[i], sorted_nums[i+1])
        
        # If differences are equal, choose the smaller pair lexicographically
        elif current_diff == min_diff:
            if sorted_nums[i] < closest_pair[0] or \
               (sorted_nums[i] == closest_pair[0] and sorted_nums[i+1] < closest_pair[1]):
                closest_pair = (sorted_nums[i], sorted_nums[i+1])
    
    return closest_pair