def filter_odd_numbers(numbers):
    """
    Returns a list of only odd numbers from the input array.
    
    Args:
        numbers (list): Input list of numbers
    
    Returns:
        list: A list containing only the odd numbers from the input
    """
    # Check if input is None or not a list
    if numbers is None:
        return []
    
    # Return only odd numbers using list comprehension
    return [num for num in numbers if isinstance(num, int) and num % 2 != 0]