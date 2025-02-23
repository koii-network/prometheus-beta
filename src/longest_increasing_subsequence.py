def longest_increasing_subsequence(arr, return_sequence=False):
    """
    Find the longest increasing subsequence in a given array.
    
    Args:
        arr (list): Input list of integers
        return_sequence (bool, optional): If True, return the actual subsequence. 
                                          If False, return the length. Defaults to False.
    
    Returns:
        int or list: Length of LIS or the actual subsequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list is empty
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Length of the input array
    n = len(arr)
    
    # Dynamic programming approach
    # dp stores the length of LIS ending at each index
    dp = [1] * n
    
    # Tracking the previous index for reconstructing the subsequence
    prev = [-1] * n
    
    # Find the longest increasing subsequence
    max_length = 1
    max_index = 0
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        
        # Update max length and index
        if dp[i] > max_length:
            max_length = dp[i]
            max_index = i
    
    # If only length is required
    if not return_sequence:
        return max_length
    
    # Reconstruct the subsequence
    subsequence = []
    while max_index != -1:
        subsequence.append(arr[max_index])
        max_index = prev[max_index]
    
    # Reverse to get correct order
    return list(reversed(subsequence))