def is_valid_increasing_sequence(arr):
    """
    Check if the given array is a valid sequence with distinct integers in strictly increasing order.
    
    Args:
        arr (list): Input list of integers to validate
    
    Returns:
        bool: True if the sequence is valid, False otherwise
    
    A valid sequence meets these criteria:
    1. Contains only integers
    2. All elements are distinct
    3. Elements are in strictly increasing order
    """
    # Check if input is a list
    if not isinstance(arr, list):
        return False
    
    # Check if list is empty
    if not arr:
        return False
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        return False
    
    # Check for distinct elements
    if len(set(arr)) != len(arr):
        return False
    
    # Check strictly increasing order
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False
    
    return True