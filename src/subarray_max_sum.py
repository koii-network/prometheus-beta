def maxSumSubarray(arr, k):
    """
    Find the maximum sum of a non-overlapping subarray with a given length k.
    
    Args:
        arr (list): Input list of numbers
        k (int): Length of the non-overlapping subarray
    
    Returns:
        int: Maximum sum of a non-overlapping subarray of length k
    
    Raises:
        ValueError: If k is invalid (less than or equal to 0, or larger than array length)
    """
    # Input validation
    if k <= 0:
        raise ValueError("Subarray length k must be a positive integer")
    
    if k > len(arr):
        raise ValueError("Subarray length k cannot be larger than the input array")
    
    # If k is equal to the array length, return the sum of the entire array
    if k == len(arr):
        return sum(arr)
    
    # Use sliding window technique
    max_sum = float('-inf')
    
    # Calculate the initial window sum
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    # Slide the window through the array
    for i in range(1, len(arr) - k + 1):
        # Adjust the sum by removing the first element of the previous window
        # and adding the last element of the new window
        current_sum = current_sum - arr[i-1] + arr[i+k-1]
        
        # Update max_sum if current sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum