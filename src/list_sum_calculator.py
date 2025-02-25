def calculate_sum(my_list):
    """
    Calculate the weighted sum of a list of integers by multiplying each 
    number by its index in the list.
    
    Args:
        my_list (list): A list of integers to be processed.
    
    Returns:
        int: The sum of each number multiplied by its index.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    # Check if input is a list
    if not isinstance(my_list, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in my_list):
        raise ValueError("All list elements must be integers")
    
    # Calculate weighted sum by multiplying each number by its index
    return sum(num * index for index, num in enumerate(my_list))