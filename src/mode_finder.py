from typing import List, Union

def find_mode(numbers: List[int]) -> Union[int, List[int]]:
    """
    Find the mode (most frequent element) in a list of numbers.
    
    Args:
        numbers (List[int]): A list of integers to find the mode from.
    
    Returns:
        Union[int, List[int]]: The mode of the list. 
        - If there's a single mode, returns that number.
        - If there are multiple modes, returns a list of those numbers.
        - If the input list is empty, returns an empty list.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    
    Examples:
        >>> find_mode([1, 2, 2, 3, 4])
        2
        >>> find_mode([1, 1, 2, 2, 3])
        [1, 2]
        >>> find_mode([])
        []
    """
    # Check input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not numbers:
        return []
    
    # Check all elements are integers
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements must be integers")
    
    # Count frequencies
    freq_dict = {}
    for num in numbers:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    
    # Find max frequency
    max_freq = max(freq_dict.values())
    
    # Find all numbers with max frequency
    modes = [num for num, freq in freq_dict.items() if freq == max_freq]
    
    # Return single mode or list of modes
    return modes[0] if len(modes) == 1 else modes