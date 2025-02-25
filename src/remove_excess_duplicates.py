def remove_excess_duplicates(input_string):
    """
    Remove characters that appear more than twice in the input string.

    Args:
        input_string (str): The input string to process.

    Returns:
        str: A string with characters appearing more than twice reduced to two occurrences.

    Examples:
        >>> remove_excess_duplicates("aabbbcccc")
        "aabbcc"
        >>> remove_excess_duplicates("hello")
        "hello"
        >>> remove_excess_duplicates("")
        ""
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If string is empty or too short to have excess duplicates, return as-is
    if len(input_string) <= 2:
        return input_string
    
    # Count character occurrences
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Build result string, keeping only up to two occurrences of each character
    result = []
    char_tracker = {}
    
    for char in input_string:
        # If character hasn't been tracked or is below 2 occurrences
        if char not in char_tracker or char_tracker[char] < 2:
            result.append(char)
            char_tracker[char] = char_tracker.get(char, 0) + 1
    
    return ''.join(result)