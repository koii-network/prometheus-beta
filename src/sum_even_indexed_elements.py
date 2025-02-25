def sum_even_indexed_elements(numbers):
    """
    Calculate the sum of elements at even indices in the given list.

    Args:
        numbers (list): A list of integers to process.

    Returns:
        int: Sum of elements at even indices (0, 2, 4, ...).
             Returns 0 if the list is empty.

    Examples:
        >>> sum_even_indexed_elements([1, 2, 3, 4, 5])
        9
        >>> sum_even_indexed_elements([-1, 10, 20, 30, 40])
        59
        >>> sum_even_indexed_elements([])
        0
    """
    # Handle empty list case
    if not numbers:
        return 0
    
    # Sum elements at even indices (0, 2, 4, ...)
    return sum(numbers[::2])