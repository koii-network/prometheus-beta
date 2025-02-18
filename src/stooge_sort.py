def stooge_sort(arr):
    """
    Implement the Stooge Sort algorithm.
    
    Stooge sort is a recursive sorting algorithm with a time complexity of O(n^(log 3 / log 1.5)) = O(n^2.7095).
    
    Args:
        arr (list): The input list to be sorted in ascending order.
    
    Returns:
        list: A new sorted list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Create a copy of the input list to avoid modifying the original
    arr = list(arr)
    
    # Validate input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Base cases: if list has 0 or 1 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # If first element is larger than last, swap them
    if arr[0] > arr[-1]:
        arr[0], arr[-1] = arr[-1], arr[0]
    
    # If list has more than 2 elements, recursively sort
    if len(arr) > 2:
        t = len(arr) // 3
        
        # Recursively sort first 2/3
        arr[:len(arr)-t] = stooge_sort(arr[:len(arr)-t])
        
        # Recursively sort last 2/3
        arr[t:] = stooge_sort(arr[t:])
        
        # Recursively sort first 2/3 again
        arr[:len(arr)-t] = stooge_sort(arr[:len(arr)-t])
    
    return arr