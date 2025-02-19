def two_sum(nums, target):
    """
    Find two indices in the array that add up to the target sum.
    
    Args:
        nums (list): List of integers to search
        target (int): Target sum to find
    
    Returns:
        list: A list of two indices where the corresponding values add up to the target
              Returns an empty list if no such indices exist
    """
    # Create a dictionary to store complement values and their indices
    num_dict = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_dict:
            # Return the indices of the two numbers that sum to target
            return [num_dict[complement], i]
        
        # Store the current number and its index
        num_dict[num] = i
    
    # If no solution is found, return an empty list
    return []