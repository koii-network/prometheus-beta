def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a subarray with length k in the given array.
    
    Args:
        arr (list): Input list of integers
        k (int): Length of the subarray
    
    Returns:
        int: Maximum sum of a subarray of length k
    
    Raises:
        ValueError: If k is larger than the array length or k is non-positive
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    if k <= 0:
        raise ValueError("k must be a positive integer")
    
    if k > len(arr):
        raise ValueError("k cannot be larger than the array length")
    
    # If array is empty, return 0
    if not arr:
        return 0
    
    # Initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Sliding window approach
    for i in range(k, len(arr)):
        # Remove first element of previous window and add new element
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum