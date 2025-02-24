def reverse_substring(s: str, start: int, end: int) -> str:
    """
    Reverse a specific substring within a given string without using built-in reverse methods.
    
    Args:
        s (str): The input string
        start (int): The starting index of the substring to reverse (inclusive)
        end (int): The ending index of the substring to reverse (exclusive)
    
    Returns:
        str: A new string with the specified substring reversed
    
    Raises:
        ValueError: If start or end indices are invalid
        TypeError: If input is not a string or indices are not integers
    """
    # Validate input types
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end indices must be integers")
    
    # Validate index ranges
    if start < 0 or end > len(s) or start > end:
        raise ValueError("Invalid substring indices")
    
    # Handle case when start equals end (no reversal needed)
    if start == end:
        return s
    
    # Convert string to list for manipulation
    chars = list(s)
    
    # Reverse the substring in-place
    left, right = start, end - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    # Convert back to string
    return ''.join(chars)