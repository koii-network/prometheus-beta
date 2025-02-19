def filter_odd_integers(numbers):
    """
    Given a list of integers, return a new list containing only the odd integers,
    sorted in ascending order.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        list: A sorted list of odd integers from the input list
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Filter odd integers and sort them
    return sorted([num for num in numbers if num % 2 != 0])