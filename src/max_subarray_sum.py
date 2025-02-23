def max_subarray_sum(arr, k):
    """
    Calculate the maximum sum of a contiguous subarray with length k.
    
    Args:
        arr (list): Input list of integers
        k (int): Length of the subarray
    
    Returns:
        int: Maximum sum of a contiguous subarray of length k
    
    Raises:
        ValueError: If k is larger than the array length or k is less than or equal to 0
    """
    # Validate input
    if k <= 0:
        raise ValueError("k must be a positive integer")
    
    if k > len(arr):
        raise ValueError("k cannot be larger than the array length")
    
    # If array is empty or k is zero, return 0
    if not arr or k == 0:
        return 0
    
    # Initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Sliding window approach
    for i in range(k, len(arr)):
        # Remove the first element of previous window and add the new element
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum