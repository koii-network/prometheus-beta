def sum_of_squares(numbers):
    """
    Calculate the sum of squares of numbers in an array.
    
    Args:
        numbers (list): A list of numbers to calculate sum of squares.
    
    Returns:
        int/float: The sum of squares of the input numbers.
    
    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    try:
        return sum(num ** 2 for num in numbers)
    except TypeError:
        raise TypeError("All elements in the list must be numeric")