from collections import Counter

def sort_by_frequency(numbers):
    """
    Sort a list of integers based on their frequency.
    Less frequent elements appear first, more frequent elements appear later.
    If multiple elements have the same frequency, maintain their relative order.
    
    Args:
        numbers (list): A list of integers to be sorted
    
    Returns:
        list: Sorted list of integers based on their frequency
    """
    # Count the frequency of each number
    freq_counter = Counter(numbers)
    
    # Sort the list based on frequency (ascending) and original order
    return sorted(numbers, key=lambda x: (freq_counter[x], numbers.index(x)))