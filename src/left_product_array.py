def calculate_left_product_array(arr):
    """
    Calculate an array where each element is the product of numbers to its left.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Array where each element is the product of numbers to its left
    
    Examples:
        >>> calculate_left_product_array([1, 2, 3, 4])
        [1, 1, 2, 6]
        >>> calculate_left_product_array([3, 1, 2, 5])
        [1, 3, 3, 6]
    """
    if not arr:
        return []
    
    # Initialize result array with first element as 1
    result = [1] * len(arr)
    
    # Calculate cumulative product from left to right
    for i in range(1, len(arr)):
        result[i] = result[i-1] * arr[i-1]
    
    return result