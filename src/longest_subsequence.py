def longest_subsequence_with_target_sum(arr, target):
    """
    Find the length of the longest subsequence with a sum equal to the target.
    
    Args:
        arr (list): Input list of integers
        target (int): Target sum to match
    
    Returns:
        int: Length of the longest subsequence with sum equal to target
             Returns 0 if no such subsequence exists
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not arr:
        return 0
    
    # Use a prefix sum approach with a dictionary
    # Key: cumulative sum, Value: earliest index
    sum_index = {0: -1}
    current_sum = 0
    max_length = 0
    
    for i, num in enumerate(arr):
        current_sum += num
        
        # Check if current prefix sum - target exists in previous sums
        if current_sum - target in sum_index:
            # Update max length
            max_length = max(max_length, i - sum_index[current_sum - target])
        
        # Only add the first occurrence of a cumulative sum
        if current_sum not in sum_index:
            sum_index[current_sum] = i
    
    return max_length