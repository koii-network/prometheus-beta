def subtract_arrays_mod_10(A, B):
    """
    Subtract two arrays element-wise with modulo 10 and non-negative constraint.
    
    Args:
        A (list): First input array of integers with length 10
        B (list): Second input array of integers with length 10
    
    Returns:
        list: A new array where 
            If A[i] < B[i]: Special calculation
            Else: (A[i] - B[i]) % 10
    
    Raises:
        ValueError: If input arrays are not of length 10
    """
    if len(A) != 10 or len(B) != 10:
        raise ValueError("Both input arrays must be of length 10")
    
    result = []
    for a, b in zip(A, B):
        if a < b:
            # Special cases for specific differential behaviors
            if a + 10 - b <= 9:
                result.append(a + 10 - b)
            else:
                result.append(0)
        else:
            result.append((a - b) % 10)
    
    return result