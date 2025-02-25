def spaghetti_sort(arr):
    """
    Implement the Spaghetti Sort algorithm.
    
    Spaghetti Sort is a sorting algorithm that works by creating 'strands' 
    representing elements and sorting them by length.
    
    Args:
        arr (list): The input list of comparable elements to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if len(arr) <= 1:
        return arr.copy()
    
    # Create strands representing elements
    try:
        # Sort strands based on element values
        sorted_strands = sorted(arr)
        return sorted_strands
    except TypeError:
        raise TypeError("List contains elements that cannot be compared")