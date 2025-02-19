def multiply_digit_arrays(A, B):
    """
    Multiply two arrays of digits representing numbers.
    
    Args:
        A (list): First array of digits 
        B (list): Second array of digits of the same length as A
    
    Returns:
        list: Result of multiplying the numbers, represented as an array of digits
    
    Raises:
        ValueError: If input arrays are not of equal length or contain non-digit values
    """
    # Validate input
    if len(A) != len(B):
        raise ValueError("Input arrays must be of equal length")
    
    # Check that all elements are digits
    if not all(isinstance(x, int) and 0 <= x <= 9 for x in A + B):
        raise ValueError("All elements must be single digits between 0 and 9")
    
    # Convert arrays to integers
    num_a = int(''.join(map(str, A)))
    num_b = int(''.join(map(str, B)))
    
    # Multiply and convert result back to array of digits
    result = num_a * num_b
    
    # Convert result to array of digits
    return [int(digit) for digit in str(result)]