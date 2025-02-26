def find_missing_number(arr):
    """
    Find the missing number in an array of integers from 1 to n+1.
    
    Args:
        arr (list): A list of integers containing numbers from 1 to n+1, 
                    with one number missing.
    
    Returns:
        int: The missing number.
    
    Raises:
        ValueError: If the input is invalid (empty list, non-integer elements, etc.)
    
    Examples:
        >>> find_missing_number([1, 3, 4, 5])
        2
        >>> find_missing_number([2, 3, 4, 5, 6])
        1
    """
    # Input validation
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Expected set of numbers from 1 to n+1
    n = len(arr) + 1
    
    # Calculate expected sum of numbers from 1 to n+1
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate actual sum of the array
    actual_sum = sum(arr)
    
    # Missing number is the difference between expected and actual sum
    return expected_sum - actual_sum