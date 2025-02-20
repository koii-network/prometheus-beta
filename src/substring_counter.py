def count_substring_occurrences(main_string: str, substring: str) -> int:
    """
    Count the number of times a substring occurs in a given string.
    
    Uses the KMP algorithm to achieve O(n) time complexity.
    
    Args:
        main_string (str): The string to search in
        substring (str): The substring to count occurrences of
    
    Returns:
        int: Number of times the substring appears in the main string
    
    Raises:
        ValueError: If either input is None or substring is empty
    """
    # Input validation
    if main_string is None or substring is None:
        raise ValueError("Inputs cannot be None")
    
    if not substring:
        raise ValueError("Substring cannot be empty")
    
    # If substring is longer than main string, no occurrences possible
    if len(substring) > len(main_string):
        return 0
    
    # Compute the Longest Prefix Suffix (LPS) array
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
    
    # Compute LPS array for the substring
    lps = compute_lps(substring)
    
    # KMP search to count occurrences
    count = 0
    i = 0  # index for main_string
    j = 0  # index for substring
    
    while i < len(main_string):
        if substring[j] == main_string[i]:
            i += 1
            j += 1
        
        if j == len(substring):
            count += 1
            # Move j back using LPS to continue searching for overlapping matches
            j = lps[j-1]
        
        # Mismatch after some matches
        elif i < len(main_string) and substring[j] != main_string[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    
    return count