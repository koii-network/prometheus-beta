def multiply(arr):
    """
    Takes an array of numbers and returns a new array where each element 
    is the result of multiplying the corresponding elements from the original array.
    
    Args:
        arr (list): A list of numbers to multiply.
    
    Returns:
        list: A new list with multiplied elements.
    
    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are numbers (int or float)
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Return a new list with multiplied elements
    return [x * x for x in arr]