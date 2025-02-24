def heapify(arr, n, i):
    """
    Heapify a subtree rooted at index i.
    
    Args:
        arr (list): The list to be heapified
        n (int): Size of the heap
        i (int): Index of the root of the subtree
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Implement Heap Sort algorithm.
    
    Args:
        arr (list): The list to be sorted
    
    Returns:
        list: Sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-comparable elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Check if all elements are comparable
    try:
        if len(arr) > 1:
            max(arr)
    except TypeError:
        raise ValueError("List contains non-comparable elements")

    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Heapify the reduced heap
        heapify(arr, i, 0)

    return arr