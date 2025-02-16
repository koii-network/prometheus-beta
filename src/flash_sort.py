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
    m = int(0.42 * n) + 1
    
    # Initialize classification array
    l = [0] * m
    
    # Compute classification weights
    c1 = (m - 1) / (max_val - min_val)
    
    # Step 1: Compute classification weights
    for x in arr:
        k = int(((x - min_val) * c1))
        l[k] += 1
    
    # Step 2: Compute cumulative count
    for k in range(1, m):
        l[k] += l[k-1]
    
    # Step 3: Permutation
    output = [0] * n
    
    # Backward pass
    for j in range(n - 1, -1, -1):
        k = int(((arr[j] - min_val) * c1))
        l[k] -= 1
        output[l[k]] = arr[j]
    
    # Step 4: Insert sort for remaining elements
    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    # Subdivide if necessary
    k = 0
    while k < m - 1:
        if l[k + 1] - l[k] > 20:
            output[l[k]:l[k+1]] = insertion_sort(output[l[k]:l[k+1]], 0, l[k+1] - l[k] - 1)
        k += 1
    
    return output