def longest_increasing_subsequence(arr):
    """
    Calculate the length of the longest increasing subsequence in an array.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        int: Length of the longest increasing subsequence.
    
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    # Handle empty array case
    if not arr:
        return 0
    
    # Initialize dp array where each element starts with a subsequence of length 1
    dp = [1] * len(arr)
    
    # Compute longest increasing subsequence
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum length found
    return max(dp)