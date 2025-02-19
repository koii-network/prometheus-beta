def maxSumSubarray(arr, k):
    """
    Find the maximum sum of a non-overlapping subarray with length k.
    
    Args:
        arr (list): Input array of numbers
        k (int): Length of the subarray
    
    Returns:
        int: Maximum sum of a non-overlapping subarray of length k
    
    Raises:
        ValueError: If k is larger than the array length or k is non-positive
    """
    # Input validation
    if k <= 0:
        raise ValueError("Subarray length must be a positive integer")
    
    if k > len(arr):
        raise ValueError("Subarray length cannot be larger than the array length")
    
    # Track the overall maximum
    max_sum = float('-inf')
    
    # Try all possible combinations of non-overlapping subarrays
    n = len(arr)
    for start in range(n - k + 1):
        current_sum = sum(arr[start:start+k])
        max_sum = max(max_sum, current_sum)
    
    return max_sum