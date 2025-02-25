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
    
    # Create a list to store frequency and order information
    freq_order = []
    for i, num in enumerate(numbers):
        freq_order.append((num, freq_counter[num], i))
    
    # Sort based on frequency first, then by original order
    freq_order.sort(key=lambda x: (x[1], x[2]))
    
    # Return the sorted list
    return [x[0] for x in freq_order]