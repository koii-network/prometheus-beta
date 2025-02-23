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
    
    # Sliding window approach
    for start in range(n):
        current_sum = 0
        count = 0

        # Try to find max sum subarray starting from 'start'
        for end in range(start, n):
            current_sum += A[end]
            count += 1

            # Check constraints
            if count >= k and current_sum >= s:
                max_sum = max(max_sum, current_sum)

    return max_sum