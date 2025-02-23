def gnome_sort(arr):
    """
    Implement the Gnome sort algorithm (also known as Stupid sort).
    
    The Gnome sort algorithm works by placing an element in its correct position 
    by continuously comparing adjacent elements and swapping them if they are in 
    the wrong order.
    
    Args:
        arr (list): The list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Actual Gnome sort implementation
    i = 0
    while i < len(arr):
        # If at the first element or previous element is smaller/equal, move forward
        if i == 0 or arr[i-1] <= arr[i]:
            i += 1
        else:
            # Swap elements and move back
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
    
    return arr