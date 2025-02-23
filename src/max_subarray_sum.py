def max_subarray_sum_with_constraints(A, k, s):
    """
    Find the maximum sum of a contiguous subarray with specific constraints.

    Args:
        A (list[int]): Input array of integers
        k (int): Minimum number of elements required in the subarray
        s (int): Minimum sum required for the subarray

    Returns:
        int: Maximum sum of a contiguous subarray meeting the constraints,
             or -1 if no such subarray exists

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Input validation
    if not A or k <= 0 or k > len(A):
        return -1

    n = len(A)
    max_sum = -1
    current_sum = 0
    window_start = 0
    elements_count = 0

    for window_end in range(n):
        # Add current element to sum and increment count
        current_sum += A[window_end]
        elements_count += 1

        # Slide window while maintaining constraints
        while window_end - window_start + 1 > k and current_sum >= s:
            if elements_count >= k:
                max_sum = max(max_sum, current_sum)
            
            current_sum -= A[window_start]
            window_start += 1
            elements_count -= 1

        # Check if current window meets all constraints
        if elements_count >= k and current_sum >= s:
            max_sum = max(max_sum, current_sum)

        # Reset window if conditions aren't met
        if elements_count > k:
            current_sum -= A[window_start]
            window_start += 1
            elements_count -= 1

    return max_sum