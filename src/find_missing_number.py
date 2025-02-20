def find_missing_number(nums):
    """
    Find the missing number in an array of unique positive integers between 1 and n.
    
    Args:
        nums (list): A list of unique positive integers between 1 and n.
    
    Returns:
        int: The missing number from the range.
    
    Raises:
        ValueError: If the input is invalid or no missing number can be found.
    """
    if not nums:
        raise ValueError("Input array cannot be empty")
    
    n = len(nums) + 1  # Total length including the missing number
    
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the given array
    actual_sum = sum(nums)
    
    # The difference is the missing number
    missing_number = expected_sum - actual_sum
    
    # Validate the result
    if missing_number < 1 or missing_number > n:
        raise ValueError("No valid missing number found")
    
    return missing_number