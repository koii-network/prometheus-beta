def filter_odd_integers(numbers):
    """
    Given a list of integers, return a new list containing only the odd integers,
    sorted in ascending order.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        list: A sorted list of odd integers from the input list
    """
    # Filter odd integers and sort them
    return sorted([num for num in numbers if num % 2 != 0])