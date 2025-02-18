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
    
    # Find all numbers with the maximum frequency
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    
    # Resolve multiple modes to the corresponding original values
    matching_modes = [numbers[normalized_numbers.index(mode)] for mode in modes]
    
    # Return single mode or list of modes, maintaining original value
    return matching_modes[0] if len(matching_modes) == 1 else matching_modes