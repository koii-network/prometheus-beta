def is_valid_increasing_sequence(arr):
    """
    Check if the given array is a valid sequence with distinct integers in strictly increasing order.
    
    Args:
        arr (list): Input list of integers to check
    
    Returns:
        bool: True if the sequence is valid, False otherwise
    
    Conditions for a valid sequence:
    - Must contain at least one element
    - All elements must be distinct
    - Elements must be in strictly increasing order
    """
    # Check if array is empty
    if not arr:
        return False
    
    # Check for duplicates by comparing length of set to original array
    if len(set(arr)) != len(arr):
        return False
    
    # Check if sequence is strictly increasing
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False
    
    return True