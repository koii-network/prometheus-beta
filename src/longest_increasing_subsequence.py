def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in an array.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: Longest increasing subsequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-comparable elements
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # Dynamic programming approach
    n = len(arr)
    # Stores the length of LIS ending at each index
    dp = [1] * n
    # Stores the previous index in the LIS
    prev = [-1] * n
    
    # Maximum length of LIS and its last index
    max_length = 1
    max_index = 0
    
    # Compute LIS lengths and track predecessors
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        
        # Update max length and index
        if dp[i] > max_length:
            max_length = dp[i]
            max_index = i
    
    # Reconstruct the subsequence
    subsequence = []
    while max_index != -1:
        subsequence.insert(0, arr[max_index])
        max_index = prev[max_index]
    
    return subsequence