from collections import Counter
from typing import List, Union

def find_mode(numbers: List[Union[int, float]]) -> Union[int, float, List[Union[int, float]]]:
    """
    Find the mode(s) of a list of numbers.
    
    Args:
        numbers (List[Union[int, float]]): A list of numbers to find the mode(s) of.
    
    Returns:
        Union[int, float, List[Union[int, float]]]: 
        - The single mode if there's one unique mode
        - A list of modes if multiple numbers have the same highest frequency
        - Raises ValueError if the input list is empty
    
    Raises:
        ValueError: If the input list is empty
    """
    if not numbers:
        raise ValueError("Cannot find mode of an empty list")
    
    # Count the frequency of each number
    frequency = Counter(numbers)
    
    # Find the maximum frequency
    max_frequency = max(frequency.values())
    
    # Find all numbers with the maximum frequency
    modes = [num for num, count in frequency.items() if count == max_frequency]
    
    # Return single mode or list of modes
    return modes[0] if len(modes) == 1 else modes