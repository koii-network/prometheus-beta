def find_missing_number(nums):
    """
    Find the missing number in an array of integers from 1 to n+1.
    
    Args:
        nums (list): A list of integers where one number between 1 and n+1 is missing.
    
    Returns:
        int: The missing number.
    
    Raises:
        ValueError: If the input list is empty or invalid.
    """
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    # Expected sum of numbers from 1 to n+1
    n = len(nums) + 1
    expected_sum = (n * (n + 1)) // 2
    
    # Actual sum of the given array
    actual_sum = sum(nums)
    
    # The missing number is the difference between expected and actual sum
    return expected_sum - actual_sum