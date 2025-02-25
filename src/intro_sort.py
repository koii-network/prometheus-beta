import math

def heapsort(arr, start, end):
    """Heapsort subroutine for intro sort."""
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
    """Insertion sort for small subarrays."""
    for i in range(start + 1, end):
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, start, end):
    """Partition function for quicksort."""
    pivot = arr[end - 1]
    i = start - 1

    for j in range(start, end - 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end - 1] = arr[end - 1], arr[i + 1]
    return i + 1

def introsort_recursive(arr, start, end, max_depth):
    """Recursive implementation of introsort."""
    n = end - start
    
    # If array is small, use insertion sort
    if n <= 16:
        insertion_sort(arr, start, end)
        return
    
    # If max recursion depth is reached, switch to heapsort
    if max_depth == 0:
        heapsort(arr, start, end)
        return
    
    # Perform quicksort
    pivot = partition(arr, start, end)
    
    # Recursively sort left and right subarrays
    introsort_recursive(arr, start, pivot, max_depth - 1)
    introsort_recursive(arr, pivot + 1, end, max_depth - 1)

def intro_sort(arr):
    """
    Introsort: A hybrid sorting algorithm that combines quicksort, 
    heapsort, and insertion sort.
    
    Args:
        arr (list): The list to be sorted.
    
    Returns:
        list: The sorted list.
    """
    if not arr:
        return arr
    
    # Calculate the maximum recursion depth
    max_depth = 2 * math.floor(math.log2(len(arr)))
    
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    
    # Call recursive introsort
    introsort_recursive(sorted_arr, 0, len(sorted_arr), max_depth)
    
    return sorted_arr