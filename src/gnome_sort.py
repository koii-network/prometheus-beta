def gnome_sort(arr):
    """
    Implement the Gnome Sort algorithm.
    
    Gnome Sort is a simple sorting algorithm that works similarly to how a 
    gnome sorts a line of flower pots. It compares adjacent elements and 
    swaps them if they are in the wrong order, then goes back to check 
    previous elements.
    
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
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Start from the first index
    i = 1
    while i < len(arr):
        # If current element is greater than or equal to the previous, move forward
        if i == 0 or arr[i] >= arr[i-1]:
            i += 1
        else:
            # Swap elements if they are in the wrong order
            arr[i], arr[i-1] = arr[i-1], arr[i]
            # Move back to check previous elements
            i -= 1
    
    return arr