from typing import List, Optional

def find_local_max_values(arr: List[int]) -> List[int]:
    """
    Find local maximum values in an input array.
    
    A local maximum is defined as an element that is greater than 
    its immediate neighbors on both sides.
    
    Args:
        arr (List[int]): Input array of integers
    
    Returns:
        List[int]: List of local maximum values
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-integer elements
    
    Examples:
        >>> find_local_max_values([1, 3, 2, 4, 1, 5, 3])
        [3, 4, 5]
        >>> find_local_max_values([1, 2, 3, 4, 5])
        [5]
        >>> find_local_max_values([5, 4, 3, 2, 1])
        [5]
        >>> find_local_max_values([])
        []
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # Check for non-integer elements
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Find local maximums
    local_maxes = []
    
    # Check first element
    if len(arr) > 1 and arr[0] > arr[1]:
        local_maxes.append(arr[0])
    
    # Check middle elements
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            local_maxes.append(arr[i])
    
    # Check last element
    if len(arr) > 1 and arr[-1] > arr[-2]:
        local_maxes.append(arr[-1])
    
    return local_maxes