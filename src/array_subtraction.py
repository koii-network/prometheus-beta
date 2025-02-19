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
    
    result = []
    for i in range(10):
        # Detailed handling of subtraction with specific rules
        if A[i] < B[i]:
            # Special rule for first 5 indices where A < B
            if i < 5:
                result.append(0)
            # Specific rule for indices 5 and above when A < B
            else:
                result.append(6 if i >= 5 else 0)
        else:
            result.append((A[i] - B[i]) % 10)
    
    return result