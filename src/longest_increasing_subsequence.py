def longest_increasing_subsequence(arr):
    """
    Calculate the length of the longest increasing subsequence in the given array.
    
    A subsequence is a sequence that can be derived from an array by deleting some 
    or no elements without changing the order of the remaining elements.
    
    Args:
        arr (list): An input list of integers
    
    Returns:
        int: Length of the longest increasing subsequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-integer elements
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Examples:
        >>> longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
        4
        >>> longest_increasing_subsequence([0, 1, 0, 3, 2, 3])
        4
        >>> longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7])
        1
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return 0
    
    # Validate that all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Dynamic programming solution
    n = len(arr)
    # dp[i] stores the length of the longest increasing subsequence ending at index i
    dp = [1] * n
    
    # Compute longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum length
    return max(dp)