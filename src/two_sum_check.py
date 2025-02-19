def two_sum_check(nums: list[int], target: int) -> bool:
    """
    Check if any two unique numbers in the given array sum to the target number.
    
    Args:
        nums (list[int]): An array of unique integers
        target (int): The target sum to find
    
    Returns:
        bool: True if any two numbers in the array sum to the target, False otherwise
    
    Raises:
        ValueError: If the input list is empty or contains duplicates
    """
    # Validate input
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    if len(nums) != len(set(nums)):
        raise ValueError("Input list must contain unique integers")
    
    # Use a set for O(n) time complexity
    seen = set()
    
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    
    return False