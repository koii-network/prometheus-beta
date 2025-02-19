def extract_odd_integers(numbers):
    """
    Extract odd integers from a given list and return them sorted in ascending order.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        list: A sorted list of odd integers from the input list
    """
    return sorted([num for num in numbers if num % 2 != 0])