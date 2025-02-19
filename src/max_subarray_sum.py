def max_subarray_sum(arr, k):
    """
    Calculate the maximum sum of a subarray of size k in the given array.
    
    Args:
        arr (list): Input array of integers
        k (int): Size of the subarray
    
    Returns:
        int: Maximum sum of a subarray of size k, or None if no valid subarrays exist
    
    Raises:
        ValueError: If k is less than or equal to 0
    """
    # Validate input
    if k <= 0:
        raise ValueError("Subarray size (k) must be a positive integer")
    
    # If k is larger than the array, return None
    if k > len(arr):
        return None
    
    # Initialize max_sum with first k elements
    max_sum = sum(arr[:k])
    current_sum = max_sum
    
    # Sliding window approach
    for i in range(k, len(arr)):
        # Remove the first element of previous window and add the next element
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum