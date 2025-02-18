from typing import List, Union

def find_mode(numbers: List[Union[int, float]]) -> Union[int, float, List[Union[int, float]]]:
    """
    Find the mode (most frequent value) in a list of numbers.
    
    Args:
        numbers (List[Union[int, float]]): A list of numbers
    
    Returns:
        Union[int, float, List[Union[int, float]]]: 
        - The single mode if there's one most frequent value
        - A list of modes if multiple values appear with the same highest frequency
        - Raises ValueError if the input list is empty
    
    Raises:
        ValueError: If the input list is empty
    """
    if not numbers:
        raise ValueError("Cannot find mode of an empty list")
    
    # Count the frequency of each number
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Find the maximum frequency
    max_freq = max(frequency.values())
    
    # Find all numbers with the maximum frequency
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    
    # Return single mode or list of modes
    return modes[0] if len(modes) == 1 else modes