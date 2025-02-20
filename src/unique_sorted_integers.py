def get_unique_sorted_integers(numbers):
    """
    Returns a list of unique integers from the input, sorted in ascending order.
    
    Args:
        numbers (list): A list of integers that may contain duplicates.
    
    Returns:
        list: A sorted list of unique integers.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Remove duplicates and sort
    return sorted(set(numbers))