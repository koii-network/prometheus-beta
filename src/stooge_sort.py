def stooge_sort(arr):
    """
    Implement the Stooge Sort algorithm.
    
    Stooge sort is a recursive sorting algorithm with a time complexity of O(n^(log 3 / log 1.5)).
    It works by recursively sorting the first 2/3 of the list, then the last 2/3 of the list, 
    and then the first 2/3 again.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list.
    """
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    # Base cases
    if len(arr) <= 1:
        return arr
    
    # If the first element is larger than the last, swap them
    if arr[0] > arr[-1]:
        arr[0], arr[-1] = arr[-1], arr[0]
    
    # If length is greater than 2, recursively sort
    if len(arr) > 2:
        t = len(arr) // 3
        
        # Recursively sort the first 2/3
        arr[:2*t] = stooge_sort(arr[:2*t])
        
        # Recursively sort the last 2/3
        arr[t:] = stooge_sort(arr[t:])
        
        # Recursively sort the first 2/3 again
        arr[:2*t] = stooge_sort(arr[:2*t])
    
    return arr