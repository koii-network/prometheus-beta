def bubble_sort(arr):
    """
    Sort an array of integers in non-decreasing order using Bubble Sort algorithm.
    
    Args:
        arr (list): A list of integers to be sorted.
    
    Returns:
        list: A new sorted list in non-decreasing order.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Create a copy of the input list to avoid modifying the original
    sorted_arr = arr.copy()
    
    # Bubble sort algorithm
    n = len(sorted_arr)
    for i in range(n):
        # Flag to optimize by breaking early if no swaps occur
        swapped = False
        
        for j in range(0, n - i - 1):
            # Compare adjacent elements and swap if they are in the wrong order
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return sorted_arr