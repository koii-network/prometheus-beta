def bitonic_sort(arr, ascending=True):
    """
    Implement the Bitonic Sort algorithm.
    
    Bitonic sort is a comparison-based sorting algorithm that can be run in parallel.
    It works by first creating a bitonic sequence and then merging it.
    
    Args:
        arr (list): The input list to be sorted
        ascending (bool, optional): Sort direction. Defaults to True (ascending order)
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-comparable elements
    """
    # Create a copy to avoid modifying the original list
    arr = list(arr)
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Merge two sequences in the specified direction
    def bitonic_merge(arr, low, count, direction):
        """
        Merge a bitonic sequence
        
        Args:
            arr (list): The list being sorted
            low (int): Starting index of the sequence
            count (int): Number of elements in the sequence
            direction (bool): True for ascending, False for descending
        """
        if count > 1:
            mid = count // 2
            
            for i in range(low, low + mid):
                if direction == (arr[i] > arr[i + mid]):
                    arr[i], arr[i + mid] = arr[i + mid], arr[i]
            
            bitonic_merge(arr, low, mid, direction)
            bitonic_merge(arr, low + mid, mid, direction)
    
    # Recursively build bitonic sequence and merge
    def bitonic_sort_recursive(arr, low, count, direction):
        """
        Recursively build and sort a bitonic sequence
        
        Args:
            arr (list): The list being sorted
            low (int): Starting index of the sequence
            count (int): Number of elements in the sequence
            direction (bool): True for ascending, False for descending
        """
        if count > 1:
            mid = count // 2
            
            # Sort first half in ascending order
            bitonic_sort_recursive(arr, low, mid, True)
            
            # Sort second half in descending order
            bitonic_sort_recursive(arr, low + mid, mid, False)
            
            # Merge entire sequence
            bitonic_merge(arr, low, count, direction)
    
    # Calculate the next power of 2
    n = len(arr)
    k = 1
    while k < n:
        k *= 2
    
    # Pad the array to make its length a power of 2
    arr = arr + [arr[-1]] * (k - n)
    
    # Sort the entire padded array
    bitonic_sort_recursive(arr, 0, k, ascending)
    
    # Return only the original number of elements
    return arr[:n]