from typing import List, Union
from collections import Counter

def find_mode(numbers: List[Union[int, float]]) -> Union[int, float, List[Union[int, float]]]:
    """
    Find the mode(s) of a list of numbers.
    
    Args:
        numbers (List[Union[int, float]]): A list of numbers
    
    Returns:
        Union[int, float, List[Union[int, float]]]: 
        - The single mode if there's one unique mode
        - A list of modes if multiple numbers appear with the same highest frequency
        - Raises ValueError if the input list is empty
    
    Raises:
        ValueError: If the input list is empty
    """
    if not numbers:
        raise ValueError("Cannot find mode of an empty list")
    
    # Normalize mixed types to floats for comparison
    normalized_numbers = [float(num) for num in numbers]
    
    # Count the frequency of each number
    frequency = Counter(normalized_numbers)
    
    # Find the maximum frequency
    max_freq = max(frequency.values())
    
    # Find modes with maximum frequency while preserving original representation
    modes = []
    for mode, freq in frequency.items():
        if freq == max_freq:
            # Find the first index of this mode and get original representation
            original_index = normalized_numbers.index(mode)
            modes.append(numbers[original_index])
    
    # Return single mode or list of modes
    return modes[0] if len(modes) == 1 else modes