def find_highest_frequency_index(numbers):
    """
    Find the index of the integer with the highest frequency in the list.
    In case of a tie, return the index of the first occurrence.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: The index of the first integer with the highest frequency
    
    Raises:
        ValueError: If the input list is empty
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Count frequencies of each number
    frequency_dict = {}
    for num in numbers:
        if num not in frequency_dict:
            frequency_dict[num] = [numbers.index(num), 1]
        else:
            frequency_dict[num][1] += 1
    
    # Find the maximum frequency
    max_freq = max(freq[1] for freq in frequency_dict.values())
    
    # Find the first occurrence with max frequency
    candidates = [
        (index, num) for num, (index, freq) in frequency_dict.items() 
        if freq == max_freq
    ]
    
    # Return the index of the first occurrence
    return min(candidates, key=lambda x: x[0])[0]