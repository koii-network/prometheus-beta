def two_sum_target(nums, target):
    """
    Determine if any two unique numbers in the array sum to the target.
    
    Args:
        nums (list): A list of unique integers
        target (int): The target sum to find
    
    Returns:
        bool: True if any two numbers sum to the target, False otherwise
    """
    # Use a set for O(n) time complexity
    seen = set()
    
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    
    return False