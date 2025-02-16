def spaghetti_sort(arr):
    """
    Implement the spaghetti sort algorithm.
    
    The algorithm works by conceptually cutting strands of different lengths
    and then lining them up from shortest to longest.
    
    Args:
        arr (list): A list of comparable elements to be sorted.
    
    Returns:
        list: A new list with elements sorted in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains elements that cannot be compared.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    sorted_arr = []
    remaining = arr.copy()
    
    while remaining:
        # Find the minimum element
        try:
            min_elem = min(remaining)
        except TypeError:
            raise ValueError("List contains elements that cannot be compared")
        
        # Add the minimum element to sorted array and remove from remaining
        sorted_arr.append(min_elem)
        remaining.remove(min_elem)
    
    return sorted_arr