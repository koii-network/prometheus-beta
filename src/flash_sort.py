def flash_sort(arr):
    """
    Implement the Flash Sort algorithm for sorting a list of numbers.
    
    Flash Sort is a distribution sorting algorithm that works by first creating 
    classification array and then redistributing elements into buckets based 
    on their relative magnitude.
    
    Args:
        arr (list): The input list of numbers to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All list elements must be numeric")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    n = len(arr)
    
    # Find min and max to create classification
    min_val = min(arr)
    max_val = max(arr)
    
    # Handle case where all elements are the same
    if min_val == max_val:
        return arr
    
    # Number of classification bins
    m = int(0.42 * n)
    
    # Initialize classification array
    l = [0] * m
    
    # Compute classification weights
    c1 = (m - 1) / (max_val - min_val)
    
    # Compute classification array
    for i in range(n):
        k = int(((arr[i] - min_val) * c1))
        l[k] += 1
    
    # Compute cumulative counts
    for k in range(1, m):
        l[k] += l[k-1]
    
    # Perform Flash Sort redistribution
    output = [0] * n
    
    # Backward pass to preserve stability
    for j in range(n - 1, -1, -1):
        k = int(((arr[j] - min_val) * c1))
        l[k] -= 1
        output[l[k]] = arr[j]
    
    # Prepare final sorted output
    sorted_arr = output
    
    return sorted_arr