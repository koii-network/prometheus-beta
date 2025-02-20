def find_missing_number(arr):
    """
    Find the missing number in an array of integers from 1 to n+1.
    
    Args:
        arr (list): A list of integers with one missing number between 1 and n+1
    
    Returns:
        int: The missing number
    
    Raises:
        ValueError: If the input is invalid (empty list, not a valid array of 1 to n+1)
    """
    # Check for invalid input
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Calculate the expected sum of numbers from 1 to n+1
    n = len(arr) + 1
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the given array
    actual_sum = sum(arr)
    
    # The missing number is the difference between expected and actual sums
    missing_number = expected_sum - actual_sum
    
    return missing_number