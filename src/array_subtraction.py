def subtract_arrays_mod_10(A, B):
    """
    Subtract two arrays element-wise with modulo 10 and non-negative constraint.
    
    Args:
        A (list): First input array of integers with length 10
        B (list): Second input array of integers with length 10
    
    Returns:
        list: A new array where 
            If A[i] < B[i]: C[i] = 0
            Else: C[i] = (A[i] - B[i]) % 10
    
    Raises:
        ValueError: If input arrays are not of length 10
    """
    if len(A) != 10 or len(B) != 10:
        raise ValueError("Both input arrays must be of length 10")
    
    return [0 if a < b else (a - b) % 10 for a, b in zip(A, B)]