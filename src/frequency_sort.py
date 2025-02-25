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
    
    # Create a list to store unique elements sorted by frequency
    unique_sorted = sorted(set(numbers), key=lambda x: freq_counter[x])
    
    # Reconstruct the list maintaining the original order within frequency groups
    result = []
    for num in unique_sorted:
        # Add all occurrences of the current number
        result.extend([n for n in numbers if n == num])
    
    return result