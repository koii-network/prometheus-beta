def longest_increasing_subsequence(arr):
    """
    Find the length of the longest increasing subsequence in an array.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: Length of the longest increasing subsequence
    
    Examples:
        - [10, 22, 9, 33, 21, 50, 41, 60] -> 5 ([10, 22, 33, 50, 60])
        - [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15] -> 6
    """
    if not arr:
        return 0
    
    n = len(arr)
    # Initialize DP array with 1 (each element is a subsequence of length 1)
    dp = [1] * n
    
    # Dynamic programming to find longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)