def longest_subsequence_with_target_sum(arr, target):
    """
    Find the length of the longest subsequence in an array where the sum of its elements 
    is equal to the target integer.
    
    Args:
        arr (list): Input list of integers
        target (int): Target sum to find
    
    Returns:
        int: Length of the longest subsequence with sum equal to target
    """
    # Handle edge cases
    if not arr:
        return 0
    
    # Use dynamic programming to solve the problem
    # Key: cumulative sum, Value: minimum index to achieve that sum
    sum_index_map = {0: -1}
    current_sum = 0
    max_length = 0
    
    for i, num in enumerate(arr):
        current_sum += num
        
        # Check if we can find a subsequence with target sum
        if current_sum - target in sum_index_map:
            max_length = max(max_length, i - sum_index_map[current_sum - target])
        
        # Only add to map if this index is not already present for the sum
        if current_sum not in sum_index_map:
            sum_index_map[current_sum] = i
    
    return max_length