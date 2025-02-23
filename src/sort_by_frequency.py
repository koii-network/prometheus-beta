from collections import Counter

def sort_by_frequency(numbers):
    """
    Sort a list of integers based on their frequency, with less frequent 
    elements appearing first and more frequent elements appearing later.
    
    Args:
        numbers (list): A list of integers to be sorted
    
    Returns:
        list: A new list sorted by frequency (ascending), with original elements
    """
    if not numbers:
        return []
    
    # Count the frequency of each number
    freq_counter = Counter(numbers)
    
    # Sort the list based on frequency (ascending) and then by the number itself
    return sorted(numbers, key=lambda x: (freq_counter[x], x))