def spaghetti_sort(arr):
    """
    Implement the Spaghetti Sort algorithm.
    
    This algorithm works by simulating sorting 'spaghetti strands' of different lengths.
    
    Args:
        arr (list): A list of comparable elements to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    strands = arr.copy()
    
    # Sort the strands (simulate cutting and aligning spaghetti)
    sorted_strands = sorted(strands)
    
    return sorted_strands