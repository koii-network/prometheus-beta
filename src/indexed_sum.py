def calculate_sum(my_list):
    """
    Calculate the sum of numbers in the list, where each number is multiplied by its index.
    
    Args:
        my_list (list): A list of integers to process
    
    Returns:
        int: The sum of each number multiplied by its index
    """
    if not isinstance(my_list, list):
        raise TypeError("Input must be a list")
    
    return sum(num * index for index, num in enumerate(my_list))