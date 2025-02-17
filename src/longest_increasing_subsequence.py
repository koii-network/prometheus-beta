def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in an array.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: The longest increasing subsequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-comparable elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # Dynamic programming solution
    # dp[i] stores the length of LIS ending at index i
    # prev[i] stores the previous index in the LIS
    n = len(arr)
    dp = [1] * n
    prev = [None] * n
    
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
    
    # Reconstruct the subsequence
    subsequence = []
    while max_index is not None:
        subsequence.insert(0, arr[max_index])
        max_index = prev[max_index]
    
    return subsequence