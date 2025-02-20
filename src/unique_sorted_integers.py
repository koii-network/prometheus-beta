def get_unique_sorted_integers(input_list):
    """
    Returns a unique and sorted list of integers.
    
    Args:
        input_list (list): A list of integers that may contain duplicates.
    
    Returns:
        list: A new list with unique integers, sorted in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Check if input is a list
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in input_list):
        raise TypeError("All elements must be integers")
    
    # Remove duplicates and sort
    return sorted(set(input_list))