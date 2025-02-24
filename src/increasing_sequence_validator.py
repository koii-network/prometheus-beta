def is_valid_increasing_sequence(arr):
    """
    Check if the given array is a valid sequence with distinct integers in strictly increasing order.
    
    Args:
        arr (list): Input list of integers to be validated
    
    Returns:
        bool: True if the array is a valid increasing sequence, False otherwise
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-integer elements
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty (considered valid)
    if len(arr) <= 1:
        return True
    
    # Convert to list of integers and validate
    try:
        int_arr = [int(x) for x in arr]
    except (ValueError, TypeError):
        raise ValueError("List must contain only integer-convertible elements")
    
    # Check for distinct elements and strictly increasing order
    seen = set()
    for i in range(len(int_arr)):
        # Check for duplicates
        if int_arr[i] in seen:
            return False
        
        # Add to seen set
        seen.add(int_arr[i])
        
        # Check strictly increasing order
        if i > 0 and int_arr[i] <= int_arr[i-1]:
            return False
    
    return True