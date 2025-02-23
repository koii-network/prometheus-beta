def two_sum_target(nums, target):
    """
    Check if any two unique numbers in the input array sum to the target.

    Args:
        nums (list): A list of unique integers to search through.
        target (int): The target sum to find.

    Returns:
        bool: True if any two numbers in the array sum to the target, False otherwise.

    Raises:
        TypeError: If input is not a list or if elements are not integers.
        ValueError: If the list contains duplicates.
    """
    # Validate input types
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    if not all(isinstance(num, int) for num in nums):
        raise TypeError("All elements must be integers")
    
    # Check for duplicate values
    if len(set(nums)) != len(nums):
        raise ValueError("Input list must contain unique integers")
    
    # Create a set for O(n) lookup
    num_set = set(nums)
    
    # Check each number for its complement
    for num in nums:
        complement = target - num
        # Ensure we're not using the same number twice
        if complement in num_set and complement != num:
            return True
    
    return False