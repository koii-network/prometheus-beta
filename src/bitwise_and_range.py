def bitwise_and_range(start, end):
    """
    Compute the bitwise AND of all numbers in the given range (inclusive).
    
    Args:
        start (int): The start of the range (inclusive)
        end (int): The end of the range (inclusive)
    
    Returns:
        int: The bitwise AND result of all numbers in the range
    
    Raises:
        ValueError: If start is greater than end or if either start or end is negative
    """
    # Validate input
    if start < 0 or end < 0:
        raise ValueError("Start and end must be non-negative integers")
    
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    
    # If range is a single number, return that number
    if start == end:
        return start
    
    # Find the most significant bit position
    def find_msb(n):
        """Find the most significant bit position"""
        msb = 0
        while (1 << msb) <= n:
            msb += 1
        return msb - 1
    
    # If the range spans multiple numbers, we need to find common bits
    msb_start = find_msb(start)
    msb_end = find_msb(end)
    
    # If the most significant bits are different, result will be 0
    if msb_start != msb_end:
        return 0
    
    # Compute common prefix
    common_prefix = start & end
    mask = (1 << (msb_start + 1)) - 1
    return common_prefix & mask