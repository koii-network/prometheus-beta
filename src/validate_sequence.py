def is_valid_increasing_sequence(arr):
    """
    Check if the given array is a valid sequence with distinct integers in strictly increasing order.
    
    Args:
        arr (list): Input list of integers to validate
    
    Returns:
        bool: True if the sequence is valid, False otherwise
    
    Conditions for a valid sequence:
    1. All elements must be integers
    2. Elements must be in strictly increasing order
    3. No duplicate values allowed
    """
    # Check if input is a list
    if not isinstance(arr, list):
        return False
    
    # Empty list or single element list is considered valid
    if len(arr) <= 1:
        return True
    
    # Check that all elements are integers
    if not all(isinstance(x, int) for x in arr):
        return False
    
    # Check for duplicates
    if len(set(arr)) != len(arr):
        return False
    
    # Check strictly increasing order
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False
    
    return True