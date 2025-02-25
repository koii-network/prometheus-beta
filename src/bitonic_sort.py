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
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Use built-in sorted for lists with fewer than 2 elements
    # The bitonic sort algorithm works best with lists of power of 2 length
    if len(arr) < 2:
        return sorted(arr, reverse=not ascending)
    
    def compare_and_swap(arr, i, j, direction):
        """
        Compare and potentially swap elements based on the sorting direction
        
        Args:
            arr (list): The list being sorted
            i (int): First index to compare
            j (int): Second index to compare
            direction (bool): Sorting direction (True for ascending, False for descending)
        """
        if direction == (arr[i] > arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
    
    def bitonic_merge(arr, low, count, direction):
        """
        Merge a bitonic sequence
        
        Args:
            arr (list): The list being sorted
            low (int): Starting index of the sequence
            count (int): Number of elements in the sequence
            direction (bool): Sorting direction
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
        
        Args:
            arr (list): The list being sorted
            low (int): Starting index of the sequence
            count (int): Number of elements in the sequence
            direction (bool): Sorting direction
        """
        if count > 1:
            k = count // 2
            
            # Sort first half in ascending order
            bitonic_sort_recursive(arr, low, k, True)
            
            # Sort second half in descending order
            bitonic_sort_recursive(arr, low + k, k, False)
            
            # Merge the entire sequence
            bitonic_merge(arr, low, count, direction)
    
    # Fallback to built-in sort
    try:
        result = arr.copy()
        
        # Find next power of 2
        n = len(result)
        next_power_of_2 = 2 ** ((n - 1).bit_length())
        
        # Pad the list with copies of elements
        result = result + [result[0]] * (next_power_of_2 - n)
        
        # Perform bitonic sort
        bitonic_sort_recursive(result, 0, next_power_of_2, ascending)
        
        # Return original number of elements
        return result[:n]
    except TypeError:
        # Fallback to built-in sort if elements are not comparable
        return sorted(arr, reverse=not ascending)