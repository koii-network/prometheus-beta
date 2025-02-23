import math

def introsort(arr):
    """
    Implement the Introsort algorithm, which is a hybrid sorting algorithm 
    that combines QuickSort, HeapSort, and Insertion Sort.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A sorted version of the input list
    """
    # If the list is empty or has a single element, return a copy
    if len(arr) <= 1:
        return arr.copy()

    # If the list is too small, use insertion sort
    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    # Heap sort implementation for deeper recursion levels
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    def heap_sort(arr, left, right):
        n = right - left + 1
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr[left:right+1], n, i)
        
        # Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            arr[left], arr[left + i] = arr[left + i], arr[left]
            heapify(arr[left:right+1], i, 0)
        
        return arr
    
    # Partition function for quicksort
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    # Recursive introsort implementation
    def _introsort_recursive(arr, left, right, max_depth):
        n = right - left + 1
        
        # Use insertion sort for small arrays
        if n <= 16:
            return insertion_sort(arr, left, right)
        
        # Switch to heapsort if recursion depth is too high
        if max_depth == 0:
            return heap_sort(arr, left, right)
        
        # Use quicksort
        pivot = partition(arr, left, right)
        
        # Recursively sort left and right partitions
        _introsort_recursive(arr, left, pivot - 1, max_depth - 1)
        _introsort_recursive(arr, pivot + 1, right, max_depth - 1)
        
        return arr
    
    # Create a copy to avoid modifying the original list
    arr_copy = arr.copy()
    
    # Calculate maximum recursion depth
    max_depth = 2 * math.floor(math.log2(len(arr_copy)))
    
    # Call recursive introsort
    return _introsort_recursive(arr_copy, 0, len(arr_copy) - 1, max_depth)