def count_substring_occurrences(string: str, substring: str) -> int:
    """
    Count the number of times a substring occurs in a given string.
    
    Uses the KMP (Knuth-Morris-Pratt) algorithm to achieve O(n) time complexity.
    
    Args:
        string (str): The main string to search in
        substring (str): The substring to search for
    
    Returns:
        int: Number of times the substring appears in the string
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If substring is an empty string
    """
    # Input validation
    if not isinstance(string, str) or not isinstance(substring, str):
        raise TypeError("Both string and substring must be strings")
    
    if not substring:
        raise ValueError("Substring cannot be empty")
    
    # If substring is longer than string, it can't occur
    if len(substring) > len(string):
        return 0
    
    # Compute the longest proper prefix which is also a suffix (LPS) array
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    # Compute LPS for the substring
    lps = compute_lps(substring)
    
    # KMP algorithm to count occurrences
    count = 0
    i = 0  # index for string
    j = 0  # index for substring
    
    while i < len(string):
        if substring[j] == string[i]:
            i += 1
            j += 1
        
        if j == len(substring):
            count += 1
            j = lps[j - 1]
        
        # Mismatch after some matches
        elif i < len(string) and substring[j] != string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return count