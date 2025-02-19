def find_lis_length(nums):
    """
    Find the length of the longest increasing subsequence in a list of numbers.
    
    Args:
        nums (list): A list of numbers
    
    Returns:
        int: Length of the longest increasing subsequence
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Input validation
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    if not nums:
        return 0
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("List must contain only numeric elements")
    
    # Dynamic Programming solution
    n = len(nums)
    # Initialize dp array where dp[i] represents the length of LIS ending at index i
    dp = [1] * n
    
    # Compute LIS lengths
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum LIS length
    return max(dp)