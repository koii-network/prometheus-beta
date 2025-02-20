def longest_increasing_subsequence(arr):
    """
    Compute the length of the longest increasing subsequence in an array of integers.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: Length of the longest increasing subsequence
    
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    # Handle empty array case
    if not arr:
        return 0
    
    # Initialize DP array where each element is initially 1 
    # (minimum length subsequence is the element itself)
    n = len(arr)
    dp = [1] * n
    
    # Compute longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum length found
    return max(dp)