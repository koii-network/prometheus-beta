from typing import List, Dict, Union

def multiArrayManipulator(arr: List[List[int]], manipulations: Dict[str, Union[int, str]]) -> List[List[int]]:
    """
    Perform various manipulations on a 2D integer array.

    Args:
        arr (List[List[int]]): The input 2D integer array to manipulate.
        manipulations (Dict[str, Union[int, str]]): A dictionary of manipulations to perform.
            Supported operations:
            - 'multiply': Multiply each element by a given number
            - 'add': Add a given number to each element
            - 'transpose': Transpose the array (swap rows and columns)

    Returns:
        List[List[int]]: The manipulated array.

    Raises:
        ValueError: If the input array is empty or manipulations are invalid.
        TypeError: If input types are incorrect.
    """
    # Validate input
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    if not isinstance(arr, list) or not all(isinstance(row, list) for row in arr):
        raise TypeError("Input must be a 2D list of integers")
    
    # Create a copy of the array to avoid modifying the original
    result = [row.copy() for row in arr]
    
    # Process each manipulation
    for op, value in manipulations.items():
        if op == 'multiply':
            # Validate multiply operation
            if not isinstance(value, (int, float)):
                raise TypeError("Multiply value must be a number")
            
            result = [[elem * value for elem in row] for row in result]
        
        elif op == 'add':
            # Validate add operation
            if not isinstance(value, (int, float)):
                raise TypeError("Add value must be a number")
            
            result = [[elem + value for elem in row] for row in result]
        
        elif op == 'transpose':
            # Transpose the array
            result = list(map(list, zip(*result)))
        
        else:
            raise ValueError(f"Unsupported manipulation: {op}")
    
    return result