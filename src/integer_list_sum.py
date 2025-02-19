def sum_integers(numbers):
    """
    Calculate the sum of a list of integers using only one loop.
    
    Args:
        numbers (list): A list of integers to sum.
    
    Returns:
        int: The sum of all integers in the list.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Initialize total sum
    total = 0
    
    # Single loop to sum all integers
    for num in numbers:
        # Validate each element is an integer
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
        total += num
    
    return total