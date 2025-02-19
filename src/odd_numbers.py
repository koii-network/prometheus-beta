def extract_odd_numbers(numbers):
    """
    Returns a list of only odd numbers from the input array.
    
    Args:
        numbers (list): A list of integers
    
    Returns:
        list: A list containing only the odd numbers from the input
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Return only odd numbers using list comprehension
    return [num for num in numbers if num % 2 != 0]