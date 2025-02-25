def longest_increasing_subsequence(arr):
    """
    Calculate the length of the longest increasing subsequence in the given array.
    
    A subsequence is a sequence that can be derived from an array by deleting some 
    or no elements without changing the order of the remaining elements.
    
    Args:
        arr (list): A list of integers to find the longest increasing subsequence in.
    
    Returns:
        int: The length of the longest increasing subsequence.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-numeric elements.
    
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
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return 0
    
    # Validate that all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements must be numeric")
    
    # Dynamic programming solution
    # dp[i] represents the length of the longest increasing subsequence 
    # that ends with arr[i]
    dp = [1] * len(arr)
    
    # Compute longest increasing subsequence
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum length found
    return max(dp)