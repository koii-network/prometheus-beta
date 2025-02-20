def get_most_frequent_index(nums):
    """
    Find the index of the integer with the highest frequency in the list.
    In case of a tie, return the index of the first occurrence.
    
    Args:
        nums (list): A list of integers
    
    Returns:
        int: The index of the most frequent integer
    
    Raises:
        ValueError: If the input list is empty
    """
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    # Count frequencies and track first occurrences
    freq_dict = {}
    first_occurrence = {}
    
    for i, num in enumerate(nums):
        # Update frequency
        freq_dict[num] = freq_dict.get(num, 0) + 1
        
        # Track first occurrence index if not already set
        if num not in first_occurrence:
            first_occurrence[num] = i
    
    # Find the maximum frequency
    max_freq = max(freq_dict.values())
    
    # Find the first number with max frequency based on first occurrence
    for num, freq in freq_dict.items():
        if freq == max_freq:
            return first_occurrence[num]