def multiply_digit_arrays(A, B):
    """
    Multiply two arrays of digits representing numbers.
    
    Args:
        A (list): First array of digits
        B (list): Second array of digits of same length as A
    
    Returns:
        list: Result of multiplication as an array of digits
    
    Raises:
        ValueError: If input arrays are not of equal length or contain non-integer values
    """
    # Input validation
    if len(A) != len(B):
        raise ValueError("Input arrays must be of equal length")
    
    if not all(isinstance(x, int) and 0 <= x <= 9 for x in A + B):
        raise ValueError("All elements must be single digits (0-9)")
    
    # Convert arrays to integers
    num_a = int(''.join(map(str, A)))
    num_b = int(''.join(map(str, B)))
    
    # Multiply and convert back to array of digits
    result = num_a * num_b
    return [int(digit) for digit in str(result)]