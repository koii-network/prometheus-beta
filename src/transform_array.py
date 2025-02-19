def transform_integers(input_array):
    """
    Transform an array of non-negative integers based on specific rules:
    - 0 remains 0
    - Non-zero elements are transformed to their square plus 1
    
    Args:
        input_array (list): A list of non-negative integers
    
    Returns:
        list: A new list with transformed elements
    
    Raises:
        ValueError: If the input contains negative integers
    """
    # Validate input
    if not all(isinstance(x, int) and x >= 0 for x in input_array):
        raise ValueError("Input must be a list of non-negative integers")
    
    # Transform the array
    return [0 if x == 0 else x**2 + 1 for x in input_array]