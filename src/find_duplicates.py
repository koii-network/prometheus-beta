def find_duplicates(numbers):
    """
    Find and return a list of duplicate integers in the input list.
    
    Args:
        numbers (list): A list of integers to check for duplicates.
    
    Returns:
        list: A list of integers that appear more than once in the input list.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Use a set to track duplicates efficiently
    seen = set()
    duplicates = set()
    
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    # Convert duplicates set to a sorted list for consistent output
    return sorted(list(duplicates))