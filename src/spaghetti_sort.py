def spaghetti_sort(arr):
    """
    Implement the spaghetti sort algorithm.
    
    Spaghetti sort (also known as Bogosort) is a highly inefficient sorting algorithm
    that works by randomly shuffling the list until it becomes sorted.
    
    Args:
    arr (list): The input list to be sorted
    
    Returns:
    list: A sorted version of the input list
    
    Raises:
    TypeError: If the input is not a list
    """
    import random
    
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If the list is empty or has only one element, it's already sorted
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    
    # Shuffle until sorted
    while not is_sorted(sorted_arr):
        random.shuffle(sorted_arr)
    
    return sorted_arr

def is_sorted(arr):
    """
    Check if the list is sorted in ascending order.
    
    Args:
    arr (list): The list to check
    
    Returns:
    bool: True if the list is sorted, False otherwise
    """
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))