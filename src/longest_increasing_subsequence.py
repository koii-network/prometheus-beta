def longest_increasing_subsequence_length(arr):
    """
    Compute the length of the longest increasing subsequence in an array of integers.
    
    Args:
        arr (list): A list of integers to find the longest increasing subsequence in.
    
    Returns:
        int: The length of the longest increasing subsequence.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains non-numeric elements.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Examples:
        >>> longest_increasing_subsequence_length([10, 22, 9, 33, 21, 50, 41, 60])
        5
        >>> longest_increasing_subsequence_length([])
        0
        >>> longest_increasing_subsequence_length([5])
        1
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return 0
    
    # Validate all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements must be numeric")
    
    # Dynamic Programming approach
    # Initialize dp array where dp[i] stores the length of LIS ending at index i
    n = len(arr)
    dp = [1] * n
    
    # Compute LIS lengths
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum LIS length
    return max(dp)