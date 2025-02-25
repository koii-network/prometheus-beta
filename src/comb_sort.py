def comb_sort(arr):
    """
    Implement the Comb Sort algorithm for sorting a list in ascending order.
    
    Comb sort is an improvement over bubble sort. It eliminates turtles (small values 
    near the end of the list) by using a gap that decreases in each iteration.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Define initial gap using Shrink factor of 1.3
    gap = len(arr)
    shrink = 1.3
    sorted_flag = False
    
    while not sorted_flag:
        # Update gap
        gap = max(int(gap / shrink), 1)
        
        # Set sorted flag to True initially
        sorted_flag = True
        
        # Compare elements with gap
        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                # Swap elements
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                # If a swap occurs, list is not yet sorted
                sorted_flag = False
        
        # If gap is 1 and no swaps occurred, list is sorted
        if gap == 1 and sorted_flag:
            break
    
    return arr