from typing import List, Optional

def find_local_maxima(arr: List[int]) -> List[int]:
    """
    Find local maximum values in an input array.
    
    A local maximum is defined as an element that is strictly greater than 
    or equal to its immediate neighbors. For the first and last elements, 
    they are considered local maxima if they are greater than or equal to 
    their single adjacent neighbor.
    
    Args:
        arr (List[int]): Input array of integers
    
    Returns:
        List[int]: Indices of local maximum values in the input array
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    
    Examples:
        >>> find_local_maxima([1, 3, 2, 4, 1, 5])
        [1, 3, 5]
        >>> find_local_maxima([1, 2, 3, 4, 5])
        [4]
        >>> find_local_maxima([5, 4, 3, 2, 1])
        [0]
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Handle single element case
    if len(arr) == 1:
        return [0]
    
    # Find local maxima
    local_maxima = []
    
    # Check first element
    if arr[0] >= arr[1]:
        local_maxima.append(0)
    
    # Check middle elements
    for i in range(1, len(arr) - 1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            local_maxima.append(i)
    
    # Check last element
    if arr[-1] >= arr[-2]:
        local_maxima.append(len(arr) - 1)
    
    return local_maxima