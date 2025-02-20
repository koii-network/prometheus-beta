def max_subarray_sum(arr, k):
    """
    Calculate the maximum sum of a contiguous subarray with length k.
    
    Args:
        arr (list): A list of integers
        k (int): The length of the subarray
    
    Returns:
        int: The maximum sum of a contiguous subarray of length k
    
    Raises:
        ValueError: If k is larger than the array length or k is less than 1
    """
    # Input validation
    if k < 1:
        raise ValueError("Subarray length (k) must be at least 1")
    
    if k > len(arr):
        raise ValueError("Subarray length (k) cannot be larger than array length")
    
    # If the array is empty or k is 0, return 0
    if not arr or k == 0:
        return 0
    
    # Initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Sliding window approach
    for i in range(k, len(arr)):
        # Remove the first element of the previous window
        # Add the next element to create the new window
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum