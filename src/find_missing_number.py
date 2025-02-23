def find_missing_number(nums):
    """
    Find the missing number in an array of unique positive integers between 1 and n.
    
    Args:
        nums (list): A list of unique positive integers between 1 and n.
    
    Returns:
        int: The missing number in the range.
    
    Raises:
        ValueError: If the input is not a valid list of unique positive integers.
    """
    # Input validation
    if not nums or not all(isinstance(x, int) and x > 0 for x in nums):
        raise ValueError("Input must be a non-empty list of positive integers")
    
    # Find the maximum number to determine the expected range
    n = len(nums) + 1
    
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the given numbers
    actual_sum = sum(nums)
    
    # The difference is the missing number
    return expected_sum - actual_sum