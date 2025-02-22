def maxSumSubarray(arr, k):
    """
    Find the maximum sum of a non-overlapping subarray with length k.
    
    Args:
        arr (list): Input array of numbers
        k (int): Length of the subarray
    
    Returns:
        int: Maximum sum of a non-overlapping subarray of length k
    
    Raises:
        ValueError: If k is greater than the length of the array or k <= 0
    """
    # Validate input
    if k <= 0:
        raise ValueError("Subarray length (k) must be a positive integer")
    
    if k > len(arr):
        raise ValueError("Subarray length (k) cannot be greater than array length")
    
    # Track the maximum sum of non-overlapping subarrays
    max_sum = float('-inf')
    
    # Iterate through the array, ensuring non-overlapping subarrays
    for i in range(0, len(arr) - k + 1, k):
        current_sum = sum(arr[i:i+k])
        max_sum = max(max_sum, current_sum)
    
    return max_sum