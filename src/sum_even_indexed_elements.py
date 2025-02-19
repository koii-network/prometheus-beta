def sum_even_indexed_elements(numbers):
    """
    Calculate the sum of elements at even indices in the given list.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        int: Sum of elements at even indices (0, 2, 4, ...). 
             Returns 0 if the list is empty.
    """
    # Return 0 for empty list
    if not numbers:
        return 0
    
    # Sum elements at even indices (0, 2, 4, ...)
    return sum(numbers[i] for i in range(0, len(numbers), 2))