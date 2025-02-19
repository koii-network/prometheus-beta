def subtract_and_modulo_arrays(A, B):
    """
    Subtract two arrays element-wise with modulo 10 and non-negative constraint.
    
    Args:
        A (list): First input array of integers (length 10)
        B (list): Second input array of integers (length 10)
    
    Returns:
        list: Resulting array where C[i] = max(0, (A[i] - B[i]) % 10)
    
    Raises:
        ValueError: If input arrays are not of length 10
    """
    # Validate input array lengths
    if len(A) != 10 or len(B) != 10:
        raise ValueError("Both input arrays must be of length 10")
    
    # Create result array using list comprehension for O(n) time complexity
    return [max(0, (a - b) % 10) for a, b in zip(A, B)]