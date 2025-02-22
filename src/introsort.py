import math

def heapsort(arr, start, end):
    """Helper function to perform heapsort on a subarray."""
    def heapify(arr, n, i, start):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[start + left] > arr[start + largest]:
            largest = left

        if right < n and arr[start + right] > arr[start + largest]:
            largest = right

        if largest != i:
            arr[start + i], arr[start + largest] = arr[start + largest], arr[start + i]
            heapify(arr, n, largest, start)

    n = end - start
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, start)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[start], arr[start + i] = arr[start + i], arr[start]
        heapify(arr, i, 0, start)

def insertion_sort(arr, start, end):
    """Perform insertion sort on a small subarray."""
    for i in range(start + 1, end):
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    """Partition function for quicksort."""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def introsort(arr, max_depth=None):
    """
    Implement Introsort algorithm.
    
    Args:
        arr (list): The list to be sorted
        max_depth (int, optional): Maximum recursion depth. 
                                   Defaults to 2 * log2(length of array)
    
    Returns:
        list: Sorted array
    """
    if not arr:
        return arr

    # If max_depth is not specified, calculate it
    if max_depth is None:
        max_depth = 2 * math.floor(math.log2(len(arr)))

    def _introsort_recursive(arr, start, end, max_depth):
        # If the array is small, use insertion sort
        if end - start <= 16:
            insertion_sort(arr, start, end)
            return

        # If max depth is 0, switch to heapsort
        if max_depth == 0:
            heapsort(arr, start, end)
            return

        # Use quicksort partition
        pivot = partition(arr, start, end - 1)
        
        # Recursively sort left and right partitions
        _introsort_recursive(arr, start, pivot, max_depth - 1)
        _introsort_recursive(arr, pivot + 1, end, max_depth - 1)

    _introsort_recursive(arr, 0, len(arr), max_depth)
    return arr