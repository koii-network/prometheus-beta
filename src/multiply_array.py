def multiply(arrays):
    """
    Takes a list of lists of numbers and returns a new list 
    where each element is the product of corresponding elements.
    
    Args:
        arrays (list of lists): A list containing multiple lists of numbers
    
    Returns:
        list: A new list with multiplied values
    
    Raises:
        ValueError: If the input is not a list of lists or lists have different lengths
    """
    # Check if input is a list of lists
    if not isinstance(arrays, list) or not all(isinstance(arr, list) for arr in arrays):
        raise ValueError("Input must be a list of lists")
    
    # Check if all input lists have the same length
    if len(set(len(arr) for arr in arrays)) > 1:
        raise ValueError("All input lists must have the same length")
    
    # If input is empty, return an empty list
    if not arrays:
        return []
    
    # Multiply corresponding elements
    return [
        # Multiply all elements at the same index across all input lists
        multiply_elements(lists_at_index) 
        for lists_at_index in zip(*arrays)
    ]

def multiply_elements(numbers):
    """
    Multiply all numbers in a list together.
    
    Args:
        numbers (list): A list of numbers to multiply
    
    Returns:
        float or int: The product of all numbers
    """
    # Use built-in prod() from math module to multiply all elements
    from math import prod
    return prod(numbers)