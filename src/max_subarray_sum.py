def max_subarray_sum(arr, k):
    """
    Calculate the maximum sum of a subarray with size k.
    
    Args:
        arr (list): Input list of integers
        k (int): Size of the subarray
    
    Returns:
        int: Maximum sum of a subarray of size k
             Returns None if k is larger than the array length
    """
    # Check if k is larger than array length
    if k > len(arr):
        return None
    
    # If k is 0 or negative, return None
    if k <= 0:
        return None
    
    # Initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window and update max sum
    for i in range(k, len(arr)):
        # Remove first element of previous window and add new element
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum