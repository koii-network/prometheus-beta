def maxSumSubarray(arr, k):
    """
    Find the maximum sum of a non-overlapping subarray with length k.
    
    Args:
        arr (list): Input array of numbers
        k (int): Length of the subarray
    
    Returns:
        int: Maximum sum of a non-overlapping subarray of length k
    
    Raises:
        ValueError: If k is larger than the array length or k is less than or equal to 0
    """
    # Validate input
    if k <= 0:
        raise ValueError("Subarray length k must be a positive integer")
    
    if k > len(arr):
        raise ValueError("Subarray length k cannot be larger than the array length")
    
    # Return None if no valid subarray can be found
    if len(arr) == 0:
        return None
    
    # Track maximum sum
    max_sum = float('-inf')
    
    # Iterate through the array to find non-overlapping subarrays
    for i in range(len(arr) - k + 1):
        current_sum = sum(arr[i:i+k])
        max_sum = max(max_sum, current_sum)
    
    return max_sum