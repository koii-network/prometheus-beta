import math

def heapify(arr, n, i):
    """
    Heapify a subtree rooted at index i.
    
    Args:
        arr (list): The list to be heapified
        n (int): Size of the heap
        i (int): Root index of the subtree
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is larger than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Perform heap sort on the input array.
    
    Args:
        arr (list): The list to be sorted
    """
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
        heapify(arr, i, 0)

def insertion_sort(arr, left=0, right=None):
    """
    Perform insertion sort on the input array or a portion of it.
    
    Args:
        arr (list): The list to be sorted
        left (int, optional): Starting index. Defaults to 0.
        right (int, optional): Ending index. Defaults to None.
    """
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    """
    Partition the array for quicksort.
    
    Args:
        arr (list): The list to be partitioned
        low (int): Starting index
        high (int): Ending index
    
    Returns:
        int: Partition index
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def intro_sort(arr, max_depth=None):
    """
    Implement intro sort algorithm.
    
    Intro sort is a hybrid sorting algorithm that combines quicksort, 
    heapsort, and insertion sort to achieve O(n log n) worst-case performance.
    
    Args:
        arr (list): The list to be sorted
        max_depth (int, optional): Maximum recursion depth. Defaults to None.
    
    Returns:
        list: Sorted list
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Make a copy to avoid modifying the original list
    arr = arr.copy()
    
    # If max_depth is not specified, calculate it based on list size
    if max_depth is None:
        max_depth = 2 * math.floor(math.log2(len(arr)))
    
    def _intro_sort_recursive(arr, low, high, max_depth):
        # Base case: small array
        if high - low <= 16:
            insertion_sort(arr, low, high)
            return
        
        # If max depth is reached, use heapsort
        if max_depth <= 0:
            heap_sort(arr[low:high+1])
            return
        
        # Use quicksort
        pivot = partition(arr, low, high)
        
        # Recursively sort left and right partitions
        _intro_sort_recursive(arr, low, pivot - 1, max_depth - 1)
        _intro_sort_recursive(arr, pivot + 1, high, max_depth - 1)
    
    # Start recursive intro sort
    _intro_sort_recursive(arr, 0, len(arr) - 1, max_depth)
    
    return arr