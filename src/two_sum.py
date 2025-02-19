def two_sum(nums, target):
    """
    Determine if any two numbers in the input array sum up to the target.
    
    Args:
        nums (list): A list of unique integers
        target (int): The target sum to find
    
    Returns:
        bool: True if any two numbers in the array sum to the target, False otherwise
    
    Raises:
        TypeError: If input is not a list or contains non-integer elements
        ValueError: If the input list contains duplicate elements
    """
    # Validate input types
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    if not all(isinstance(num, int) for num in nums):
        raise TypeError("All elements must be integers")
    
    # Check for duplicates
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