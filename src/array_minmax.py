def find_highest_lowest(numbers):
    """
    Find the highest and lowest numbers in an input array.
    
    Args:
        numbers (list): A list of numbers
    
    Returns:
        tuple: A tuple containing the lowest and highest numbers in the array
    
    Raises:
        ValueError: If the input array is empty
        TypeError: If the input contains non-numeric values
    """
    # Check if the input is empty
    if not numbers:
        raise ValueError("Input array cannot be empty")
    
    # Check if all elements are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numeric")
    
    # Return a tuple with lowest and highest numbers
    return (min(numbers), max(numbers))