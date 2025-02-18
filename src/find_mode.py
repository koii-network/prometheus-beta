from typing import List, Union
from collections import Counter

def find_mode(numbers: List[float]) -> Union[float, List[float]]:
    """
    Find the mode (most frequent value) in a list of numbers.
    
    Args:
        numbers (List[float]): A list of numbers to find the mode for.
    
    Returns:
        Union[float, List[float]]: 
        - If there's a single mode, returns that number
        - If multiple numbers have the same highest frequency, returns a list of those numbers
        - Returns an empty list if the input list is empty
    
    Raises:
        TypeError: If the input is not a list
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    
    # Handle empty list
    if not numbers:
        return []
    
    # Count frequencies of numbers
    freq_counter = Counter(numbers)
    
    # Find the maximum frequency
    max_freq = max(freq_counter.values())
    
    # Find all numbers with the maximum frequency
    modes = [num for num, count in freq_counter.items() if count == max_freq]
    
    # Return single mode or list of modes
    return modes[0] if len(modes) == 1 else modes