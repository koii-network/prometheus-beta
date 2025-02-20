def longest_increasing_subsequence(arr):
    """
    Compute the length of the longest increasing subsequence in an array of integers.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: Length of the longest increasing subsequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-integer elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Handle empty list case
    if not arr:
        return 0
    
    # Dynamic programming solution
    # dp[i] represents the length of LIS ending at index i
    dp = [1] * len(arr)
    
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)