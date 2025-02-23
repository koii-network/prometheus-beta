def modulo_subtraction(A, B):
    """
    Perform element-wise subtraction with modulo 10 operation between two arrays.
    
    Args:
        A (list): First input array of integers, length 10
        B (list): Second input array of integers, length 10
    
    Returns:
        list: A new array C where C[i] = max(0, (A[i] - B[i]) % 10)
    
    Raises:
        ValueError: If input arrays are not of length 10
    """
    # Validate input arrays
    if len(A) != 10 or len(B) != 10:
        raise ValueError("Both input arrays must be of length 10")
    
    # Create result array using list comprehension for O(n) time complexity
    return [max(0, (a - b + 10) % 10) for a, b in zip(A, B)]