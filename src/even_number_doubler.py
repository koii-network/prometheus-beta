def double_even_numbers(numbers):
    """
    Takes an array of numbers and returns a new array with even numbers multiplied by 2.
    
    Args:
        numbers (list): Input list of numbers
    
    Returns:
        list: New list with even numbers doubled, odd numbers unchanged
    
    Raises:
        TypeError: If input is not a list or contains non-numeric elements
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numeric")
    
    return [num * 2 if num % 2 == 0 else num for num in numbers]