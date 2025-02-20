def is_valid_increasing_sequence(arr):
    """
    Check if the given array is a valid sequence with distinct integers in strictly increasing order.
    
    Args:
        arr (list): Input list of integers to validate
    
    Returns:
        bool: True if the sequence is valid, False otherwise
    
    Conditions:
    - All elements must be distinct
    - Elements must be in strictly increasing order
    - Supports non-empty lists
    """
    # Check if input is a list and not empty
    if not isinstance(arr, list) or len(arr) == 0:
        return False
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        return False
    
    # Check for distinct elements
    if len(set(arr)) != len(arr):
        return False
    
    # Check for strictly increasing order
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False
    
    return True