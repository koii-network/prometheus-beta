def filter_exclusive_multiples(numbers):
    """
    Filter a list of integers to include only numbers that are multiples 
    of either 3 or 5, but not both.

    Args:
        numbers (list): A list of integers to filter.

    Returns:
        list: A sorted list of integers that are multiples of 3 or 5, 
              but not both.

    Examples:
        >>> filter_exclusive_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        [5, 6, 7, 9, 10]
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Filter numbers that are multiples of 3 XOR 5 (exclusive or)
    exclusive_multiples = [
        num for num in numbers 
        if (num % 3 == 0) != (num % 5 == 0)
    ]
    
    # Return sorted list
    return sorted(exclusive_multiples)