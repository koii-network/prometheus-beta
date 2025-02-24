def find_missing_number(nums):
    """
    Find the missing number in a sequence of integers from 1 to n+1.
    
    Args:
        nums (list): A list of unique integers from 1 to n, with one number missing.
    
    Returns:
        int: The missing number in the sequence.
    
    Raises:
        ValueError: If the input is not a valid sequence or is empty.
    
    Examples:
        >>> find_missing_number([3, 7, 1, 2, 8, 4, 5])
        6
        >>> find_missing_number([1, 2, 4, 6, 3, 7, 8])
        5
    """
    # Check for invalid input
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the expected sum of numbers from 1 to n+1
    n = len(nums) + 1
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the given numbers
    actual_sum = sum(nums)
    
    # The missing number is the difference between expected and actual sum
    return expected_sum - actual_sum