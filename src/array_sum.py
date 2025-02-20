def sum_array(numbers):
    """
    Calculate the sum of elements in an array of integers.
    
    Args:
        numbers (list): An array of integers to sum.
    
    Returns:
        int: The sum of all elements in the array.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Return the sum of the array
    return sum(numbers)