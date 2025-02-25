def sum_of_squares(numbers):
    """
    Calculate the sum of squares for a given array of numbers.

    Args:
        numbers (list): A list of numbers to calculate sum of squares.

    Returns:
        int or float: The sum of squares of the input numbers.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numeric")
    
    # Calculate sum of squares
    return sum(x**2 for x in numbers)