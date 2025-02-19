def reverse_substring(original_string, start_index, end_index):
    """
    Reverse a specific substring within a given string without using built-in reverse methods.
    
    Args:
        original_string (str): The original input string
        start_index (int): The starting index of the substring to reverse (inclusive)
        end_index (int): The ending index of the substring to reverse (inclusive)
    
    Returns:
        str: A new string with the specified substring reversed
    
    Raises:
        ValueError: If indices are out of bounds or invalid
    """
    # Validate input indices
    if not isinstance(original_string, str):
        raise TypeError("Input must be a string")
    
    if start_index < 0 or end_index < 0:
        raise ValueError("Indices must be non-negative")
    
    if start_index > end_index:
        raise ValueError("Start index must be less than or equal to end index")
    
    if end_index >= len(original_string):
        raise ValueError("End index is out of bounds")
    
    # Convert string to list for easier manipulation
    chars = list(original_string)
    
    # Reverse the substring in-place
    while start_index < end_index:
        chars[start_index], chars[end_index] = chars[end_index], chars[start_index]
        start_index += 1
        end_index -= 1
    
    # Convert back to string
    return ''.join(chars)