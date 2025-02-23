def two_sum_check(numbers, target_sum):
    """
    Check if there exist two numbers in the array that sum up to the target sum.
    
    Args:
        numbers (list): A list of numbers to search through
        target_sum (int): The target sum to find
    
    Returns:
        bool: True if two numbers in the array sum to target_sum, False otherwise
    """
    # Use a set to track numbers we've seen for O(n) time complexity
    seen = set()
    
    for num in numbers:
        complement = target_sum - num
        
        # If the complement is already in seen, we found two numbers that sum to target
        if complement in seen:
            return True
        
        # Add the current number to seen
        seen.add(num)
    
    # No two numbers found that sum to target
    return False