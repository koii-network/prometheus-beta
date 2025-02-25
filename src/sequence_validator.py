def is_valid_increasing_sequence(arr):
    """
    Check if the given array is a valid sequence with distinct integers in strictly increasing order.
    
    Args:
        arr (list): Input list of integers to validate
    
    Returns:
        bool: True if the sequence is valid, False otherwise
    
    Raises:
        TypeError: If input is not a list
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Empty list or single element list is considered valid
    if len(arr) <= 1:
        return True
    
    # Check that all elements are integers
    if not all(isinstance(x, int) for x in arr):
        return False
    
    # Check for strict increasing order and distinct elements
    for i in range(1, len(arr)):
        # Check if current element is strictly greater than previous
        if arr[i] <= arr[i-1]:
            return False
    
    return True