def reverse_list(input_list):
    """
    Reverse a list of integers without using built-in list manipulation functions.
    
    Args:
        input_list (list): A list of integers to be reversed
    
    Returns:
        list: A new list with elements in reverse order
    """
    # Create a new list to store reversed elements
    reversed_list = []
    
    # Iterate through the input list from the end to the beginning
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    
    return reversed_list