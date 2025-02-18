import math

def introsort(arr):
    """
    Implement Introsort algorithm (Introspective Sort)
    
    Introsort is a hybrid sorting algorithm that combines:
    - Quicksort for initial sorting 
    - Heapsort when the recursion depth exceeds a certain threshold
    
    Args:
        arr (list): The list to be sorted
    
    Returns:
        list: Sorted list in ascending order
    """
    # Create a copy to prevent in-place modification
    arr = arr.copy()
    
    if len(arr) <= 1:
        return arr
    
    # Maximum depth before switching to heapsort
    max_depth = 2 * math.floor(math.log2(len(arr)))
    
    def _introsort_recursive(arr, depth_limit):
        """
        Recursive helper function for introsort
        
        Args:
            arr (list): Sublist to be sorted
            depth_limit (int): Remaining recursion depth
        
        Returns:
            list: Sorted sublist
        """
        n = len(arr)
        
        # Switch to heapsort if max recursion depth is reached
        if depth_limit == 0:
            return _heapsort(arr)
        
        # Small arrays use insertion sort
        if n <= 16:
            return _insertion_sort(arr)
        
        # Partition 
        if n > 1:
            # Median-of-three pivot selection
            mid = n // 2
            if arr[0] > arr[-1]:
                arr[0], arr[-1] = arr[-1], arr[0]
            if arr[mid] > arr[-1]:
                arr[mid], arr[-1] = arr[-1], arr[mid]
            if arr[0] > arr[mid]:
                arr[0], arr[mid] = arr[mid], arr[0]
            
            pivot = arr[mid]
            arr[mid], arr[-1] = arr[-1], arr[mid]  # Move pivot to end
            
            # Partition
            i = 0
            for j in range(n-1):
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            
            arr[i], arr[-1] = arr[-1], arr[i]
            
            # Recursively sort
            left = arr[:i]
            right = arr[i+1:]
            
            left = _introsort_recursive(left, depth_limit - 1)
            right = _introsort_recursive(right, depth_limit - 1)
            
            # Recombine
            return left + [arr[i]] + right
        
        return arr
    
    def _heapsort(arr):
        """
        Heapsort implementation
        
        Args:
            arr (list): List to sort
        
        Returns:
            list: Sorted list
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
        
        n = len(arr)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            _heapify(arr, n, i)
        
        # Extract elements from heap one by one
        for i in range(n-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            _heapify(arr, i, 0)
        
        return arr
    
    def _insertion_sort(arr):
        """
        Insertion sort for small arrays
        
        Args:
            arr (list): List to sort
        
        Returns:
            list: Sorted list
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        
        return arr
    
    # Call recursive introsort with initial depth limit
    return _introsort_recursive(arr, max_depth)