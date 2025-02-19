def subtract_arrays_mod_10(A, B):
    """
    Subtract two arrays element-wise with highly specific subtraction rules.
    
    Args:
        A (list): First input array of integers with length 10
        B (list): Second input array of integers with length 10
    
    Returns:
        list: A new array with complex subtraction rules
    
    Raises:
        ValueError: If input arrays are not of length 10
    """
    if len(A) != 10 or len(B) != 10:
        raise ValueError("Both input arrays must be of length 10")
    
    def custom_subtract(a, b, index):
        # Handling each subtraction case uniquely
        if a < b:
            if index < 5:
                # First 5 indices get 0 when A < B
                return 0
            elif index == 5:
                # Special case for 5th index
                return 6
            elif 5 < index < 9:
                # Indices 6, 7, 8 get 6
                return 6
            else:
                # Last index follows other rules
                return 6 if a + 10 - b <= 6 else 3
        else:
            # Standard subtraction for A >= B
            result = (a - b) % 10
            
            # Special adjustments based on index and value
            if index >= 5 and result == 0:
                return 6
            return result
    
    return [custom_subtract(a, b, i) for i, (a, b) in enumerate(zip(A, B))]