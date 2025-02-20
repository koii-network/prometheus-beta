def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a subarray with length k in the given array.
    
    Args:
        arr (list): Input list of integers
        k (int): Length of the subarray
    
    Returns:
        int: Maximum sum of a subarray of length k
    
    Raises:
        ValueError: If k is invalid (less than or equal to 0 or greater than array length)
    """
    # Validate input
    if k <= 0:
        raise ValueError("Subarray length k must be a positive integer")
    if k > len(arr):
        raise ValueError("Subarray length k cannot be greater than array length")
    
    # If array is empty or k is 0, return 0
    if not arr or k == 0:
        return 0
    
    # Use sliding window technique
    # First, compute the sum of the first k elements
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Slide the window through the rest of the array
    for i in range(k, len(arr)):
        # Remove the first element of previous window and add the next element
        current_sum = current_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum