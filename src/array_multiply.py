from typing import List, Union

def multiply(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Multiplies corresponding elements of the input array.

    Args:
        arr (List[Union[int, float]]): Input list of numbers to multiply.

    Returns:
        List[Union[int, float]]: A new list with corresponding elements multiplied.

    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
        ValueError: If input list is empty.
    """
    # Check for valid input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for empty list
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("List must contain only numeric elements")
    
    # Return a new list with multiplied elements 
    return [x*x for x in arr]