def selection_sort(arr):
    """
    Implement the selection sort algorithm.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-comparable elements.
    """
    # Validate input 
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the list to avoid modifying the original
    sorted_arr = arr.copy()
    
    # Traverse through all array elements
    for i in range(len(sorted_arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(sorted_arr)):
            # Compare current element with minimum found so far
            try:
                if sorted_arr[j] < sorted_arr[min_idx]:
                    min_idx = j
            except TypeError:
                raise ValueError("List contains non-comparable elements")
        
        # Swap the found minimum element with the first element
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    
    return sorted_arr