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
    max_sum = float('-inf')
    current_sum = 0
    start = 0

    for end in range(n):
        # Add current element to sum
        current_sum += A[end]

        # Shrink window from start if we have enough elements
        while end - start + 1 >= k:
            # Check if current subarray meets sum constraint
            if current_sum >= s:
                max_sum = max(max_sum, current_sum)
            
            # Remove start element and move window
            current_sum -= A[start]
            start += 1

    return max_sum if max_sum != float('-inf') else -1