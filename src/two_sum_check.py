def two_sum_check(nums, target_sum):
    """
    Check if there exist two numbers in the array that sum up to the target sum.
    
    Args:
        nums (list): A list of numbers to search through
        target_sum (int): The target sum to find
    
    Returns:
        bool: True if two numbers in the list sum up to target_sum, False otherwise
    """
    # Use a set to track numbers we've seen
    seen = set()
    
    # Iterate through the numbers in the array
    for num in nums:
        # Check if the complement exists in the seen set
        complement = target_sum - num
        if complement in seen:
            return True
        
        # Add the current number to the seen set
        seen.add(num)
    
    # No two numbers sum up to target_sum
    return False