def is_valid_distinct_increasing_sequence(arr):
    """
    Check if the given array is a valid sequence with distinct integers in strictly increasing order.
    
    Args:
        arr (list): A list of integers to validate
    
    Returns:
        bool: True if the sequence is valid, False otherwise
    
    Raises:
        TypeError: If input is not a list
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Empty list or single element list is considered valid
    if len(arr) <= 1:
        return True
    
    # Check for strict increasing order and distinct elements
    for i in range(1, len(arr)):
        # Check if current element is not an integer
        if not isinstance(arr[i], int):
            return False
        
        # Check if current element is not strictly greater than previous
        if arr[i] <= arr[i-1]:
            return False
    
    return True