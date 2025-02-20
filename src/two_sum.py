def two_sum(nums, target):
    """
    Find two numbers in the given array that add up to the target.
    
    Args:
        nums (list): List of integers to search
        target (int): Target sum to find
    
    Returns:
        list: Indices of the two numbers that add up to the target, 
              or an empty list if no such pair exists
    """
    # Create a dictionary to store complements
    num_dict = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_dict:
            # Return the indices of the two numbers
            return [num_dict[complement], i]
        
        # Store the current number and its index
        num_dict[num] = i
    
    # If no solution is found, return an empty list
    return []