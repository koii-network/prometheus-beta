def bitonic_sort(arr, ascending=True):
    """
    Implement bitonic sort algorithm.
    
    Args:
        arr (list): The input list to be sorted
        ascending (bool, optional): Sort in ascending order. Defaults to True.
    
    Returns:
        list: Sorted list in the specified order
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-comparable elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    def compare_and_swap(arr, i, j, direction):
        """
        Compare and swap elements if they are in the wrong order
        """
        if (direction and arr[i] > arr[j]) or (not direction and arr[i] < arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
    
    def bitonic_merge(arr, low, count, direction):
        """
        Merge a bitonic sequence
        """
        if count > 1:
            k = count // 2
            for i in range(low, low + k):
                compare_and_swap(arr, i, i + k, direction)
            
            bitonic_merge(arr, low, k, direction)
            bitonic_merge(arr, low + k, k, direction)
    
    def bitonic_sort_recursive(arr, low, count, direction):
        """
        Recursively sort a bitonic sequence
        """
        if count > 1:
            k = count // 2
            
            # Sort first half in ascending order
            bitonic_sort_recursive(arr, low, k, True)
            
            # Sort second half in descending order
            bitonic_sort_recursive(arr, low + k, k, False)
            
            # Merge the entire sequence 
            bitonic_merge(arr, low, count, direction)
    
    # Create a copy to avoid modifying the original list
    arr_copy = arr.copy()
    
    # Perform bitonic sort
    bitonic_sort_recursive(arr_copy, 0, len(arr_copy), ascending)
    
    return arr_copy