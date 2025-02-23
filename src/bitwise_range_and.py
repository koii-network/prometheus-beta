def bitwise_and_range(start: int, end: int) -> int:
    """
    Compute the bitwise AND of all numbers in the given range (inclusive).

    This function performs a bitwise AND operation on all numbers from start to end.
    It efficiently handles the computation by finding the common bits in the binary 
    representation of all numbers in the range.

    Args:
        start (int): The start of the range (inclusive)
        end (int): The end of the range (inclusive)

    Returns:
        int: The result of bitwise AND of all numbers in the range

    Raises:
        ValueError: If start is greater than end or if either number is negative

    Examples:
        >>> bitwise_and_range(5, 7)
        4
        >>> bitwise_and_range(10, 10)
        10
    """
    # Validate input
    if start < 0 or end < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    
    # If start and end are the same, return the number itself
    if start == end:
        return start
    
    # Find the number of bits to shift to get the common prefix
    shift = 0
    while start != end:
        start >>= 1
        end >>= 1
        shift += 1
    
    # Shift back and add zeros to the right
    return start << shift