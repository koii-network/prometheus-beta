def find_most_frequent_index(nums):
    """
    Find the index of the integer with the highest frequency in the list.
    If multiple integers have the same highest frequency, return the index
    of the first such integer.
    
    Args:
        nums (list): A list of integers
    
    Returns:
        int: The index of the most frequent integer
    
    Raises:
        ValueError: If the input list is empty
    """
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    # Count frequencies of each number
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    
    # Find the maximum frequency
    max_freq = max(freq_dict.values())
    
    # Find the first index of the most frequent number
    for i, num in enumerate(nums):
        if freq_dict[num] == max_freq:
            return i