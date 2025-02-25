def find_missing_numbers(arr):
    """
    Find all missing numbers between the smallest and largest numbers in a sorted array.
    
    Args:
        arr (list[int]): A sorted list of integers in ascending order.
    
    Returns:
        list[int]: A list of all missing numbers between the smallest and largest numbers.
    
    Raises:
        ValueError: If the input array is empty or None.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Check for invalid input
    if arr is None:
        raise ValueError("Input array cannot be None")
    
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Validate input is a list of integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("Input must be a list of integers")
    
    # If the array has only one element, return an empty list
    if len(arr) == 1:
        return []
    
    # Find missing numbers between the smallest and largest numbers
    missing_numbers = []
    for num in range(arr[0] + 1, arr[-1]):
        if num not in arr:
            missing_numbers.append(num)
    
    return missing_numbers