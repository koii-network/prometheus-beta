def find_missing_numbers(arr):
    """
    Find all missing numbers between the smallest and largest numbers in a sorted array.
    
    Args:
        arr (list): A sorted list of integers
    
    Returns:
        list: A list of missing numbers between the minimum and maximum of the input array
    
    Raises:
        ValueError: If the input array is empty
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Find the minimum and maximum numbers in the array
    min_num = arr[0]
    max_num = arr[-1]
    
    # Create a set of the input array for efficient lookup
    num_set = set(arr)
    
    # Find missing numbers
    missing_numbers = [
        num for num in range(min_num + 1, max_num) 
        if num not in num_set
    ]
    
    return missing_numbers