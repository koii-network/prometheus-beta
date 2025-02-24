def quick_sort(arr):
    """
    Implement the Quick Sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Handle edge cases
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Empty or single-element list is already sorted
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    def _quick_sort(low, high):
        """
        Internal recursive function to perform quick sort.
        
        Args:
            low (int): Starting index of the sublist.
            high (int): Ending index of the sublist.
        """
        if low < high:
            # Partition the array
            pivot_index = _partition(low, high)
            
            # Recursively sort the two partitions
            _quick_sort(low, pivot_index - 1)
            _quick_sort(pivot_index + 1, high)
    
    def _partition(low, high):
        """
        Partition the sublist and return the pivot index.
        
        Args:
            low (int): Starting index of the sublist.
            high (int): Ending index of the sublist.
        
        Returns:
            int: The index of the pivot element after partitioning.
        """
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
        
        # Place pivot in its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    # Start the recursive quick sort
    _quick_sort(0, len(arr) - 1)
    
    return arr