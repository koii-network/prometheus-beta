from typing import List, Any

def multiply_corresponding_elements(arr1: List[Any], arr2: List[Any]) -> List[Any]:
    """
    Multiply corresponding elements from two input arrays of the same length.
    
    Args:
        arr1 (List[Any]): First input array
        arr2 (List[Any]): Second input array
    
    Returns:
        List[Any]: Array with elements multiplied element-wise
    
    Raises:
        ValueError: If input arrays have different lengths
    """
    if len(arr1) != len(arr2):
        raise ValueError("Input arrays must have the same length")
    
    return [x * y for x, y in zip(arr1, arr2)]