def reverse_substring(s: str, start: int, end: int) -> str:
    """
    Reverse a substring of a given string between start and end indices (inclusive).
    
    Args:
        s (str): The input string
        start (int): Starting index of the substring to reverse (0-based)
        end (int): Ending index of the substring to reverse (0-based)
    
    Returns:
        str: A new string with the specified substring reversed
    
    Raises:
        ValueError: If start or end indices are invalid
    """
    # Validate input indices
    if start < 0 or end < 0:
        raise ValueError("Start and end indices must be non-negative")
    
    if start > end:
        raise ValueError("Start index must be less than or equal to end index")
    
    if start >= len(s) or end >= len(s):
        raise ValueError("Indices out of string bounds")
    
    # Convert string to list for easy manipulation
    chars = list(s)
    
    # Reverse the substring in-place
    while start < end:
        chars[start], chars[end] = chars[end], chars[start]
        start += 1
        end -= 1
    
    # Convert back to string and return
    return ''.join(chars)