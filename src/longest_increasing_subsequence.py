def find_lis_length(arr):
    """
    Compute the length of the longest increasing subsequence in an array of integers.
    
    Args:
        arr (list): A list of integers to find the longest increasing subsequence in.
    
    Returns:
        int: The length of the longest increasing subsequence.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
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
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return 0
    
    # Validate all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Dynamic programming solution
    n = len(arr)
    # dp[i] stores the length of the longest increasing subsequence 
    # that ends with arr[i]
    dp = [1] * n
    
    # Compute optimal solution
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum length
    return max(dp)