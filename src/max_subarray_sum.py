def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a subarray with length k in the given array.

    Args:
        arr (list): Input list of integers
        k (int): Length of the subarray

    Returns:
        int: Maximum sum of a subarray of length k
        
    Raises:
        ValueError: If k is less than or equal to 0
        ValueError: If k is greater than the length of the array
    """
    # Handle empty array case
    if not arr and k == 0:
        return 0
    
    # Validate input parameters
    if k <= 0:
        raise ValueError("Subarray length (k) must be a positive integer")
    
    if k > len(arr):
        raise ValueError("Subarray length cannot be greater than array length")
    
    # Initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Sliding window approach
    for i in range(k, len(arr)):
        # Remove first element of previous window and add new element
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum