def find_missing_numbers(arr):
    """
    Find all missing numbers between the smallest and largest numbers in a sorted array.
    
    Args:
        arr (list): A sorted list of integers
    
    Returns:
        list: A list of missing numbers between the smallest and largest elements
    
    Raises:
        ValueError: If the input array is empty
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Find the smallest and largest numbers
    start = arr[0]
    end = arr[-1]
    
    # Create a set of the input array for efficient lookup
    arr_set = set(arr)
    
    # Find missing numbers
    missing_numbers = [
        num for num in range(start + 1, end) 
        if num not in arr_set
    ]
    
    return missing_numbers