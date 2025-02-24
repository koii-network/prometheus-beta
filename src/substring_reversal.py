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
    
    # Validate index ranges and empty string
    if len(s) == 0 or start < 0 or end > len(s) or start > end:
        raise ValueError("Invalid substring indices")
    
    # Handle case when start equals end (no reversal needed)
    if start == end:
        return s
    
    # Split the string 
    prefix = s[:start]    # Before the substring
    substring = s[start:end]  # Part to reverse
    suffix = s[end:]      # After the substring
    
    # Reverse the substring manually
    reversed_substring = ''.join(
        substring[i] for i in range(len(substring) - 1, -1, -1)
    )
    
    # Combine the parts
    return prefix + reversed_substring + suffix