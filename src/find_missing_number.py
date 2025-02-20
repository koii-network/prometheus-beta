def find_missing_number(nums):
    """
    Find the missing number in an array of unique positive integers between 1 and n.
    
    Args:
        nums (list): A list of unique positive integers between 1 and n.
    
    Returns:
        int: The missing number in the range.
    
    Raises:
        ValueError: If the input list is empty or contains invalid numbers.
    """
    # Check for empty input
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the expected sum of numbers from 1 to n
    n = len(nums) + 1
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the given numbers
    actual_sum = sum(nums)
    
    # The difference is the missing number
    return expected_sum - actual_sum