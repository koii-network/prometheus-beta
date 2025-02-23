from typing import List, Union
from collections import Counter

def find_mode(numbers: List[Union[int, float]]) -> Union[int, float, List[Union[int, float]]]:
    """
    Find the mode (most frequent value) in a list of numbers.
    
    Args:
        numbers (List[Union[int, float]]): A list of numbers to find the mode for.
    
    Returns:
        Union[int, float, List[Union[int, float]]]: 
        - The single mode if there's only one
        - List of modes if multiple numbers have the same highest frequency
        - Raises ValueError for empty input list
    
    Raises:
        ValueError: If the input list is empty
    """
    # Check for empty input
    if not numbers:
        raise ValueError("Cannot find mode of an empty list")
    
    # Use Counter to count occurrences of each number
    frequency = Counter(numbers)
    
    # Find the maximum frequency
    max_freq = max(frequency.values())
    
    # Find all numbers with the maximum frequency
    modes = [num for num, count in frequency.items() if count == max_freq]
    
    # Return single mode if only one, otherwise return list of modes
    return modes[0] if len(modes) == 1 else modes