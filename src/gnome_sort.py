def gnome_sort(arr):
    """
    Implement the Gnome Sort algorithm.
    
    Gnome Sort, also known as Stupid Sort, works by comparing adjacent elements
    and swapping them if they are in the wrong order, then moving back to 
    previous elements to ensure the list is sorted.
    
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
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Gnome Sort algorithm
    index = 0
    while index < len(arr):
        # If at the start or previous elements are in order, move forward
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            # Swap elements and move back
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    
    return arr