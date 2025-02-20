def longest_increasing_subsequence(arr, return_subsequence=False):
    """
    Find the longest increasing subsequence in a given array.
    
    Args:
        arr (list): Input list of integers
        return_subsequence (bool, optional): If True, return the subsequence. 
                                             If False, return its length. 
                                             Defaults to False.
    
    Returns:
        int or list: Length of LIS or the actual subsequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list contains non-integer elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Empty list case
    if not arr:
        return [] if return_subsequence else 0
    
    n = len(arr)
    
    # Dynamic Programming approach
    # Length of LIS ending at each index
    dp = [1] * n
    
    # Previous element indices to reconstruct subsequence
    prev = [-1] * n
    
    # Find the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    # Find the maximum length and its index
    max_length = max(dp)
    max_index = dp.index(max_length)
    
    # Reconstruct subsequence if required
    if return_subsequence:
        subsequence = []
        while max_index != -1:
            subsequence.insert(0, arr[max_index])
            max_index = prev[max_index]
        return subsequence
    
    return max_length