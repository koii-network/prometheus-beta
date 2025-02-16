def rabin_karp_search(text, pattern):
    """
    Implement Rabin-Karp algorithm for string matching.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices of all occurrences of the pattern in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If pattern is empty
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        raise ValueError("Pattern cannot be empty")
    
    # If pattern is longer than text, no match is possible
    if len(pattern) > len(text):
        return []
    
    # Prime number for hashing
    prime = 101
    
    # Base for rolling hash
    base = 256
    
    # Store results
    results = []
    
    # Lengths of text and pattern
    n, m = len(text), len(pattern)
    
    # Calculate hash values
    pattern_hash = 0
    text_hash = 0
    
    # Compute base^(m-1) for rolling hash
    h = 1
    for _ in range(m - 1):
        h = (h * base) % prime
    
    # Compute initial hash values
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime
    
    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # If hash values match, check character by character
        if pattern_hash == text_hash:
            # Verify match
            if text[i:i+m] == pattern:
                results.append(i)
        
        # Compute hash for next window of text
        if i < n - m:
            # Remove leading digit, add trailing digit
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i+m])) % prime
            
            # Convert negative hash to positive
            if text_hash < 0:
                text_hash += prime
    
    return results