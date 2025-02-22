def quick_sort(arr):
    """
    Sort an array of integers in non-decreasing order using Quick Sort algorithm.
    
    Args:
        arr (list): A list of integers to be sorted.
    
    Returns:
        list: A new sorted list in non-decreasing order.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    def _quick_sort(low, high):
        if low < high:
            # Partition the array
            pivot_index = _partition(low, high)
            
            # Recursively sort the sub-arrays
            _quick_sort(low, pivot_index - 1)
            _quick_sort(pivot_index + 1, high)
    
    def _partition(low, high):
        # Choose the rightmost element as pivot
        pivot = arr[high]
        
        # Pointer for greater element
        i = low - 1
        
        # Traverse through all elements
        # Compare each element with pivot
        for j in range(low, high):
            if arr[j] <= pivot:
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i += 1
                
                # Swapping element at i with element at j
                arr[i], arr[j] = arr[j], arr[i]
        
        # Swap the pivot element with the greater element specified by i
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        
        # Return the position from where partition is done
        return i + 1
    
    # Start quick sort
    _quick_sort(0, len(arr) - 1)
    
    return arr