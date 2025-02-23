def find_duplicates(numbers):
    """
    Find and return a list of duplicate integers in the input list.

    Args:
        numbers (list): A list of integers to search for duplicates.

    Returns:
        list: A list of integers that appear more than once in the input list.
        
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate list contains only integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("List must contain only integers")
    
    # Use a dictionary to track occurrence count
    occurrence_count = {}
    
    # Count occurrences of each number
    for num in numbers:
        occurrence_count[num] = occurrence_count.get(num, 0) + 1
    
    # Return list of numbers that appear more than once
    return [num for num, count in occurrence_count.items() if count > 1]