def gnome_sort(arr):
    """
    Implement the Gnome sort algorithm.
    
    Gnome sort is a simple sorting algorithm that works similarly to how a gnome 
    sorts a line of flower pots. It works by swapping adjacent elements if they 
    are in the wrong order, moving back and forth through the list.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If list contains elements that cannot be compared
    """
    # Create a copy of the input list to avoid modifying the original
    arr = arr.copy()
    
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If list is empty or has only one element, return it
    if len(arr) <= 1:
        return arr
    
    # Start with the first two elements
    i = 1
    while i < len(arr):
        # If current element is greater than or equal to the previous, move forward
        if i == 0 or arr[i] >= arr[i-1]:
            i += 1
        else:
            # Swap the current element with the previous one
            arr[i], arr[i-1] = arr[i-1], arr[i]
            # Move back to check if further swaps are needed
            i -= 1
    
    return arr