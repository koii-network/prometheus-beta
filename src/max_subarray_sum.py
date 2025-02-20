def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a contiguous subarray with length k.
    
    Args:
        arr (list): An array of integers
        k (int): The length of the subarray
    
    Returns:
        int: The maximum sum of a contiguous subarray of length k
    
    Raises:
        ValueError: If k is larger than the array length or k is non-positive
    """
    if k <= 0:
        raise ValueError("k must be a positive integer")
    
    if k > len(arr):
        raise ValueError("k cannot be larger than the array length")
    
    # Initialize the first window sum
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Sliding window approach
    for i in range(k, len(arr)):
        # Remove the first element of the previous window and add the next element
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum