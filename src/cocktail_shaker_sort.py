def cocktail_shaker_sort(arr):
    """
    Implement the Cocktail Shaker Sort (Bidirectional Bubble Sort) algorithm.
    
    This sorting algorithm is a variation of bubble sort that sorts in both directions.
    It works by moving the largest element to the end in the forward pass, 
    and then the smallest element to the beginning in the backward pass.
    
    Args:
        arr (list): The list to be sorted.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Validate input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    
    # Flag to optimize the algorithm by breaking early if no swaps occur
    swapped = True
    start = 0
    end = len(sorted_arr) - 1
    
    while swapped:
        # Reset swapped flag for this pass
        swapped = False
        
        # Forward pass (left to right)
        for i in range(start, end):
            if sorted_arr[i] > sorted_arr[i + 1]:
                # Swap elements
                sorted_arr[i], sorted_arr[i + 1] = sorted_arr[i + 1], sorted_arr[i]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
        
        # Move the end point back by one, as the last element is now in place
        end -= 1
        
        # Backward pass (right to left)
        for i in range(end - 1, start - 1, -1):
            if sorted_arr[i] > sorted_arr[i + 1]:
                # Swap elements
                sorted_arr[i], sorted_arr[i + 1] = sorted_arr[i + 1], sorted_arr[i]
                swapped = True
        
        # Move the start point forward
        start += 1
    
    return sorted_arr