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
    
    # For each possible start index
    for start in range(n):
        # Generate all subarrays starting from this index with length <= k
        subarray_sum = 0
        for length in range(1, k + 1):
            if start + length > n:
                break
            
            # Sum the subarray
            subarray_sum += sum(arr[start:start+length])
            total_sum += subarray_sum
    
    return total_sum