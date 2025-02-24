def two_sum(numbers, target):
    """
    Determine if there exist two numbers in the array that sum to the target.

    Args:
        numbers (list): A list of numbers to search through
        target (int/float): The target sum to find

    Returns:
        bool: True if two numbers in the list sum to target, False otherwise

    Raises:
        TypeError: If input is not a list or if target is not a number
    """
    # Validate input types
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be a number")
    
    # Use two-pointer approach for efficiency
    # First, sort a copy of the list to avoid modifying original
    sorted_nums = sorted(enumerate(numbers), key=lambda x: x[1])
    
    # Two-pointer search
    left, right = 0, len(sorted_nums) - 1
    
    while left < right:
        current_sum = sorted_nums[left][1] + sorted_nums[right][1]
        
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return False