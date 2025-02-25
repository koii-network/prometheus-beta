def calculate_array_difference(A: list[int], B: list[int]) -> list[int]:
    """
    Calculate element-wise difference between two arrays with modulo 10 and non-negative constraint.
    
    Args:
        A (list[int]): First input array of integers (length 10)
        B (list[int]): Second input array of integers (length 10)
    
    Returns:
        list[int]: Array C where C[i] = max(0, (A[i] - B[i]) % 10)
    
    Raises:
        ValueError: If input arrays are not of length 10
    """
    # Validate input array lengths
    if len(A) != 10 or len(B) != 10:
        raise ValueError("Both input arrays must be of length 10")
    
    # Create result array using list comprehension for O(n) time complexity
    return [max(0, (a - b) % 10) for a, b in zip(A, B)]