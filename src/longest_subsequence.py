def longest_subsequence_with_target_sum(arr, target):
    """
    Find the length of the longest subsequence with a sum equal to the target.
    
    Args:
        arr (list): Input list of integers
        target (int): Target sum to match
    
    Returns:
        int: Length of the longest subsequence with sum equal to target
             Returns 0 if no such subsequence exists
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    if not arr:
        return 0
    
    n = len(arr)
    max_length = 0
    
    # Iterate through all possible starting points
    for start in range(n):
        current_sum = 0
        
        # Check subsequences starting from this point
        for end in range(start, n):
            current_sum += arr[end]
            
            # If current subsequence sum matches target, update max length
            if current_sum == target:
                max_length = max(max_length, end - start + 1)
            
            # If sum exceeds target, break inner loop
            if current_sum > target:
                break
    
    return max_length