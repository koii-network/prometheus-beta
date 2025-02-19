def find_lis_length(nums):
    """
    Find the length of the longest increasing subsequence in a list of numbers.
    
    Args:
        nums (list): A list of integers
    
    Returns:
        int: Length of the longest increasing subsequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Validate input
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not nums:
        return 0
    
    # Validate list contains only numbers
    if not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("List must contain only numeric elements")
    
    # Dynamic Programming solution
    # Time complexity: O(n²), Space complexity: O(n)
    n = len(nums)
    dp = [1] * n  # Each element starts with a subsequence length of 1
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)