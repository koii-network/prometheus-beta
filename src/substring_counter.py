def count_substring_occurrences(text: str, substring: str) -> int:
    """
    Count the number of non-overlapping occurrences of a substring in a given string.
    
    Args:
        text (str): The main string to search in.
        substring (str): The substring to count occurrences of.
    
    Returns:
        int: The number of times the substring appears in the text.
    
    Time Complexity: O(n), where n is the length of the input text.
    Space Complexity: O(1)
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If substring is an empty string.
    
    Examples:
        >>> count_substring_occurrences("hello hello world", "hello")
        2
        >>> count_substring_occurrences("aaaaa", "aa")
        2
    """
    # Special case: empty text and/or substring
    if text == "" and substring == "":
        return 0
    
    # Validate inputs
    if not isinstance(text, str) or not isinstance(substring, str):
        raise TypeError("Both text and substring must be strings")
    
    # Handle edge cases
    if not substring:
        raise ValueError("Substring cannot be empty")
    
    if len(substring) > len(text):
        return 0
    
    # Efficient O(n) substring counting using sliding window
    count = 0
    i = 0
    while i <= len(text) - len(substring):
        # Check if substring matches at current position
        if text[i:i+len(substring)] == substring:
            count += 1
            # Move past the current occurrence to avoid overlapping
            i += len(substring)
        else:
            # Move to next character if no match
            i += 1
    
    return count