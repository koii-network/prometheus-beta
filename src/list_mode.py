from collections import Counter
from typing import List, Union

def find_mode(numbers: List[float]) -> Union[float, List[float]]:
    """
    Find the mode (most frequent value) in a list of numbers.
    
    Args:
        numbers (List[float]): A list of numbers to find the mode for.
    
    Returns:
        Union[float, List[float]]: The mode of the list. 
        If multiple modes exist, returns a list of modes.
        If the list is empty, returns None.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    
    # Handle empty list
    if not numbers:
        return None
    
    # Count occurrences of each number
    count = Counter(numbers)
    
    # Find the maximum frequency
    max_freq = max(count.values())
    
    # Find all numbers with the maximum frequency
    modes = [num for num, freq in count.items() if freq == max_freq]
    
    # Return single mode or list of modes
    return modes[0] if len(modes) == 1 else modes