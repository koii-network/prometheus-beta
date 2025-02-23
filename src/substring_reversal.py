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
    
    # First part of the string before reversal
    prefix = string[:start]
    
    # Substring to be reversed
    substring = string[start:end]
    
    # Reversed substring
    reversed_substring = substring[::-1]
    
    # Last part of the string after reversal
    suffix = string[end:]
    
    # Combine and return
    return prefix + reversed_substring + suffix