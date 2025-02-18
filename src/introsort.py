import math

def introsort(arr):
    """
    Implements the Introsort algorithm for efficient sorting.
    
    Introsort begins with quicksort and switches to heapsort when the recursion 
    depth exceeds a level based on the array's logarithm.
    
    Args:
        arr (list): The list to be sorted
    
    Returns:
        list: A sorted version of the input list
    """
    if len(arr) <= 1:
        return arr
    
    max_depth = 2 * math.floor(math.log2(len(arr)))
    return _introsort_recursive(arr, 0, len(arr) - 1, max_depth)

def _introsort_recursive(arr, low, high, max_depth):
    """
    Recursive helper function for introsort.
    
    Args:
        arr (list): The list being sorted
        low (int): Starting index of the subarray
        high (int): Ending index of the subarray
        max_depth (int): Maximum recursion depth before switching to heapsort
    
    Returns:
        list: The sorted subarray
    """
    # If the subarray is small, use insertion sort
    if high - low + 1 <= 16:
        return _insertion_sort(arr, low, high)
    
    # If max recursion depth is reached, use heapsort
    if max_depth == 0:
        return _heapsort(arr, low, high)
    
    # Partition and recursively sort
    pivot_index = _partition(arr, low, high)
    
    _introsort_recursive(arr, low, pivot_index - 1, max_depth - 1)
    _introsort_recursive(arr, pivot_index + 1, high, max_depth - 1)
    
    return arr

def _partition(arr, low, high):
    """
    Partition function for quicksort with median-of-three pivot selection.
    
    Args:
        arr (list): The list being sorted
        low (int): Starting index of the subarray
        high (int): Ending index of the subarray
    
    Returns:
        int: The pivot index
    """
    # Choose median of first, middle, and last elements as pivot
    mid = (low + high) // 2
    
    # Sort first, middle, and last elements
    if arr[mid] < arr[low]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] < arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def _insertion_sort(arr, low, high):
    """
    Insertion sort for small subarrays.
    
    Args:
        arr (list): The list being sorted
        low (int): Starting index of the subarray
        high (int): Ending index of the subarray
    
    Returns:
        list: The sorted subarray
    """
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

def _heapsort(arr, low, high):
    """
    Heapsort implementation for use when recursion depth is exceeded.
    
    Args:
        arr (list): The list being sorted
        low (int): Starting index of the subarray
        high (int): Ending index of the subarray
    
    Returns:
        list: The sorted subarray
    """
    # Build max heap
    n = high - low + 1
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i + low, low, high)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[low], arr[low + i] = arr[low + i], arr[low]
        _heapify(arr, i, low, low, high)
    
    return arr

def _heapify(arr, n, i, low, high):
    """
    Heapify a subtree rooted at index i.
    
    Args:
        arr (list): The list being sorted
        n (int): Size of the heap
        i (int): Root index of the subtree
        low (int): Starting index of the subarray
        high (int): Ending index of the subarray
    """
    largest = i
    left = 2 * (i - low) + 1 + low
    right = 2 * (i - low) + 2 + low
    
    if left < low + n and arr[left] > arr[largest]:
        largest = left
    
    if right < low + n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest, low, high)