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
    
    # Create a list of unique frequencies in ascending order
    sorted_frequencies = sorted(set(freq_counter.values()))
    
    # Create the result list
    result = []
    
    # For each unique frequency, add numbers with that frequency
    for freq in sorted_frequencies:
        # Find all numbers with this frequency
        current_nums = [num for num in numbers if freq_counter[num] == freq]
        
        # Add these numbers to the result, preserving their original order
        for num in numbers:
            if num in current_nums:
                result.append(num)
                # Remove to handle duplicates
                current_nums.remove(num)
    
    return result