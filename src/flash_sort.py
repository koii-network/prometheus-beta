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
    n = len(arr)
    m = int(0.42 * n) + 1
    
    # Initialize buckets 
    class_count = [0] * m
    
    # Compute the indices
    c1 = (m - 1) / (max_val - min_val)
    
    # Count the number of elements in each class
    for x in arr:
        i = int(((x - min_val) * c1))
        class_count[i] += 1
    
    # Compute cumulative count
    for i in range(1, m):
        class_count[i] += class_count[i-1]
    
    # Create output array
    output = [0] * n
    
    # Redistribute elements
    for x in reversed(arr):
        # Compute class index
        j = int(((x - min_val) * c1))
        
        # Decrement count and place element
        class_count[j] -= 1
        output[class_count[j]] = x
    
    # Insertion sort on small classes (optional optimization)
    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    # Apply insertion sort on small classes or problematic parts
    for i in range(1, m):
        if class_count[i] - class_count[i-1] > 1:
            left = class_count[i-1]
            right = class_count[i] - 1
            if right - left > 10:  # optional: adjust threshold as needed
                output[left:right+1] = sorted(output[left:right+1])
            else:
                insertion_sort(output, left, right)
    
    return output