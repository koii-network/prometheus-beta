def bitwise_and_range(start, end):
    """
    Compute the bitwise AND of all numbers in the given range (inclusive).
    
    Args:
        start (int): The start of the range (inclusive)
        end (int): The end of the range (inclusive)
    
    Returns:
        int: The result of bitwise AND of all numbers in the range
    
    Raises:
        ValueError: If start is greater than end or if either number is negative
    """
    if start < 0 or end < 0:
        raise ValueError("Range numbers must be non-negative")
    
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    
    result = start
    for num in range(start + 1, end + 1):
        result &= num
    
    return result