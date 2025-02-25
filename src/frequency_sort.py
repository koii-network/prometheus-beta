from collections import Counter
from typing import List

def sort_by_frequency(numbers: List[int]) -> List[int]:
    """
    Sort a list of integers based on their frequency, with less frequent 
    elements appearing first and more frequent elements appearing later.
    
    Args:
        numbers (List[int]): Input list of integers to be sorted
    
    Returns:
        List[int]: Sorted list based on frequency (ascending)
    
    Examples:
        >>> sort_by_frequency([1, 1, 2, 2, 2, 3])
        [3, 1, 1, 2, 2, 2]
        >>> sort_by_frequency([])
        []
        >>> sort_by_frequency([5, 5, 4, 4, 4, 3, 3, 3, 3])
        [5, 5, 4, 4, 4, 3, 3, 3, 3]
    """
    # Handle empty list case
    if not numbers:
        return []
    
    # Count frequency of each number
    freq_count = Counter(numbers)
    
    # Create a list of indices to preserve original order for stable sorting
    indices = list(range(len(numbers)))
    
    # Sort based on frequency (ascending) and then original order
    sorted_indices = sorted(indices, key=lambda i: (freq_count[numbers[i]], i))
    
    return [numbers[i] for i in sorted_indices]