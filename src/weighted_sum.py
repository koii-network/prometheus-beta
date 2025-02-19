def calculate_sum(my_list):
    """
    Calculate the sum of numbers in the list, where each number is multiplied by its index.
    
    Args:
        my_list (list): A list of integers
    
    Returns:
        int: The weighted sum of the list
    """
    # Use enumerate to get both index and value, multiply and sum
    return sum(num * index for index, num in enumerate(my_list))