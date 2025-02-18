def rabin_karp_search(text, pattern, prime=101):
    """
    Implement Rabin-Karp algorithm for string matching.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
        prime (int, optional): A prime number used for hashing. Defaults to 101.
    
    Returns:
        list: A list of starting indices where the pattern is found in the text
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        return []
    
    # Length of text and pattern
    n, m = len(text), len(pattern)
    
    # If pattern is longer than text, it can't be found
    if m > n:
        return []
    
    # Base value for the rightmost position
    d = 256  # number of characters in the input alphabet
    
    # Compute hash values for pattern and first window of text
    pattern_hash = 0
    text_hash = 0
    h = 1
    
    # h = d^(m-1) % prime
    for _ in range(m - 1):
        h = (h * d) % prime
    
    # Compute initial hash values
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % prime
        text_hash = (d * text_hash + ord(text[i])) % prime
    
    # Find matches
    results = []
    for i in range(n - m + 1):
        # If hash values match, check characters
        if pattern_hash == text_hash:
            # Check each character to confirm match
            if text[i:i+m] == pattern:
                results.append(i)
        
        # Compute hash for next window
        if i < n - m:
            # Remove leading digit, add trailing digit
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            
            # Ensure positive hash value
            if text_hash < 0:
                text_hash += prime
    
    return results