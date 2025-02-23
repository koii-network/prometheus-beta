def reverse_substring(string: str, start: int, end: int) -> str:
    """
    Reverse a substring within a given string.

    Args:
        string (str): The original input string.
        start (int): The starting index of the substring to reverse (inclusive).
        end (int): The ending index of the substring to reverse (exclusive).

    Returns:
        str: A new string with the specified substring reversed.

    Raises:
        ValueError: If start or end indices are out of bounds.
        TypeError: If inputs are not of the expected types.
    """
    # Type checking
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end indices must be integers")
    
    # Validate index bounds
    if start < 0 or end > len(string) or start > end:
        raise ValueError("Invalid substring indices")
    
    # Convert string to list for easy manipulation
    chars = list(string)
    
    # Reverse the substring in-place
    while start < end - 1:
        chars[start], chars[end - 1] = chars[end - 1], chars[start]
        start += 1
        end -= 1
    
    # Convert back to string and return
    return ''.join(chars)