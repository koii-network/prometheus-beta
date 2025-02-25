def count_zero_sum_pairs(nums):
    """
    Count the number of pairs of elements in the input array that sum up to 0.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The number of pairs that sum to zero.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    # Validate input
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in nums):
        raise ValueError("All elements must be integers")
    
    # Use a hash map to efficiently count zero-sum pairs
    pair_count = 0
    num_freq = {}
    
    for num in nums:
        # Special handling for zero
        if num == 0:
            # If zero is already seen, add to pair count
            pair_count += num_freq.get(0, 0)
            num_freq[0] = num_freq.get(0, 0) + 1
            continue
        
        # Check if the negative of the current number exists in the frequency map
        if -num in num_freq:
            pair_count += num_freq[-num]
        
        # Update the frequency of the current number
        num_freq[num] = num_freq.get(num, 0) + 1
    
    return pair_count