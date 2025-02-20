def find_duplicates(numbers):
    """
    Find and return a list of duplicate integers from the input list.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        list: A list of integers that appear more than once in the input list
    """
    # Use a set to track duplicates efficiently
    seen = set()
    duplicates = set()
    
    for num in numbers:
        # If the number is already in seen, it's a duplicate
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    # Convert duplicates set to a sorted list for consistent output
    return sorted(list(duplicates))