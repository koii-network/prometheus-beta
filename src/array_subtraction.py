def subtract_arrays_mod_10(A: list[int], B: list[int]) -> list[int]:
    """
    Perform element-wise subtraction of two arrays with modulo 10 operation.
    
    Args:
    A (list[int]): First input array of 10 integers
    B (list[int]): Second input array of 10 integers
    
    Returns:
    list[int]: Result array where each element is (A[i] - B[i]) % 10, 
               with negative results set to 0
    
    Raises:
    ValueError: If input arrays are not of length 10
    """
    # Validate input array lengths
    if len(A) != 10 or len(B) != 10:
        raise ValueError("Both input arrays must be of length 10")
    
    # Create result array using list comprehension for O(n) time complexity
    return [max(0, (A[i] - B[i]) % 10) for i in range(10)]