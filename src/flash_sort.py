def flash_sort(arr):
    """
    Implement the Flash Sort algorithm for sorting a list of numbers.
    
    Flash Sort is a distribution sorting algorithm that works efficiently 
    for uniformly distributed data by first classifying elements into buckets.
    
    Args:
        arr (list): A list of comparable elements to be sorted
    
    Returns:
        list: A new sorted list with elements in ascending order
    """
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Find min and max to determine the range
    min_val = min(arr)
    max_val = max(arr)
    
    # Prevent division by zero
    if min_val == max_val:
        return arr.copy()
    
    # Number of buckets (typically around 0.1 * length of the array)
    m = max(1, int(0.1 * len(arr)))
    
    # Calculate the bucket size
    c1 = (m - 1) / (max_val - min_val)
    
    # Create buckets to classify elements
    l = [0] * m
    
    # Count elements in each bucket
    for x in arr:
        k = int(c1 * (x - min_val))
        l[k] += 1
    
    # Modify l to contain indices
    for i in range(1, m):
        l[i] += l[i-1]
    
    # Create output array
    output = [0] * len(arr)
    
    # Move elements to their correct buckets
    for x in reversed(arr):
        k = int(c1 * (x - min_val))
        output[l[k] - 1] = x
        l[k] -= 1
    
    return output