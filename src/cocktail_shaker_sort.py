def cocktail_shaker_sort(arr):
    """
    Implement the Cocktail Shaker Sort (Bidirectional Bubble Sort) algorithm.
    
    This sorting algorithm is a variation of bubble sort that sorts in both 
    directions. It works by sorting the list from left to right, and then 
    from right to left in each iteration, which can be more efficient than 
    standard bubble sort for some input types.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: The sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If list contains elements that cannot be compared.
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    
    # Flag to optimize sorting by detecting if any swaps occurred
    swapped = True
    start = 0
    end = len(sorted_arr) - 1
    
    while swapped:
        # Reset swap flag for this pass
        swapped = False
        
        # Forward pass (left to right)
        for i in range(start, end):
            if sorted_arr[i] > sorted_arr[i + 1]:
                # Swap elements
                sorted_arr[i], sorted_arr[i + 1] = sorted_arr[i + 1], sorted_arr[i]
                swapped = True
        
        # If no swapping occurred, list is sorted
        if not swapped:
            break
        
        # Reset swap flag
        swapped = False
        
        # Reduce end point
        end -= 1
        
        # Backward pass (right to left)
        for i in range(end - 1, start - 1, -1):
            if sorted_arr[i] > sorted_arr[i + 1]:
                # Swap elements
                sorted_arr[i], sorted_arr[i + 1] = sorted_arr[i + 1], sorted_arr[i]
                swapped = True
        
        # Increase start point
        start += 1
    
    return sorted_arr