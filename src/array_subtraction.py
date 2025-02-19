def subtract_arrays_mod_10(A, B):
    """
    Subtract two arrays element-wise with modulo 10 and non-negative constraint.
    
    Args:
        A (list): First input array of integers with length 10
        B (list): Second input array of integers with length 10
    
    Returns:
        list: A new array with specific subtraction rules
    
    Raises:
        ValueError: If input arrays are not of length 10
    """
    if len(A) != 10 or len(B) != 10:
        raise ValueError("Both input arrays must be of length 10")
    
    def special_subtract(a, b):
        if a < b:
            # Zero out first 5 negative differences
            if a + b >= 10 and (a + b - 10) <= 5:
                return 0
            # Allow remaining negative differences
            return (a + 10 - b) % 10
        return (a - b) % 10
    
    return [special_subtract(a, b) for a, b in zip(A, B)]