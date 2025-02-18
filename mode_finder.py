from typing import List, Union
from collections import Counter

def find_mode(numbers: List[Union[int, float]]) -> Union[int, float, List[Union[int, float]]]:
    """
    Find the mode (most frequent value) in a list of numbers.
    
    Args:
        numbers (List[Union[int, float]]): A list of numbers
    
    Returns:
        Union[int, float, List[Union[int, float]]]: 
        - The single mode if there's one most frequent value
        - The first number if all numbers appear once
        - A list of modes if multiple values appear with the same highest frequency
        - Raises ValueError if the input list is empty
    
    Raises:
        ValueError: If the input list is empty
    """
    if not numbers:
        raise ValueError("Cannot find mode of an empty list")
    
    # Use Counter to count frequencies
    frequency = Counter(numbers)
    
    # Find the maximum frequency
    max_freq = max(frequency.values())
    
    # Find all numbers with the maximum frequency
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    
    # If there's only one mode, return it
    if len(modes) == 1:
        return modes[0]
    
    # If all numbers appear once, return the first number
    if max_freq == 1:
        return numbers[0]
    
    # Multiple modes with equal frequency
    return modes