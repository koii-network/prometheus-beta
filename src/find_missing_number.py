def find_missing_number(nums):
    """
    Find the missing number in an array of integers from 1 to n+1.
    
    Args:
        nums (list): A list of integers containing distinct numbers from 1 to n+1 
                     with one number missing.
    
    Returns:
        int: The missing number.
    
    Raises:
        ValueError: If the input is not a valid list or is empty.
    """
    # Validate input
    if not isinstance(nums, list) or len(nums) == 0:
        raise ValueError("Input must be a non-empty list of integers")
    
    # Use Gauss formula to calculate the expected sum of numbers from 1 to n+1
    n = len(nums) + 1
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the given numbers
    actual_sum = sum(nums)
    
    # The difference is the missing number
    return expected_sum - actual_sum