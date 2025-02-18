def gnome_sort(arr):
    """
    Implement the Gnome Sort algorithm.
    
    Gnome Sort is a simple sorting algorithm that works similarly to how a gnome 
    sorts a line of flower pots. It works as follows:
    1. If the current element is in the right order with the previous element, move forward
    2. If the current element is out of order, swap it with the previous element
    3. Move back one position and repeat the process
    
    Args:
        arr (list): The list to be sorted
    
    Returns:
        list: The sorted list
    
    Raises:
        TypeError: If the input is not a list
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the input list to avoid modifying the original
    arr = arr.copy()
    
    # If the list is empty or has only one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Start from the second element (index 1)
    i = 1
    while i < len(arr):
        # If first element or current element is greater than the previous, move forward
        if i == 0 or arr[i] >= arr[i-1]:
            i += 1
        else:
            # Swap the current element with the previous element
            arr[i], arr[i-1] = arr[i-1], arr[i]
            # Move back one position
            i -= 1
    
    return arr