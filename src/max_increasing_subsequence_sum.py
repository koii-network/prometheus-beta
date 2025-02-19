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
    
    # Initialize tracking arrays
    dp = [0] * len(arr)
    dp[0] = arr[0]
    
    # Best subsequence sums for each length
    sums = [arr[0]]
    
    for i in range(1, len(arr)):
        # Find where this element could be inserted
        left, right = 0, len(sums)
        while left < right:
            mid = (left + right) // 2
            if sums[mid] < arr[i]:
                left = mid + 1
            else:
                right = mid
        
        # Compute the maximum sum for this position
        if left == 0:
            # Start a new subsequence
            dp[i] = arr[i]
            if arr[i] > sums[0]:
                sums.append(arr[i])
            else:
                sums[0] = arr[i]
        else:
            # Extend a previous subsequence
            dp[i] = sums[left-1] + arr[i]
            
            # Update subsequence sums
            if left == len(sums):
                sums.append(dp[i])
            else:
                sums[left] = max(sums[left], dp[i])
    
    return max(dp)