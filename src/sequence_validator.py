def is_valid_sequence(arr):
    """
    Check if the given array is a valid sequence with distinct integers 
    in strictly increasing order.
    
    Args:
        arr (list): Input list of integers to validate
    
    Returns:
        bool: True if the sequence is valid, False otherwise
    
    Raises:
        TypeError: If input is not a list
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Empty list or single element list is valid
    if len(arr) <= 1:
        return True
    
    # Check for strictly increasing and distinct elements
    for i in range(1, len(arr)):
        # Check if current element is an integer
        if not isinstance(arr[i], int):
            return False
        
        # Check if current element is not the same as previous
        if arr[i] == arr[i-1]:
            return False
        
        # Check if current element is less than or equal to previous
        if arr[i] <= arr[i-1]:
            return False
    
    return True