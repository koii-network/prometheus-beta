def transform_array(arr):
    """
    Transform an array of non-negative integers based on specific rules:
    - 0 remains 0
    - Non-zero elements are transformed to their square plus 1
    
    Args:
        arr (list): Input array of non-negative integers
    
    Returns:
        list: Transformed array according to the specified rules
    
    Raises:
        ValueError: If the input contains negative numbers
    """
    if not all(isinstance(x, int) and x >= 0 for x in arr):
        raise ValueError("Input must be an array of non-negative integers")
    
    return [0 if x == 0 else x**2 + 1 for x in arr]