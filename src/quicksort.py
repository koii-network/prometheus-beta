def quicksort(arr):
    """
    Implement the Quick Sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Base case: lists with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy of the input list to avoid modifying the original
    arr = arr.copy()
    
    # Recursive Quick Sort implementation
    def _quicksort(low, high):
        if low < high:
            # Partition the array
            pivot_index = _partition(low, high)
            
            # Recursively sort the sub-arrays
            _quicksort(low, pivot_index - 1)
            _quicksort(pivot_index + 1, high)
    
    def _partition(low, high):
        # Choose the rightmost element as pivot
        pivot = arr[high]
        
        # Index of smaller element
        i = low - 1
        
        # Traverse through all elements
        # Compare each element with pivot
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                # Increment index of smaller element
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # Place pivot in correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    # Start the quick sort process
    _quicksort(0, len(arr) - 1)
    
    return arr