def maxSumSubarray(arr, k):
    """
    Find the maximum sum of a non-overlapping subarray with length k.
    
    Args:
        arr (list): Input list of numbers
        k (int): Length of the subarray
    
    Returns:
        int: Maximum sum of a non-overlapping subarray of length k
    
    Raises:
        ValueError: If k is invalid or larger than the array length
    """
    # Validate input
    if k <= 0:
        raise ValueError("Subarray length k must be a positive integer")
    
    if k > len(arr):
        raise ValueError("Subarray length k cannot be larger than the array length")
    
    # Initialize max sum to the first possible subarray
    max_sum = sum(arr[:k])
    
    # Iterate through possible non-overlapping subarrays
    for start in range(k, len(arr), k):
        # Stop if not enough elements remain for a full subarray
        if start + k > len(arr):
            break
        
        # Calculate current subarray sum
        current_sum = sum(arr[start:start+k])
        
        # Update max sum if current sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum