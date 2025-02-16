def flash_sort(arr):
    """
    Implement the Flash Sort algorithm for efficient sorting.
    
    Flash Sort is a distribution sorting algorithm that works particularly well 
    for data with non-uniform distribution. It uses the concept of classification 
    and redistribution to achieve efficient sorting.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: The sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains non-comparable elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) <= 1:
        return arr.copy()
    
    # Find min and max to determine the range
    try:
        min_val = min(arr)
        max_val = max(arr)
    except TypeError:
        raise ValueError("List contains non-comparable elements")
    
    # Special case: all elements are the same
    if min_val == max_val:
        return arr.copy()
    
    # Number of classes (partitions)
    m = max(int(0.43 * len(arr)), 1)
    
    # Initialize classification array
    L = [0] * m
    
    # Compute classification
    c1 = (m - 1) / (max_val - min_val)
    
    # Classify elements
    for x in arr:
        k = int(c1 * (x - min_val))
        L[k] += 1
    
    # Compute cumulative frequencies
    for i in range(1, m):
        L[i] += L[i-1]
    
    # Create output array
    output = [None] * len(arr)
    
    # Redistribute elements
    for x in reversed(arr):
        k = int(c1 * (x - min_val))
        output[L[k] - 1] = x
        L[k] -= 1
    
    # Final permutation
    arr_sorted = [x for x in output]
    
    return arr_sorted