from typing import List, Union, Any
from tabulate import tabulate

def log_array_table(arr: List[Union[Any, List[Any]]], headers: List[str] = None) -> str:
    """
    Convert an array to a formatted table string.

    Args:
        arr (List): The input array to be logged as a table.
        headers (List[str], optional): Custom headers for the table. 
                                       Defaults to None.

    Returns:
        str: A formatted table representation of the input array.

    Raises:
        TypeError: If input is not a list.
        ValueError: If the array is empty.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input array cannot be empty")
    
    # Determine if the array is 2D or 1D
    is_2d = all(isinstance(item, list) for item in arr)
    
    # If 1D array, convert to 2D
    if not is_2d:
        arr = [[item] for item in arr]
    
    # Use default headers if not provided
    if headers is None:
        headers = [f"Column {i+1}" for i in range(len(arr[0]))]
    
    # Validate headers match array structure
    if len(headers) != len(arr[0]):
        raise ValueError("Number of headers must match number of columns")
    
    # Use tabulate to create the table
    return tabulate(arr, headers=headers, tablefmt="grid")