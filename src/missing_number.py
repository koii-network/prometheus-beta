def find_missing_number(nums):
    """
    Find the missing number in an array of unique positive integers between 1 and n.
    
    Args:
        nums (list): A list of unique positive integers between 1 and n (inclusive), 
                     with one number missing.
    
    Returns:
        int: The missing number.
    
    Raises:
        ValueError: If the input is invalid (empty, contains non-positive, or out of range numbers).
    """
    # Validate input
    if not nums:
        raise ValueError("Input array cannot be empty")
    
    # Determine the expected length of the complete array
    n = len(nums) + 1
    
    # Validate all numbers are within the expected range
    if any(num < 1 or num > n for num in nums):
        raise ValueError(f"All numbers must be between 1 and {n}")
    
    # Use the sum of first n natural numbers formula to find the missing number
    # Total sum of numbers from 1 to n is n * (n + 1) // 2
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    
    return expected_sum - actual_sum