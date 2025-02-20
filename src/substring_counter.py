def count_substring_occurrences(main_string: str, substring: str) -> int:
    """
    Count the number of times a substring occurs in a given string.
    
    Uses the Knuth-Morris-Pratt (KMP) algorithm for O(n) time complexity.
    
    Args:
        main_string (str): The string to search in
        substring (str): The substring to count occurrences of
    
    Returns:
        int: Number of times the substring appears in the main string
    
    Raises:
        ValueError: If either input is empty
    """
    # Input validation
    if not main_string or not substring:
        raise ValueError("Both main_string and substring must be non-empty")
    
    # Compute the prefix function (longest proper prefix which is also a suffix)
    def compute_prefix_function(pattern):
        m = len(pattern)
        prefix = [0] * m
        length = 0
        i = 1
        
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                prefix[i] = length
                i += 1
            else:
                if length != 0:
                    length = prefix[length - 1]
                else:
                    prefix[i] = 0
                    i += 1
        
        return prefix
    
    # KMP substring counting
    substring_length = len(substring)
    main_string_length = len(main_string)
    
    # Compute prefix function for the substring
    prefix = compute_prefix_function(substring)
    
    # Count occurrences
    count = 0
    i = 0  # index for main_string
    j = 0  # index for substring
    
    while i < main_string_length:
        if substring[j] == main_string[i]:
            i += 1
            j += 1
        
        if j == substring_length:
            count += 1
            j = prefix[j - 1]
        
        # Mismatch after some matches
        elif i < main_string_length and substring[j] != main_string[i]:
            if j != 0:
                j = prefix[j - 1]
            else:
                i += 1
    
    return count