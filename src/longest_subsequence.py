def longest_subsequence_with_sum(arr, target):
    """
    Returns the length of the longest subsequence in the array 
    where the sum of its elements equals the target.
    
    Args:
        arr (list): Input list of integers
        target (int): Target sum to find
    
    Returns:
        int: Length of the longest subsequence with sum equal to target
    """
    # Handle edge cases
    if not arr:
        return 0
    
    # Dictionary to store the minimum index for a given cumulative sum
    sum_index_map = {0: -1}
    
    current_sum = 0
    max_length = 0
    
    for i, num in enumerate(arr):
        current_sum += num
        
        # Check if current_sum - target exists in map
        if current_sum - target in sum_index_map:
            max_length = max(max_length, i - sum_index_map[current_sum - target])
        
        # Only update sum_index_map if this sum is not already in map
        # This ensures we keep the earliest index
        if current_sum not in sum_index_map:
            sum_index_map[current_sum] = i
    
    return max_length