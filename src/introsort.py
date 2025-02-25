import math

def introsort(arr):
    """
    Implement the Introsort algorithm, which is a hybrid sorting algorithm 
    that combines Quicksort, Heapsort, and Insertion sort.
    
    Args:
        arr (list): The list to be sorted
    
    Returns:
        list: A sorted version of the input list
    """
    # If the list is small, use insertion sort
    if len(arr) <= 1:
        return arr
    
    # Calculate the maximum depth for recursion
    max_depth = 2 * math.floor(math.log2(len(arr)))
    
    def _introsort_helper(arr, depth_limit):
        """
        Recursive helper function for introsort
        
        Args:
            arr (list): Sublist to be sorted
            depth_limit (int): Remaining recursion depth
        
        Returns:
            list: Sorted sublist
        """
        n = len(arr)
        
        # Use insertion sort for small arrays
        if n <= 10:
            return _insertion_sort(arr)
        
        # If max recursion depth is reached, switch to heapsort
        if depth_limit == 0:
            return _heapsort(arr)
        
        # Partition using first element as pivot
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        
        # Recursively sort with reduced depth limit
        sorted_left = _introsort_helper(left, depth_limit - 1)
        sorted_right = _introsort_helper(right, depth_limit - 1)
        
        return sorted_left + [pivot] + sorted_right
    
    def _insertion_sort(arr):
        """
        Insertion sort for small subarrays
        
        Args:
            arr (list): Sublist to be sorted
        
        Returns:
            list: Sorted sublist
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    def _heapsort(arr):
        """
        Heapsort for when recursion depth is exceeded
        
        Args:
            arr (list): Sublist to be sorted
        
        Returns:
            list: Sorted sublist
        """
        def _heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[left] > arr[largest]:
                largest = left
            
            if right < n and arr[right] > arr[largest]:
                largest = right
            
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                _heapify(arr, n, largest)
        
        # Build max heap
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            _heapify(arr, n, i)
        
        # Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            _heapify(arr, i, 0)
        
        return arr
    
    # Call the helper function with initial depth limit
    return _introsort_helper(arr.copy(), max_depth)