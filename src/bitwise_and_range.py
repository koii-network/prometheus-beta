def bitwise_and_range(start, end):
    """
    Compute the bitwise AND of all numbers in a given range (inclusive).
    
    Args:
        start (int): The start of the range (inclusive)
        end (int): The end of the range (inclusive)
    
    Returns:
        int: The bitwise AND of all numbers in the range
    
    Raises:
        ValueError: If start is greater than end
        TypeError: If inputs are not integers
    """
    # Validate inputs
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Inputs must be integers")
    
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    
    # Edge case: Single number
    if start == end:
        return start
    
    # Bitwise AND operation
    result = start
    for num in range(start + 1, end + 1):
        result &= num
    
    return result