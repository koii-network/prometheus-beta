def max_subarray_sum_with_constraints(A, k, s):
    """
    Find the maximum sum of a contiguous subarray with specific constraints.

    Args:
        A (list): An array of integers
        k (int): Minimum number of elements in the subarray
        s (int): Minimum sum threshold for the subarray

    Returns:
        int: Maximum sum of a contiguous subarray with at least k elements
             and sum >= s, or -1 if no such subarray exists

    Raises:
        ValueError: If input constraints are invalid
    """
    # Input validation
    if not isinstance(A, list):
        raise ValueError("Input A must be a list of integers")
    
    if not isinstance(k, int) or k < 1:
        raise ValueError("k must be a positive integer")
    
    # If array is too short to meet minimum length requirement
    if len(A) < k:
        return -1

    n = len(A)
    max_constrained_sum = -1

    # Try all possible subarrays of at least k elements
    for start in range(n - k + 1):
        for length in range(k, n - start + 1):
            current_sum = sum(A[start:start+length])
            if current_sum >= s:
                max_constrained_sum = max(max_constrained_sum, current_sum)

    return max_constrained_sum