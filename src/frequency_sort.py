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
    
    # Group numbers by their frequency
    freq_groups = {}
    for num in numbers:
        freq = freq_counter[num]
        if freq not in freq_groups:
            freq_groups[freq] = []
        if num not in freq_groups[freq]:
            freq_groups[freq].append(num)
    
    # Sort frequencies in ascending order
    sorted_freqs = sorted(freq_groups.keys())
    
    # Reconstruct the result list
    result = []
    for freq in sorted_freqs:
        for num in freq_groups[freq]:
            # Add all occurrences of this number in original order
            result.extend([x for x in numbers if x == num])
    
    return result