def max_subarray_sum(arr, k):
    """
    Find the maximum sum of a subarray of length k in the given list.
    
    Args:
        arr (list): Input list of integers
        k (int): Length of the subarray to find maximum sum
    
    Returns:
        list: Subarray with maximum sum, or empty list if k > len(arr)
    
    Raises:
        TypeError: If input is not a list or k is not an integer
        ValueError: If k is negative
    """
    # Validate inputs
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    if k < 0:
        raise ValueError("k cannot be negative")
    
    # If k is larger than the list length, return empty list
    if k > len(arr):
        return []
    
    # If k is 0, return empty list
    if k == 0:
        return []
    
    # Sliding window approach to find maximum sum subarray
    max_sum = float('-inf')
    max_subarray = []
    
    for i in range(len(arr) - k + 1):
        current_sum = sum(arr[i:i+k])
        if current_sum > max_sum:
            max_sum = current_sum
            max_subarray = arr[i:i+k]
    
    return max_subarray