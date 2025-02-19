def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in the given array.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        tuple: A tuple containing:
            - Length of the longest increasing subsequence (int)
            - The longest increasing subsequence itself (list)
    """
    if not arr:
        return 0, []
    
    # Dynamic Programming approach
    n = len(arr)
    # Store the length of LIS ending at each index
    dp = [1] * n
    # Store the previous index for reconstructing the subsequence
    prev = [-1] * n
    
    # Find the longest increasing subsequence
    max_length = 1
    max_index = 0
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        
        # Track the overall maximum
        if dp[i] > max_length:
            max_length = dp[i]
            max_index = i
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_index
    while current != -1:
        subsequence.insert(0, arr[current])
        current = prev[current]
    
    return max_length, subsequence