def quick_sort(arr):
    """
    Implement Quick Sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list 
    
    Raises:
        TypeError: If the input is not a list
        TypeError: If the list contains elements that cannot be compared
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    def _quick_sort(low, high):
        """Internal recursive quick sort function"""
        if low < high:
            # Partition the array
            pivot_index = _partition(low, high)
            
            # Recursively sort the left and right subarrays
            _quick_sort(low, pivot_index - 1)
            _quick_sort(pivot_index + 1, high)
    
    def _partition(low, high):
        """Partition the array and return the pivot index"""
        # Choose the rightmost element as pivot
        pivot = arr[high]
        
        # Index of smaller element
        i = low - 1
        
        # Traverse through the array
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                # Increment index of smaller element
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # Place pivot in its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    # Call the internal recursive sort
    _quick_sort(0, len(arr) - 1)
    
    return arr