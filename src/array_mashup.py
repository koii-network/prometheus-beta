from typing import List

def arrayMashup(array1: List[int], array2: List[int]) -> List[int]:
    """
    Combine two arrays by summing elements at corresponding indices.

    Args:
        array1 (List[int]): First input array of positive integers
        array2 (List[int]): Second input array of positive integers

    Returns:
        List[int]: A new array where each element is the sum of 
                   corresponding elements from input arrays

    Raises:
        ValueError: If input arrays have different lengths
        TypeError: If inputs contain non-integer values
    """
    # Validate input types
    if not (isinstance(array1, list) and isinstance(array2, list)):
        raise TypeError("Inputs must be lists")
    
    # Validate array lengths
    if len(array1) != len(array2):
        raise ValueError("Input arrays must have equal length")
    
    # Validate all elements are positive integers
    if not (all(isinstance(x, int) and x > 0 for x in array1) and 
            all(isinstance(x, int) and x > 0 for x in array2)):
        raise TypeError("All elements must be positive integers")
    
    # Perform element-wise sum
    return [a + b for a, b in zip(array1, array2)]