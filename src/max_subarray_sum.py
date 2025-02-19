def max_subarray_sum(arr, k):
    """
    Calculate the maximum sum of a subarray with size k.
    
    Args:
        arr (list): Input list of integers
        k (int): Size of the subarray
    
    Returns:
        int: Maximum sum of a subarray of size k, or None if k is invalid
    """
    # Validate input
    if not arr or k <= 0 or k > len(arr):
        return None
    
    # Calculate initial window sum
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Slide the window and update max sum
    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum