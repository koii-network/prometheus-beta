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

    # Sliding window approach
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += A[end]
            current_window_size = end - start + 1

            # Check if current window meets length and sum constraints
            if current_window_size >= k and current_sum >= s:
                max_constrained_sum = max(max_constrained_sum, current_sum)

    return max_constrained_sum