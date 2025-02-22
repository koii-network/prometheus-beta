def heap_sort(arr):
    """
    Implement the Heap Sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains elements that cannot be compared.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    def heapify(arr, n, i):
        """
        Heapify a subtree rooted at index i.
        
        Args:
            arr (list): The list to heapify
            n (int): Size of the heap
            i (int): Root index of the subtree
        """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        # See if left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        # See if right child exists and is greater than largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        # Change root if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            
            # Heapify the affected sub-tree
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