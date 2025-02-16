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
        ValueError: If list contains non-comparable elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    def bitonic_merge(start, length, direction):
        """
        Merge a bitonic sequence
        
        Args:
            start (int): Starting index of the sequence
            length (int): Length of the sequence
            direction (bool): Sort direction (True for ascending, False for descending)
        """
        if length > 1:
            k = length // 2
            for i in range(start, start + k):
                if direction == (arr[i] > arr[i + k]):
                    # Swap elements
                    arr[i], arr[i + k] = arr[i + k], arr[i]
            
            # Recursively merge the two halves
            bitonic_merge(start, k, direction)
            bitonic_merge(start + k, k, direction)
    
    def bitonic_sort_recursive(start, length, direction):
        """
        Recursively sort a bitonic sequence
        
        Args:
            start (int): Starting index of the sequence
            length (int): Length of the sequence
            direction (bool): Sort direction (True for ascending, False for descending)
        """
        if length > 1:
            k = length // 2
            
            # Sort first half in ascending order
            bitonic_sort_recursive(start, k, True)
            
            # Sort second half in descending order
            bitonic_sort_recursive(start + k, k, False)
            
            # Merge the entire sequence
            bitonic_merge(start, length, direction)
    
    # Determine the next power of 2 to pad the list if needed
    def next_power_of_two(n):
        return 1 << (n - 1).bit_length()
    
    n = len(arr)
    
    # Pad the list with the last element to make its length a power of 2
    if n & (n - 1):  # if n is not a power of 2
        pad_length = next_power_of_two(n)
        arr.extend([arr[-1]] * (pad_length - n))
    
    # Perform bitonic sort
    bitonic_sort_recursive(0, len(arr), ascending)
    
    # Remove padding if necessary
    return arr[:n]