def heapify(arr, n, i):
    """
    Heapify a subtree rooted at index i.
    
    Args:
        arr (list): The list to be heapified
        n (int): Size of the heap
        i (int): Root index of the subtree to heapify
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Perform Heap Sort on the input list.
    
    Args:
        arr (list): The list to be sorted
    
    Returns:
        list: The sorted list
    """
    # Handle empty or single-element lists
    if not arr or len(arr) <= 1:
        return arr.copy()

    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Heapify the reduced heap
        heapify(arr, i, 0)

    return arr