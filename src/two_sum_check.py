def two_sum_check(numbers, target_sum):
    """
    Check if there exist two numbers in the array that sum up to the target sum.
    
    Args:
        numbers (list): A list of numbers to search through
        target_sum (int): The target sum to find
    
    Returns:
        bool: True if two numbers in the list sum up to the target, False otherwise
    """
    # Create a set to store seen numbers for O(n) time complexity
    seen = set()
    
    for num in numbers:
        complement = target_sum - num
        if complement in seen:
            return True
        seen.add(num)
    
    return False