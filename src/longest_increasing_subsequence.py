def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in a given array of integers.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        list: The longest increasing subsequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Length of the input array
    n = len(arr)
    
    # Dynamic programming approach
    # dp[i] stores the length of the LIS ending at index i
    dp = [1] * n
    
    # Stores the previous index to reconstruct the subsequence
    prev = [-1] * n
    
    # Find the length of LIS and track the longest subsequence
    max_length = 1
    max_index = 0
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        
        # Update max_length and max_index if current subsequence is longer
        if dp[i] > max_length:
            max_length = dp[i]
            max_index = i
    
    # Reconstruct the subsequence
    subsequence = []
    while max_index != -1:
        subsequence.insert(0, arr[max_index])
        max_index = prev[max_index]
    
    return subsequence