def max_subarray_sum_constraint(A, k, s):
    """
    Find the maximum sum of a contiguous subarray with at least k elements 
    and sum greater than or equal to s.
    
    Args:
        A (list): Input array of integers
        k (int): Minimum number of elements in the subarray
        s (int): Minimum sum threshold
    
    Returns:
        int: Maximum sum of a subarray meeting the constraints, 
             or -1 if no such subarray exists
    """
    n = len(A)
    
    # If array is too short to meet minimum length requirement
    if n < k:
        return -1
    
    # Compute prefix sums for efficient subarray sum calculation
    prefix_sums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i-1] + A[i-1]
    
    max_sum = float('-inf')
    found_valid_subarray = False
    
    # Sliding window approach
    for start in range(n):
        for end in range(start + k, n + 1):
            # Calculate subarray sum using prefix sums
            current_sum = prefix_sums[end] - prefix_sums[start]
            
            # Check if current subarray meets both constraints
            if end - start >= k and current_sum >= s:
                max_sum = max(max_sum, current_sum)
                found_valid_subarray = True
    
    return max_sum if found_valid_subarray else -1