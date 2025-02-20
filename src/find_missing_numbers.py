def find_missing_numbers(arr):
    """
    Find all missing numbers between the smallest and largest numbers in a sorted array.
    
    Args:
        arr (list): A sorted list of integers.
    
    Returns:
        list: A list of missing numbers between the smallest and largest values.
    
    Raises:
        ValueError: If the input array is empty.
    """
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Get the smallest and largest numbers in the array
    smallest = arr[0]
    largest = arr[-1]
    
    # Create a set of the input array for efficient lookup
    num_set = set(arr)
    
    # Find missing numbers
    missing_numbers = [
        num for num in range(smallest + 1, largest) 
        if num not in num_set
    ]
    
    return missing_numbers