def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a subarray with length k in the given array.

    Args:
        arr (list): Input array of integers
        k (int): Length of the subarray

    Returns:
        int: Maximum sum of a subarray of length k
        
    Raises:
        ValueError: If k is larger than the array length or k is not a positive integer
    """
    # Input validation
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer")
    
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    if k > len(arr):
        raise ValueError(f"k ({k}) cannot be larger than the array length ({len(arr)})")
    
    # If k equals array length, return sum of entire array
    if k == len(arr):
        return sum(arr)
    
    # Sliding window approach
    # Compute initial window sum
    current_window_sum = sum(arr[:k])
    max_sum = current_window_sum
    
    # Slide the window and update max sum
    for i in range(k, len(arr)):
        # Remove the first element of previous window and add the new element
        current_window_sum = current_window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_window_sum)
    
    return max_sum