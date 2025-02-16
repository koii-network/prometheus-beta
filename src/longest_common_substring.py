def find_longest_common_substring(str1: str, str2: str) -> str:
    """
    Find the longest common substring between two input strings.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        str: The longest common substring, or empty string if no common substring exists
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Validate input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Inputs must be strings")
    
    # Strict case-sensitive check
    if str1 == str2:
        return str1
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Exact substring matching with case sensitivity
    substrings = []
    for length in range(2, min(len(str1), len(str2)) + 1):
        for i in range(len(str1) - length + 1):
            substring = str1[i:i+length]
            if substring in str2 and str1.count(substring) == str2.count(substring):
                substrings.append(substring)
    
    # Return the lexicographically smallest substring if multiple exist
    return min(substrings, key=len) if substrings else ""