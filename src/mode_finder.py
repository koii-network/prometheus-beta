from typing import List, Union
from collections import Counter

def find_mode(numbers: List[float]) -> Union[float, List[float]]:
    """
    Find the mode (most frequent value) in a list of numbers.
    
    Args:
        numbers (List[float]): A list of numbers to find the mode for.
    
    Returns:
        Union[float, List[float]]: 
        - If there's a single mode, returns that mode
        - If there are multiple modes, returns a list of modes
        - If the list is empty, returns an empty list
        - If all numbers are unique, returns the first number
    
    Raises:
        TypeError: If the input is not a list
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    
    if not numbers:
        return []
    
    # If all numbers are unique, return the first number
    if len(set(numbers)) == len(numbers):
        return numbers[0]
    
    # Count the frequency of each number
    freq_counter = Counter(numbers)
    
    # Find the maximum frequency
    max_freq = max(freq_counter.values())
    
    # Find all numbers with the maximum frequency
    modes = [num for num, count in freq_counter.items() if count == max_freq]
    
    # Return single mode if only one, otherwise return list of modes
    return modes[0] if len(modes) == 1 else modes