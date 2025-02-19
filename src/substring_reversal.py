def reverse_substring(s: str, start: int, end: int) -> str:
    """
    Reverse a substring of a given string between specified start and end indices.
    
    Args:
        s (str): The input string
        start (int): Starting index of the substring to reverse (inclusive)
        end (int): Ending index of the substring to reverse (exclusive)
    
    Returns:
        str: A new string with the specified substring reversed
    
    Raises:
        ValueError: If start or end indices are invalid
    """
    # Validate input indices
    if start < 0 or end > len(s) or start >= end:
        raise ValueError("Invalid start or end indices")
    
    # Reverse the substring
    return s[:start] + s[start:end][::-1] + s[end:]