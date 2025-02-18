def bitonic_sort(arr, ascending=True):
    """
    Implements the bitonic sort algorithm.
    
    Args:
        arr (list): The list to be sorted
        ascending (bool, optional): Sort direction. Defaults to True (ascending order)
    
    Returns:
        list: The sorted list
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-comparable elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    def compare_and_swap(subarr, i, j, direction):
        """
        Compare and swap elements if they are in the wrong order
        """
        if direction == (subarr[i] > subarr[j]):
            subarr[i], subarr[j] = subarr[j], subarr[i]
    
    def bitonic_merge(subarr, low, count, direction):
        """
        Merge a bitonic sequence
        """
        if count > 1:
            k = count // 2
            for i in range(low, low + k):
                compare_and_swap(subarr, i, i + k, direction)
            
            bitonic_merge(subarr, low, k, direction)
            bitonic_merge(subarr, low + k, k, direction)
    
    def bitonic_sort_recursive(subarr, low, count, direction):
        """
        Recursively sort a bitonic sequence
        """
        if count > 1:
            k = count // 2
            
            # Sort first half in ascending order
            bitonic_sort_recursive(subarr, low, k, True)
            
            # Sort second half in descending order
            bitonic_sort_recursive(subarr, low + k, k, False)
            
            # Merge the entire sequence
            bitonic_merge(subarr, low, count, direction)
    
    # Ensure the length is a power of 2
    def next_power_of_two(n):
        """Find the next power of 2 greater than or equal to n"""
        return 2 ** ((n - 1).bit_length())
    
    # Pad the array if needed
    original_length = len(arr)
    padded_length = next_power_of_two(original_length)
    
    if padded_length > original_length:
        arr.extend([arr[-1]] * (padded_length - original_length))
    
    # Perform bitonic sort
    bitonic_sort_recursive(arr, 0, len(arr), ascending)
    
    # Return only the original number of elements
    return arr[:original_length]