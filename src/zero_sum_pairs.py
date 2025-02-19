def count_zero_sum_pairs(nums):
    """
    Count the number of pairs of elements in the input array that sum up to 0.
    
    Args:
        nums (list): A list of integers
    
    Returns:
        int: Number of pairs that sum to 0
    
    Examples:
        >>> count_zero_sum_pairs([1, -1, 2, -2, 3])
        2
        >>> count_zero_sum_pairs([])
        0
        >>> count_zero_sum_pairs([0, 0, 0])
        3
    """
    # Handle edge cases
    if not nums:
        return 0
    
    # Use a hash map to track counts efficiently
    num_counts = {}
    zero_sum_pairs = 0
    
    for num in nums:
        # Check if the complement exists
        complement = -num
        if complement in num_counts:
            zero_sum_pairs += num_counts[complement]
        
        # Update the count of the current number
        num_counts[num] = num_counts.get(num, 0) + 1
    
    return zero_sum_pairs