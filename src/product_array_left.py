def product_array_left(arr):
    """
    Create an array where each element is the product of numbers to its left in the original array.
    
    Args:
        arr (list): Input list of numbers
    
    Returns:
        list: Array with products of left elements
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-numeric elements
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("All elements must be numeric")
    
    # Special case for empty or single-element list
    if len(arr) <= 1:
        return [1]
    
    # Initialize result array
    result = [1] * len(arr)
    
    # Calculate cumulative product of left elements
    for i in range(1, len(arr)):
        result[i] = result[i-1] * arr[i-1]
    
    return result