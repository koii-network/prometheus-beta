def sum_subarrays(arr, k):
    """
    Calculate the sum of all elements in subarrays with length less than or equal to k.
    
    Args:
        arr (list): A sorted list of integers
        k (int): Maximum subarray length
    
    Returns:
        int: Sum of all elements in subarrays of length <= k
    """
    if not arr or k <= 0:
        return 0
    
    total_sum = 0
    n = len(arr)
    
    # Go through each possible subarray start
    for start in range(n):
        # Sum of current subarray
        current_sum = 0
        
        # For each possible length
        for length in range(1, k + 1):
            # Check if current subarray exceeds array bounds
            if start + length > n:
                break
            
            # Add next element to current subarray
            current_sum += arr[start + length - 1]
            
            # Accumulate the sum of this complete current subarray multiple times
            total_sum += current_sum * (min(length, k) + 1)
    
    return total_sum