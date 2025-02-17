def quicksort(arr):
    """
    Implement Quick Sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    def _quicksort_inplace(low, high):
        """
        Recursive helper function to perform quicksort in-place
        
        Args:
            low (int): Starting index of the subarray
            high (int): Ending index of the subarray
        """
        if low < high:
            # Partition the array
            pivot_index = _partition(low, high)
            
            # Recursively sort left and right subarrays
            _quicksort_inplace(low, pivot_index - 1)
            _quicksort_inplace(pivot_index + 1, high)
    
    def _partition(low, high):
        """
        Choose the rightmost element as pivot and partition the array
        
        Args:
            low (int): Starting index of the subarray
            high (int): Ending index of the subarray
        
        Returns:
            int: The pivot index after partitioning
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
        
        # Place pivot in correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    # Start the quicksort process
    _quicksort_inplace(0, len(arr) - 1)
    
    return arr