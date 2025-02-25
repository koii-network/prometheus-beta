def flash_sort(arr):
    """
    Implement the Flash Sort algorithm for efficient sorting.
    
    Flash Sort is a distribution sorting algorithm that uses classification 
    to improve the performance of sorting, especially for non-uniform distributions.
    
    Args:
        arr (list): The input list to be sorted in-place
    
    Returns:
        list: The sorted list
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-comparable elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Determine the range of input values
    min_val = min(arr)
    max_val = max(arr)
    
    # Prevent division by zero
    if min_val == max_val:
        return arr
    
    # Number of classes (buckets)
    m = int(0.43 * len(arr)) + 1
    
    # Create classification array to hold the count of elements in each class
    l = [0] * m
    
    # Compute the range of each class
    c1 = (max_val - min_val) / m
    
    # Classify the elements
    for i in range(len(arr)):
        j = int((arr[i] - min_val) / c1)
        # Ensure j is within bounds
        j = min(j, m - 1)
        l[j] += 1
    
    # Compute cumulative count
    for i in range(1, m):
        l[i] += l[i-1]
    
    # Rearrange the elements
    k = 0
    j = 0
    while k < len(arr):
        # Find the initial class
        j = int((arr[k] - min_val) / c1)
        j = min(j, m - 1)
        
        # Move element to its correct position
        while k < l[j] - 1:
            # Swap elements
            temp = arr[k]
            pos = l[j] - 1
            arr[k] = arr[pos]
            arr[pos] = temp
            
            # Reduce the count for this class
            l[j] -= 1
        
        # Move to next element
        k += 1
    
    # Perform insertion sort on each class
    for i in range(m):
        start = 0 if i == 0 else l[i-1]
        end = l[i]
        insertion_sort(arr, start, end)
    
    return arr

def insertion_sort(arr, low, high):
    """
    Perform insertion sort on a subarray.
    
    Args:
        arr (list): The list to be partially sorted
        low (int): Starting index of the subarray
        high (int): Ending index of the subarray
    """
    for i in range(low + 1, high):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key