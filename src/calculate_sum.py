def calculate_sum(my_list):
    """
    Calculate the sum of numbers in the list, where each number is multiplied by its index.
    
    Args:
        my_list (list): A list of integers
    
    Returns:
        int: The sum of numbers multiplied by their indices
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains non-integer elements
    """
    # Validate input is a list
    if not isinstance(my_list, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(x, int) for x in my_list):
        raise ValueError("All elements must be integers")
    
    # Calculate weighted sum
    return sum(num * index for index, num in enumerate(my_list))