def filter_odd_numbers(input_array):
    """
    Returns a list of only odd numbers from the input array.

    Args:
        input_array (list): A list of integers to filter.

    Returns:
        list: A list containing only the odd numbers from the input array.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Check if input is a list
    if not isinstance(input_array, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(num, int) for num in input_array):
        raise TypeError("All elements must be integers")
    
    # Filter and return only odd numbers
    return [num for num in input_array if num % 2 != 0]