def multiply_digit_arrays(A, B):
    """
    Multiply two arrays of digits representing numbers.
    
    Args:
        A (list): First array of digits
        B (list): Second array of digits of the same length
    
    Returns:
        list: Array of digits representing the multiplication result
    
    Raises:
        ValueError: If input arrays are not of equal length or contain non-digit values
    """
    # Input validation
    if len(A) != len(B):
        raise ValueError("Input arrays must be of equal length")
    
    # Check if all elements are valid digits
    if not all(isinstance(x, int) and 0 <= x <= 9 for x in A + B):
        raise ValueError("All elements must be single digits (0-9)")
    
    # Convert arrays to numbers
    num1 = int(''.join(map(str, A)))
    num2 = int(''.join(map(str, B)))
    
    # Multiply and convert result back to array of digits
    result = num1 * num2
    return [int(digit) for digit in str(result)]