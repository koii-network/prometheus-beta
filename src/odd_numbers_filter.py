def filter_odd_numbers(numbers):
    """
    Returns a list of only odd numbers from the input array.
    
    Args:
        numbers (list): An input list of numbers
    
    Returns:
        list: A list containing only the odd numbers from the input list
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    return [num for num in numbers if isinstance(num, (int, float)) and num % 2 != 0]