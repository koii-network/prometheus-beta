def max_subarray_sum(arr, k):
    """
    Returns the maximum sum of a subarray of length 'k' within a given list of integers.
    
    Args:
        arr (list): Input list of integers
        k (int): Length of the subarray to find maximum sum
    
    Returns:
        list: Maximum sum if valid, otherwise an empty list
    """
    # If k is larger than the list length, return empty list
    if k > len(arr):
        return []
    
    # If k is 0, return empty list
    if k == 0:
        return []
    
    # Initialize with the first k elements
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Sliding window approach
    for i in range(k, len(arr)):
        # Remove first element of previous window and add new element
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum