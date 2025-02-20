def sum_subarrays(arr, k):
    """
    Calculate the sum of all subarrays with length less than or equal to k.
    
    Args:
    arr (list): A sorted list of integers
    k (int): Maximum subarray length
    
    Returns:
    int: Sum of all subarrays with length <= k
    
    Raises:
    ValueError: If k is less than 1 or arr is None
    """
    # Input validation
    if k < 1:
        raise ValueError("k must be at least 1")
    
    if arr is None:
        raise ValueError("Input array cannot be None")
    
    total_sum = 0
    n = len(arr)
    
    # Iterate through all possible starting positions
    for start in range(n):
        # Consider subarrays of lengths from 1 to min(k, n-start)
        subarray_sum = 0
        for length in range(1, min(k, n-start) + 1):
            subarray_sum += arr[start + length - 1]
            # Sum the cumulative subarrays for each length
            total_sum += subarray_sum * (n - start - length + 1)
    
    return total_sum