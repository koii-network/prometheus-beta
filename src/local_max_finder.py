def find_local_maxima(arr):
    """
    Find local maximum values in an input array.
    
    A local maximum is an element that is strictly greater than its immediate neighbors.
    For the first and last elements, they are local maxima if they are greater than 
    their single adjacent element.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Indices of local maximum values
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Handle single element case
    if len(arr) == 1:
        return [0]
    
    local_maxima = []
    
    # Check first element
    if len(arr) > 1 and arr[0] > arr[1]:
        local_maxima.append(0)
    
    # Check middle elements
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            local_maxima.append(i)
    
    # Check last element
    if len(arr) > 1 and arr[-1] > arr[-2]:
        local_maxima.append(len(arr) - 1)
    
    return local_maxima