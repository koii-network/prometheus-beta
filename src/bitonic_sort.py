def bitonic_sort(arr, ascending=True):
    """
    Implement bitonic sort algorithm.
    
    Args:
        arr (list): Input list to be sorted
        ascending (bool, optional): Sort in ascending order if True, 
                                    descending order if False. Defaults to True.
    
    Returns:
        list: Sorted list
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains elements of different types
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Check for type consistency
    if len(set(type(x) for x in arr)) > 1:
        raise ValueError("List must contain elements of the same type")
    
    def compare_and_swap(arr, i, j, direction):
        """
        Compare and swap elements if they are in the wrong order
        """
        if (direction and arr[i] > arr[j]) or (not direction and arr[i] < arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    
    def bitonic_merge(arr, low, count, direction):
        """
        Merge a bitonic sequence in given direction
        """
        if count > 1:
            k = count // 2
            for i in range(low, low + k):
                arr = compare_and_swap(arr, i, i + k, direction)
            
            arr = bitonic_merge(arr, low, k, direction)
            arr = bitonic_merge(arr, low + k, k, direction)
        
        return arr
    
    def bitonic_sort_recursive(arr, low, count, direction):
        """
        Recursively sort a bitonic sequence
        """
        if count > 1:
            k = count // 2
            
            # Sort first half in ascending order
            arr = bitonic_sort_recursive(arr, low, k, True)
            
            # Sort second half in descending order
            arr = bitonic_sort_recursive(arr, low + k, k, False)
            
            # Merge the entire sequence
            arr = bitonic_merge(arr, low, count, direction)
        
        return arr
    
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    
    # Perform bitonic sort
    sorted_arr = bitonic_sort_recursive(sorted_arr, 0, len(sorted_arr), ascending)
    
    return sorted_arr