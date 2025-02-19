def sum_integers(numbers):
    """
    Calculate the sum of integers in a list using only one loop.
    
    Args:
        numbers (list): A list of integers to be summed.
    
    Returns:
        int: The sum of all integers in the list.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    total = 0
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
        total += num
    
    return total