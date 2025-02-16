def flash_sort(arr):
    """
    Implement the Flash Sort algorithm for sorting a list of numbers.
    
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
    
    # Handle trivial cases
    if n <= 1:
        return arr
    
    # Find min and max to create classification
    min_val = min(arr)
    max_val = max(arr)
    
    # Handle case where all elements are the same
    if min_val == max_val:
        return arr
    
    # Compute the number of classes dynamically
    m = max(1, int(0.42 * n))
    
    # Initialize and compute classification
    l = [0] * m
    c1 = (m - 1) / (max_val - min_val)
    
    # Compute classification and cumulative count
    for x in arr:
        k = int(((x - min_val) * c1))
        l[k] += 1
    
    # Compute cumulative count
    for k in range(1, m):
        l[k] += l[k-1]
    
    # Permutation
    output = [0] * n
    
    # Backward pass
    for j in range(n - 1, -1, -1):
        k = int(((arr[j] - min_val) * c1))
        l[k] -= 1
        output[l[k]] = arr[j]
    
    # Insertion sort on small segments to improve accuracy
    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    # Sort small segments
    start = 0
    for k in range(m):
        if l[k] - start > 20:
            output[start:l[k]] = insertion_sort(output[start:l[k]], 0, l[k] - start - 1)
        start = l[k]
    
    return output