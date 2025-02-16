from typing import List, Union
from collections import Counter

def find_mode(numbers: List[Union[int, float]]) -> Union[int, float, List[Union[int, float]]]:
    """
    Find the mode (most frequent value) in a list of numbers.
    
    Args:
        numbers (List[Union[int, float]]): A list of numbers to find the mode for.
    
    Returns:
        Union[int, float, List[Union[int, float]]]: 
        - The mode if there's a single most frequent value
        - A list of modes if multiple values have the same highest frequency
        - A single value from the list if all values have equal frequency
        - Raises ValueError if the input list is empty
    
    Raises:
        ValueError: If the input list is empty
    """
    if not numbers:
        raise ValueError("Cannot find mode of an empty list")
    
    # Convert to floats to handle mixed type inputs
    numbers = [float(num) for num in numbers]
    
    # Count occurrences of each number
    counts = Counter(numbers)
    
    # Find the maximum frequency
    max_freq = max(counts.values())
    
    # Find all numbers with the maximum frequency
    modes = [num for num, freq in counts.items() if freq == max_freq]
    
    # If all numbers have the same frequency, return the first number
    if len(modes) == len(set(numbers)):
        return modes[0]
    
    # Return single mode or list of modes
    return modes[0] if len(modes) == 1 else modes