def gnome_sort(arr):
    """
    Implement the Gnome Sort algorithm.
    
    Gnome Sort (Stupid Sort) is a sorting algorithm that works similarly to how a gardener 
    sorts a line of flower pots. The gardener looks at each pot, and if it's out of order 
    with the previous pot, they swap them and go back one step. Otherwise, they move forward.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
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
    
    # Gnome sort implementation
    i = 1
    while i < len(arr):
        # If at the start or current element is in order with the previous, move forward
        if i == 0 or arr[i] >= arr[i-1]:
            i += 1
        else:
            # If out of order, swap and move back
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
    
    return arr