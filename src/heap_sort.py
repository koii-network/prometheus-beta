def heap_sort(arr):
    """
    Implement Heap Sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If list contains non-comparable elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the input list to avoid modifying the original
    arr = arr.copy()
    
    def heapify(arr, n, i):
        """
        Maintain heap property for a subtree rooted at index i.
        
        Args:
            arr (list): The list being heapified
            n (int): Size of the heap
            i (int): Root index of the subtree
        """
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # Left child
        right = 2 * i + 2  # Right child
        
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
    
    # Build max heap
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Heapify the reduced heap
        heapify(arr, i, 0)
    
    return arr