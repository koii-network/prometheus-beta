def calculate_sum(my_list):
    """
    Calculate the sum of numbers in a list, where each number is multiplied by its index.
    
    Args:
        my_list (list): A list of integers
    
    Returns:
        int: The sum of each number multiplied by its index
    """
    return sum(num * index for index, num in enumerate(my_list))