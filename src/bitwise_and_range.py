def bitwise_and_range(start: int, end: int) -> int:
    """
    Compute the bitwise AND of all numbers in the given range (inclusive).
    
    Args:
        start (int): The start of the range (inclusive)
        end (int): The end of the range (inclusive)
    
    Returns:
        int: The bitwise AND result of all numbers in the range
    
    Raises:
        ValueError: If start is greater than end or if either number is negative
    """
    # Validate input
    if start < 0 or end < 0:
        raise ValueError("Both start and end must be non-negative integers")
    
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    
    # If range is empty, return 0
    if start == end:
        return start
    
    # Find the common most significant bits
    result = start
    for num in range(start + 1, end + 1):
        result &= num
    
    return result