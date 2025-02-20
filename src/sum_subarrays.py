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
    
    # Generate all possible subarrays of length <= k
    for start in range(n):
        current_sum = 0
        for end in range(start, min(start + k, n)):
            current_sum += arr[end]
            total_sum += current_sum
    
    return total_sum