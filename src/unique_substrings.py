def get_unique_substrings(s: str) -> list:
    """
    Returns an array of all unique substrings within the input string.
    
    Args:
        s (str): The input string to find unique substrings in.
    
    Returns:
        list: A list of unique substrings in the order they are discovered.
    
    Examples:
        >>> get_unique_substrings("abc")
        ['a', 'ab', 'abc', 'b', 'bc', 'c']
        >>> get_unique_substrings("")
        []
    """
    if not s:
        return []
    
    unique_substrings = set()
    
    # Generate all possible substrings
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            unique_substrings.add(s[start:end])
    
    # Convert set to list while preserving order of first occurrence
    result = []
    seen = set()
    for substring in s:
        for end in range(1, len(s) + 1):
            current = s[substring:end]
            if current not in seen:
                result.append(current)
                seen.add(current)
    
    return result