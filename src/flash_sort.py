def flash_sort(arr):
    """
    Implement the Flash Sort algorithm for efficient sorting.
    
    Flash Sort is a distribution sorting algorithm that works well on 
    uniformly distributed data with O(n) average time complexity.
    
    Args:
        arr (list): The input list to be sorted in ascending order
    
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
        return arr.copy()
    
    # Find min and max to determine distribution
    try:
        min_val = min(arr)
        max_val = max(arr)
    except TypeError:
        raise ValueError("List contains non-comparable elements")
    
    # If all elements are the same, return a copy
    if min_val == max_val:
        return arr.copy()
    
    # Number of buckets (classes)
    m = int(0.42 * len(arr)) + 1
    
    # Initialize buckets
    buckets = [0] * m
    
    # Calculate class boundaries
    c1 = (m - 1) / (max_val - min_val)
    
    # Count number of elements in each class
    for x in arr:
        i = int(((x - min_val) * c1))
        buckets[i] += 1
    
    # Cumulative count of elements in each class
    for i in range(1, m):
        buckets[i] += buckets[i-1]
    
    # Create output array and temp storage
    output = [0] * len(arr)
    
    # Permute elements
    for x in reversed(arr):
        i = int(((x - min_val) * c1))
        buckets[i] -= 1
        output[buckets[i]] = x
    
    return output