def return_odd_numbers(input_array):
    """
    Returns a list of only odd numbers from the input array.
    
    Args:
        input_array (list): A list of integers
    
    Returns:
        list: A list containing only the odd numbers from the input array
    """
    return [num for num in input_array if num % 2 != 0]