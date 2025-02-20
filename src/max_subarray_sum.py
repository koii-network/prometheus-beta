def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a contiguous subarray with length k.
    
    Args:
        arr (list): An array of integers
        k (int): Length of the subarray
    
    Returns:
        int: Maximum sum of a contiguous subarray of length k
    
    Raises:
        ValueError: If k is larger than the array length or k is non-positive
    """
    # Validate input
    if k <= 0:
        raise ValueError("k must be a positive integer")
    
    if k > len(arr):
        raise ValueError("k cannot be larger than the array length")
    
    # Handle trivial case of k == array length
    if k == len(arr):
        return sum(arr)
    
    # Sliding window approach
    # Initial window sum
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Slide the window and update max sum
    for i in range(k, len(arr)):
        # Remove first element of previous window and add next element
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum