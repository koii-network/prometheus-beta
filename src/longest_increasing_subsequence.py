def find_lis_length(arr):
    """
    Find the length of the longest increasing subsequence in an array.
    
    Args:
        arr (list): An array of integers
    
    Returns:
        int: Length of the longest increasing subsequence
    
    Examples:
        >>> find_lis_length([10, 22, 9, 33, 21, 50, 41, 60, 80])
        6
        >>> find_lis_length([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
        6
        >>> find_lis_length([])
        0
        >>> find_lis_length([5])
        1
    """
    if not arr:
        return 0
    
    # Dynamic programming approach
    n = len(arr)
    # dp[i] will store the length of LIS ending at index i
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)