def longest_increasing_subsequence_length(nums):
    """
    Find the length of the longest increasing subsequence in a list of numbers.
    
    Args:
        nums (list): A list of numbers to find the longest increasing subsequence length.
    
    Returns:
        int: The length of the longest increasing subsequence.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-numeric elements.
    
    Examples:
        >>> longest_increasing_subsequence_length([10, 9, 2, 5, 3, 7, 101, 18])
        4
        >>> longest_increasing_subsequence_length([])
        0
        >>> longest_increasing_subsequence_length([1, 3, 6, 7, 9, 4, 10, 5, 6])
        6
    """
    # Handle edge cases
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Empty list case
    if not nums:
        return 0
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("List must contain only numeric elements")
    
    # Dynamic Programming solution
    # Time complexity: O(n^2), Space complexity: O(n)
    n = len(nums)
    # dp[i] represents the length of the longest increasing subsequence ending at index i
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)