def count_zero_sum_pairs(arr):
    """
    Count the number of pairs of elements in the array that sum up to 0.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: Number of pairs that sum to zero
    
    Raises:
        TypeError: If input is not a list
    """
    # Validate input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    # Use a hash set for efficient counting
    pair_count = 0
    num_counts = {}
    
    # Single pass through the array
    for num in arr:
        # Check if the negative of the current number exists in the previous counts
        if -num in num_counts:
            pair_count += num_counts[-num]
        
        # Increment the count of the current number
        num_counts[num] = num_counts.get(num, 0) + 1
    
    return pair_count