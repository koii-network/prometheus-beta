def find_missing_number(nums):
    """
    Find the missing number in a list of integers from 1 to n.
    
    Args:
        nums (list): A list of integers with one number missing from the range 1 to n.
    
    Returns:
        int: The missing number.
    
    Raises:
        ValueError: If the input list is empty or does not contain a valid range.
    """
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    n = len(nums) + 1  # Total expected numbers in the range
    
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the given list
    actual_sum = sum(nums)
    
    # The difference is the missing number
    return expected_sum - actual_sum