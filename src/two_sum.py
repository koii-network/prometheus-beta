def two_sum(nums, target):
    """
    Find two indices in the given array that add up to the target sum.

    Args:
        nums (list): A list of integers to search through
        target (int): The target sum to find

    Returns:
        list: A list of two indices where the corresponding numbers sum to the target.
              Returns an empty list if no such indices exist.

    Raises:
        TypeError: If input is not a list or if elements are not integers
        ValueError: If target is not a number
    """
    # Validate input types
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target, (int, float)):
        raise ValueError("Target must be a number")
    
    # Check if all elements are numbers
    if not all(isinstance(num, (int, float)) for num in nums):
        raise TypeError("All list elements must be numbers")
    
    # Use a hash map for O(n) time complexity
    num_dict = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_dict:
            return [num_dict[complement], i]
        
        # Store the current number and its index
        num_dict[num] = i
    
    # Return empty list if no solution found
    return []