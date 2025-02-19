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
    
    # Individual max sums with their ending element and length
    # Format: (max sum, max sum's length)
    dp = [(arr[0], 1)]
    max_total_sum = arr[0]
    
    for i in range(1, len(arr)):
        # Find the maximum previous subsequence this can extend
        best_prev_sum = 0
        best_prev_length = 0
        
        # Binary search to find best previous subsequence to extend
        left, right = 0, len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid][1] < arr[i]:
                best_prev_sum = max(best_prev_sum, dp[mid][0])
                best_prev_length = max(best_prev_length, dp[mid][1])
                left = mid + 1
            else:
                right = mid
        
        # Compute current subsequence sum
        current_sum = best_prev_sum + arr[i]
        current_length = best_prev_length + 1
        
        # Maintain sorted order of subsequence sums
        idx = binary_search_index(dp, current_length)
        
        # 3 cases of insertion
        if idx == len(dp):
            # Append new subsequence
            dp.append((current_sum, current_length))
        elif current_sum > dp[idx][0]:
            # Replace existing subsequence
            dp[idx] = (current_sum, current_length)
        
        # Update maximum total sum
        max_total_sum = max(max_total_sum, current_sum)
    
    return max_total_sum

def binary_search_index(dp, length):
    """
    Find the index to insert/replace a subsequence with a given length.
    
    Args:
        dp (list): List of (sum, length) tuples
        length (int): Target subsequence length
    
    Returns:
        int: Insertion/replacement index
    """
    left, right = 0, len(dp)
    while left < right:
        mid = (left + right) // 2
        if dp[mid][1] < length:
            left = mid + 1
        else:
            right = mid
    return left