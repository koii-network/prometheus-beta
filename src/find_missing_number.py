def find_missing_number(nums):
    """
    Find the missing number in an array of unique positive integers between 1 and n.
    
    Args:
        nums (list): An array of unique positive integers between 1 and n.
    
    Returns:
        int: The missing number in the range.
    
    Raises:
        ValueError: If the input is invalid or empty.
    """
    # Check for invalid input
    if not nums:
        raise ValueError("Input array cannot be empty")
    
    # Get the expected length of the array (including the missing number)
    n = len(nums) + 1
    
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the given array
    actual_sum = sum(nums)
    
    # The difference is the missing number
    return expected_sum - actual_sum