from typing import List
from collections import Counter

def sort_by_frequency(numbers: List[int]) -> List[int]:
    """
    Sort a list of integers based on their frequency, 
    with less frequent elements appearing first,
    preserving the original order of elements.
    
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
    
    # Create a list of (frequency, original index, element) tuples
    freq_order = []
    for i, num in enumerate(numbers):
        freq_order.append((freq_counter[num], i, num))
    
    # Sort based on frequency (ascending) and then original index
    freq_order.sort()
    
    # Return the sorted elements, preserving their relative order
    return [x[2] for x in freq_order]