def bitonic_sort(arr, ascending=True):
    """
    Implement the bitonic sort algorithm.
    
    Args:
        arr (list): The input list to be sorted
        ascending (bool, optional): Sort in ascending order if True, 
                                    descending order if False. Defaults to True.
    
    Returns:
        list: The sorted list
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains elements of different types
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty or contains only one element
    if len(arr) <= 1:
        return arr.copy()
    
    # Ensure all elements are of the same type
    if len(set(type(x) for x in arr)) > 1:
        raise ValueError("All elements must be of the same type")
    
    def compare_and_swap(arr, i, j, direction):
        """
        Compare and potentially swap elements based on the direction
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
        Recursively sort the bitonic sequence
        """
        if count > 1:
            k = count // 2
            
            # Sort first half in ascending order
            bitonic_sort_recursive(arr, low, k, True)
            
            # Sort second half in descending order
            bitonic_sort_recursive(arr, low + k, k, False)
            
            # Merge the entire sequence in the specified direction
            bitonic_merge(arr, low, count, direction)
    
    # Create a copy to avoid modifying the original list
    result = arr.copy()
    
    # Full bitonic sort
    bitonic_sort_recursive(result, 0, len(result), ascending)
    
    return result