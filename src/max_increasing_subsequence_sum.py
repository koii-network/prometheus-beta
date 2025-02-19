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
    
    # Initialize an array to store the maximum sum up to each index
    dp = [0] * len(arr)
    dp[0] = arr[0]
    
    # Use a list to track the maximum sums with their corresponding lengths 
    max_sums = [(arr[0], 1)]
    
    for i in range(1, len(arr)):
        # Binary search to find the correct position to insert current element
        left, right = 0, len(max_sums)
        while left < right:
            mid = (left + right) // 2
            if max_sums[mid][1] < arr[i]:
                left = mid + 1
            else:
                right = mid
        
        # Calculate the maximum sum for current element
        if left == 0:
            # Starting a new subsequence
            dp[i] = arr[i]
            max_sums.insert(0, (arr[i], arr[i]))
        else:
            # Extending an existing subsequence
            dp[i] = max_sums[left-1][0] + arr[i]
            max_sums.insert(left, (dp[i], arr[i]))
    
    return max(dp)