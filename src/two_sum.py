def two_sum_target(nums, target):
    """
    Check if any two unique numbers in the array sum to the target.
    
    Args:
        nums (list): An array of unique integers
        target (int): The target sum to find
    
    Returns:
        bool: True if any two numbers in the array sum to the target, False otherwise
    """
    # Create a set for O(1) lookup
    num_set = set(nums)
    
    for num in nums:
        complement = target - num
        # Check if the complement exists in the set, 
        # and ensure it's not the same number being used twice
        if complement in num_set and complement != num:
            return True
    
    return False