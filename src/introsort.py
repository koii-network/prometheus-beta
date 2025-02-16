import math

def partition(arr, low, high):
    """Partition the array using the last element as pivot."""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def heapsort(arr, low, high):
    """Implement heapsort for the remaining elements."""
    def heapify(arr, n, root):
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != root:
            arr[root], arr[largest] = arr[largest], arr[root]
            heapify(arr, n, largest)
    
    n = high - low + 1
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr[low:high+1], n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[low], arr[low + i] = arr[low + i], arr[low]
        heapify(arr[low:high+1], i, 0)

def introsort(arr):
    """
    Implement Introsort (Introspective Sort) algorithm.
    
    Introsort is a hybrid sorting algorithm that combines 
    quicksort, heapsort, and insertion sort to provide 
    both fast average performance and O(n log n) worst-case performance.
    
    Args:
        arr (list): The list to be sorted
    
    Returns:
        list: The sorted list
    """
    if not arr:
        return arr
    
    # Maximum recursion depth
    max_depth = 2 * math.floor(math.log2(len(arr)))
    
    def _introsort(arr, low, high, max_depth):
        # If the array is small, use insertion sort
        if high - low + 1 <= 16:
            # Insertion sort for small arrays
            for i in range(low + 1, high + 1):
                key = arr[i]
                j = i - 1
                while j >= low and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
            return
        
        # If max recursion depth is reached, switch to heapsort
        if max_depth == 0:
            heapsort(arr, low, high)
            return
        
        # Partition and recursively sort
        pivot_index = partition(arr, low, high)
        
        # Sort left subarray
        _introsort(arr, low, pivot_index - 1, max_depth - 1)
        
        # Sort right subarray
        _introsort(arr, pivot_index + 1, high, max_depth - 1)
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Start the recursive introsort
    _introsort(arr, 0, len(arr) - 1, max_depth)
    
    return arr