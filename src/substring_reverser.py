def reverse_substring(string: str, start: int, end: int) -> str:
    """
    Reverse a specific substring within a given string without using built-in reverse methods.
    
    Args:
        string (str): The original input string
        start (int): The starting index of the substring to reverse (inclusive)
        end (int): The ending index of the substring to reverse (exclusive)
    
    Returns:
        str: A new string with the specified substring reversed
    
    Raises:
        ValueError: If start or end indices are invalid
    """
    # Validate input indices
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    if start < 0 or end < 0:
        raise ValueError("Indices must be non-negative")
    
    # Handle empty string as a special case
    if len(string) == 0 and start == 0 and end == 0:
        return ""
    
    if start >= end or end > len(string):
        raise ValueError("Invalid substring indices")
    
    # Convert string to list for manipulation
    chars = list(string)
    
    # Reverse the specified substring in-place
    left, right = start, end - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    # Convert back to string
    return ''.join(chars)