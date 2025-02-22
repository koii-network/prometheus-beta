def longest_subsequence_with_target_sum(arr, target):
    """
    Find the length of the longest subsequence where the sum of elements equals the target.
    
    Args:
        arr (list): Input list of integers
        target (int): Target sum to find
    
    Returns:
        int: Length of the longest subsequence with sum equal to target
    """
    if not arr:
        return 0
    
    # Dictionary to store max subsequence length for a given cumulative sum
    dp = {0: 0}
    current_sum = 0
    max_length = 0
    
    for num in arr:
        current_sum += num
        
        # If current_sum - target exists in dp, update max_length
        if current_sum - target in dp:
            max_length = max(max_length, current_sum - dp[current_sum - target])
        
        # Store the earliest occurrence of current_sum
        if current_sum not in dp:
            dp[current_sum] = current_sum
    
    return max_length