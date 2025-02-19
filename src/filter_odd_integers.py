def filter_odd_integers(numbers):
    """
    Given a list of integers, return a new list containing only the odd integers 
    sorted in ascending order.
    
    Args:
        numbers (list): List of integers to filter
    
    Returns:
        list: Sorted list of odd integers from the input list
    """
    # Filter out odd integers and sort them in ascending order
    return sorted([num for num in numbers if num % 2 != 0])