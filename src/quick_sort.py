def quick_sort(arr):
    """
    Implement Quick Sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    
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
    
    def _quick_sort_inplace(low, high):
        """Internal recursive quick sort method"""
        if low < high:
            # Partition the array
            pivot_index = _partition(low, high)
            
            # Recursively sort the sub-arrays
            _quick_sort_inplace(low, pivot_index - 1)
            _quick_sort_inplace(pivot_index + 1, high)
    
    def _partition(low, high):
        """Partition the array and return the pivot index"""
        # Choose the rightmost element as pivot
        pivot = arr[high]
        
        # Pointer for greater element
        i = low - 1
        
        # Traverse through all elements
        # Compare each element with pivot
        for j in range(low, high):
            if arr[j] <= pivot:
                # If element smaller than pivot is found
                # Swap it with the greater element pointed by i
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # Swap the pivot element with the greater element specified by i
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        
        # Return the position from where partition is done
        return i + 1
    
    # Start the recursive sorting process
    _quick_sort_inplace(0, len(arr) - 1)
    
    return arr