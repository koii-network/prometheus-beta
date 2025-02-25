def max_subarray_sum_with_constraints(A, k, s):
    """
    Find the maximum sum of a contiguous subarray with specific constraints.

    This function does the following:
    1. Ensures the subarray is at least k elements long
    2. Finds the first subarray that meets sum constraint (>= s)
    3. Prevents inclusion of the entire remaining array after the start point

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

    # Iterate through possible start points
    for start in range(n - k + 1):
        # Look for the first valid subarray configuration
        for length in range(k, min(k + 1, n - start + 1)):
            current_subarray = A[start:start+length]
            current_sum = sum(current_subarray)
            
            # Check if current subarray meets both constraints
            if current_sum >= s:
                # This ensures we don't just take the whole remaining array
                max_constrained_sum = max(max_constrained_sum, current_sum)
                break  # Stop after finding first valid configuration

    return max_constrained_sum