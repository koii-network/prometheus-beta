def flash_sort(arr):
    """
    Implement the Flash Sort algorithm for efficient sorting.
    
    Flash Sort is a distribution sorting algorithm that works particularly well 
    for data with non-uniform distribution. It has an average time complexity 
    of O(n + k) where k is the number of classes/bins.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-comparable elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # Ensure all elements are comparable
    try:
        arr = list(arr)  # Create a copy to avoid modifying original
    except TypeError:
        raise TypeError("List contains non-comparable elements")
    
    # If list has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Find min and max values
    min_val = min(arr)
    max_val = max(arr)
    
    # Handle case where all elements are the same
    if min_val == max_val:
        return arr
    
    # Number of classes/bins
    m = int(0.43 * len(arr)) + 1
    
    # Create classes/bins
    classes = [0] * m
    
    # Compute class for each element
    c = (m - 1) / (max_val - min_val)
    
    # Count elements in each class
    for x in arr:
        k = int(c * (x - min_val))
        classes[k] += 1
    
    # Cumulative count of classes
    for i in range(1, m):
        classes[i] += classes[i-1]
    
    # Redistribute elements
    output = [0] * len(arr)
    
    # Backward pass
    for x in reversed(arr):
        k = int(c * (x - min_val))
        classes[k] -= 1
        output[classes[k]] = x
    
    return output