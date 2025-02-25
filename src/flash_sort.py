def flash_sort(arr):
    """
    Implement the Flash Sort algorithm for efficient sorting.
    
    Flash Sort is a distribution sorting algorithm that uses classification 
    to improve the performance of sorting, especially for non-uniform distributions.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: The sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    n = len(arr)
    if n <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Find min and max
    min_val = min(arr)
    max_val = max(arr)
    
    # Handle case where all elements are the same
    if min_val == max_val:
        return arr
    
    # Determine number of classes
    m = int(0.43 * n) + 1
    
    # Create classification array
    l = [0] * m
    
    # Compute range per class
    c1 = (max_val - min_val) / m
    
    # Classify elements
    for x in arr:
        j = int((x - min_val) / c1)
        # Ensure j is within bounds
        j = min(j, m - 1)
        l[j] += 1
    
    # Cumulative count
    for j in range(1, m):
        l[j] += l[j-1]
    
    # Move elements to their correct classes
    result = [0] * n
    count = [0] * m
    
    for x in arr:
        j = int((x - min_val) / c1)
        j = min(j, m - 1)
        result[l[j] - 1 - count[j]] = x
        count[j] += 1
    
    # Insertion sort within each class
    for j in range(m):
        start = 0 if j == 0 else l[j-1]
        end = l[j]
        insertion_sort(result, start, end)
    
    return result

def insertion_sort(arr, start, end):
    """
    Perform insertion sort on a specific section of the array.
    
    Args:
        arr (list): The list to partially sort
        start (int): Starting index of the section
        end (int): Ending index of the section
    """
    for i in range(start + 1, end):
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key