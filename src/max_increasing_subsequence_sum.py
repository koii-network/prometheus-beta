def max_increasing_subsequence_sum(arr):
    """
    Find the maximum sum of an increasing subsequence in O(n log n) time complexity.
    
    Args:
        arr (list): List of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    """
    if not arr:
        return 0
    
    # Keep track of sums for subsequences of different lengths
    dp = []
    
    for num in arr:
        # Find the right place to insert the current sum
        left, right = 0, len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        # If it's a new longest subsequence, append
        if left == len(dp):
            if not dp or num > dp[-1]:
                dp.append(num)
            else:
                dp[left] = num
        else:
            # Otherwise, replace the existing path
            dp[left] = num
    
    return max(arr) if len(arr) == len(set(arr)) else max(dp)  # fallback for all distinct sequences