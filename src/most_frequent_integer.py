def find_most_frequent_integer_index(numbers):
    """
    Find the index of the integer with the highest frequency in the list.
    
    Args:
        numbers (list): A list of integers to analyze.
    
    Returns:
        int: The index of the first occurrence of the most frequent integer.
        
    Raises:
        ValueError: If the input list is empty.
    
    Examples:
        >>> find_most_frequent_integer_index([1, 2, 2, 3, 3, 3])
        4
        >>> find_most_frequent_integer_index([1, 1, 2, 2])
        0
    """
    # Check for empty list
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Create a frequency dictionary to track occurrences
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Find the maximum frequency
    max_freq = max(frequency.values())
    
    # Find the last (highest) index of the most frequent number
    for i in range(len(numbers) - 1, -1, -1):
        if frequency[numbers[i]] == max_freq:
            return i