def find_missing_number(nums):
    """
    Find the missing number in an array of unique positive integers between 1 and n.
    
    Args:
        nums (list): A list of unique positive integers between 1 and n.
    
    Returns:
        int: The missing number in the sequence.
    
    Raises:
        ValueError: If the input is not a valid list of unique positive integers.
    """
    # Validate input
    if not nums or not isinstance(nums, list):
        raise ValueError("Input must be a non-empty list")
    
    # Determine the expected range
    n = len(nums) + 1
    
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2
    
    # Calculate the actual sum of the given numbers
    actual_sum = sum(nums)
    
    # The missing number is the difference between expected and actual sums
    return expected_sum - actual_sum