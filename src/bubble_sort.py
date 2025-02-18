def bubble_sort(arr):
    """
    Implements the bubble sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains elements that cannot be compared.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the list to avoid modifying the original
    sorted_arr = arr.copy()
    
    # If list is empty or has only one element, return as-is
    if len(sorted_arr) <= 1:
        return sorted_arr
    
    # Bubble sort implementation
    n = len(sorted_arr)
    for i in range(n):
        # Flag to optimize by breaking early if no swaps occur
        swapped = False
        
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            try:
                if sorted_arr[j] > sorted_arr[j + 1]:
                    # Swap elements
                    sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                    swapped = True
            except TypeError:
                raise ValueError("List contains elements that cannot be compared")
        
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
    
    return sorted_arr