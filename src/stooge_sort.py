def stooge_sort(arr):
    """
    Implement the Stooge Sort algorithm.
    
    Stooge sort is a recursive sorting algorithm with a time complexity of O(n^(log 3 / log 1.5)) ≈ O(n^2.7095).
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If the input is not a list
    """
    # Create a copy to avoid modifying the original list
    arr = list(arr)
    
    # If arr has less than 2 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # If first element is larger than last, swap them
    if arr[0] > arr[-1]:
        arr[0], arr[-1] = arr[-1], arr[0]
    
    # If length is greater than 2, recursively sort
    if len(arr) > 2:
        t = len(arr) // 3
        
        # Recursively sort first 2/3
        arr[:2*t] = stooge_sort(arr[:2*t])
        
        # Recursively sort last 2/3
        arr[t:] = stooge_sort(arr[t:])
        
        # Recursively sort first 2/3 again
        arr[:2*t] = stooge_sort(arr[:2*t])
    
    return arr