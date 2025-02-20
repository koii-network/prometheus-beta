def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a subarray with length k in the given array.
    
    Args:
        arr (list): Input list of integers
        k (int): Length of the subarray
    
    Returns:
        int: Maximum sum of any subarray of length k
    
    Raises:
        ValueError: If k is larger than the array length or k is less than or equal to 0
    """
    # Validate input
    if k <= 0:
        raise ValueError("Subarray length k must be a positive integer")
    if k > len(arr):
        raise ValueError("Subarray length k cannot be larger than the array length")
    
    # Handle edge case of empty array
    if not arr:
        return 0
    
    # Sliding window approach
    # Calculate initial window sum
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Slide the window and update max_sum
    for i in range(k, len(arr)):
        # Remove the first element of previous window and add the new element
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum