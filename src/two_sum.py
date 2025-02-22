def find_two_sum_indices(nums, target):
    """
    Find two indices in an array that add up to the target sum.
    
    Args:
        nums (list): List of integers to search
        target (int): Target sum to find
    
    Returns:
        list: A list of two indices where the corresponding values add up to the target
              Returns an empty list if no such indices are found
    
    Raises:
        TypeError: If input is not a list or target is not an integer
    """
    # Validate input types
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Use a hash map for O(n) time complexity
    num_dict = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_dict:
            return [num_dict[complement], i]
        
        # Store the current number's index
        num_dict[num] = i
    
    # If no solution is found
    return []