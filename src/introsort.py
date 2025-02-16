import math

def insertion_sort(arr, left, right):
    """
    Insertion sort for small subarrays in introsort.
    
    Args:
        arr (list): The list to be sorted
        left (int): Starting index of the subarray
        right (int): Ending index of the subarray
    """
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, left, right):
    """
    Partition function for quicksort used in introsort.
    
    Args:
        arr (list): The list to be partitioned
        left (int): Starting index of the subarray
        right (int): Ending index of the subarray
    
    Returns:
        int: The partition index
    """
    # Choose the rightmost element as pivot
    pivot = arr[right]
    i = left - 1
    
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def introsort_recursive(arr, left, right, max_depth):
    """
    Recursive helper function for introsort.
    
    Args:
        arr (list): The list to be sorted
        left (int): Starting index of the subarray
        right (int): Ending index of the subarray
        max_depth (int): Maximum recursion depth
    """
    # If the subarray is small, use insertion sort
    if right - left + 1 <= 16:
        insertion_sort(arr, left, right)
        return
    
    # If max recursion depth is reached, use heapsort
    if max_depth == 0:
        heapsort(arr, left, right)
        return
    
    # Perform quicksort partition
    pivot_index = partition(arr, left, right)
    
    # Recursively sort left and right subarrays
    introsort_recursive(arr, left, pivot_index - 1, max_depth - 1)
    introsort_recursive(arr, pivot_index + 1, right, max_depth - 1)

def heapsort(arr, left, right):
    """
    Heapsort implementation for use in introsort.
    
    Args:
        arr (list): The list to be sorted
        left (int): Starting index of the subarray
        right (int): Ending index of the subarray
    """
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and arr[l] > arr[largest]:
            largest = l
        
        if r < n and arr[r] > arr[largest]:
            largest = r
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = right - left + 1
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr[left:right+1], n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[left], arr[left + i] = arr[left + i], arr[left]
        heapify(arr[left:right+1], i, 0)

def introsort(arr):
    """
    Introsort algorithm implementation.
    
    Introsort is a hybrid sorting algorithm that provides both 
    fast average performance and O(n log n) worst-case performance.
    It combines quicksort, heapsort, and insertion sort.
    
    Args:
        arr (list): The list to be sorted
    
    Returns:
        list: Sorted list
    """
    if not arr:
        return arr
    
    # Calculate maximum recursion depth
    max_depth = 2 * math.floor(math.log2(len(arr)))
    
    # Create a copy to avoid modifying the original list
    arr_copy = arr.copy()
    
    # Call recursive introsort function
    introsort_recursive(arr_copy, 0, len(arr_copy) - 1, max_depth)
    
    return arr_copy