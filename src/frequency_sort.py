from typing import List
from collections import Counter

def sort_by_frequency(numbers: List[int]) -> List[int]:
    """
    Sort a list of integers based on their frequency, 
    with less frequent elements appearing first.
    
    Args:
        numbers (List[int]): Input list of integers to be sorted
    
    Returns:
        List[int]: Sorted list based on element frequency 
                   (less frequent elements first)
    
    Examples:
        >>> sort_by_frequency([1, 1, 2, 2, 2, 3])
        [3, 1, 1, 2, 2, 2]
        >>> sort_by_frequency([])
        []
    """
    # Handle empty list case
    if not numbers:
        return []
    
    # Count frequency of each number
    freq_counter = Counter(numbers)
    
    # Create a custom sorting key that preserves original order for same frequency
    def custom_key(x):
        # This will sort first by frequency, then by original index
        return (freq_counter[x], numbers.index(x))
    
    # Sort the list preserving original order for equal frequencies
    return sorted(numbers, key=custom_key)