def sum_subarrays(arr, k):
    """
    Calculate the sum of all elements in subarrays of arr with length <= k.
    
    Args:
        arr (list): A sorted list of integers
        k (int): Maximum length of subarrays to consider
    
    Returns:
        int: Sum of all elements in valid subarrays
    
    Raises:
        ValueError: If k is negative
        TypeError: If arr is not a list or k is not an integer
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input arr must be a list")
    if not isinstance(k, int):
        raise TypeError("Input k must be an integer")
    
    # Value checking
    if k < 0:
        raise ValueError("k must be a non-negative integer")
    
    # If k is 0, return 0
    if k == 0:
        return 0
    
    total_sum = 0
    n = len(arr)
    
    # Generate all possible subarrays and sum those with length <= k
    for start in range(n):
        current_sum = 0
        for end in range(start, min(start + k, n)):
            current_sum += arr[end]
            total_sum += current_sum
    
    return total_sum