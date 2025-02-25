def cocktail_shaker_sort(arr):
    """
    Implement the cocktail shaker sort (bidirectional bubble sort) algorithm.
    
    This sorting algorithm is a variation of bubble sort that sorts in both 
    directions. It works by moving the largest unsorted element to the end in 
    the forward pass, then the smallest unsorted element to the beginning 
    in the backward pass.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains elements that cannot be compared.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Flag to optimize early stopping if list becomes sorted
    swapped = True
    start = 0
    end = len(arr) - 1
    
    try:
        while swapped:
            # Reset swapped flag for this pass
            swapped = False
            
            # Forward pass (left to right)
            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    # Swap elements
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            
            # If no swapping occurred, list is sorted
            if not swapped:
                break
            
            # Decrease end index as largest element is now at the end
            end -= 1
            
            # Backward pass (right to left)
            for i in range(end - 1, start - 1, -1):
                if arr[i] > arr[i + 1]:
                    # Swap elements
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
            
            # Increase start index as smallest element is now at the beginning
            start += 1
        
        return arr
    
    except TypeError:
        # Catch cases where elements cannot be compared
        raise ValueError("List contains elements that cannot be compared")