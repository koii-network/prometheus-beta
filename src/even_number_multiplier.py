def multiply_even_numbers(numbers):
    """
    Take an array of numbers and return a new array with even numbers multiplied by 2.
    
    Args:
        numbers (list): A list of numbers to process
    
    Returns:
        list: A new list with even numbers multiplied by 2, odd numbers unchanged
    
    Raises:
        TypeError: If the input is not a list or contains non-numeric elements
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are numbers
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numeric")
    
    # Create a new list with even numbers multiplied by 2
    return [num * 2 if num % 2 == 0 else num for num in numbers]