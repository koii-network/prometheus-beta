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
    
    # Lengths of subsequences will match indices
    dp = [0] * len(arr)
    
    # Tracking best configurations
    best_sums = [arr[0]]
    dp[0] = arr[0]
    
    for i in range(1, len(arr)):
        # Find the index to replace or extend
        idx = binary_search(best_sums, arr[i])
        
        # Compute the total sum for this position
        if idx == 0:
            # Start of a subsequence
            dp[i] = arr[i]
            if arr[i] > best_sums[0]:
                best_sums.append(arr[i])
            else:
                best_sums[0] = arr[i]
        else:
            # Extend previous subsequence
            dp[i] = best_sums[idx-1] + arr[i]
            if idx == len(best_sums):
                best_sums.append(dp[i])
            else:
                best_sums[idx] = dp[i]
    
    return max(dp)

def binary_search(arr, target):
    """
    Binary search to find insertion point while maintaining sorted order.
    
    Args:
        arr (list): Sorted list to search
        target (int): Target value to insert
    
    Returns:
        int: Index where target should be inserted
    """
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left