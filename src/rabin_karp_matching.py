def rabin_karp_search(text, pattern, prime=101):
    """
    Implement Rabin-Karp string matching algorithm.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
        prime (int, optional): Prime number used for hash calculation. Defaults to 101.
    
    Returns:
        list: List of starting indices where the pattern is found in the text
    """
    # Input validation
    if not text or not pattern:
        return []
    
    # Length of text and pattern
    n, m = len(text), len(pattern)
    
    # If pattern is longer than text, it can't be found
    if m > n:
        return []
    
    # Hash values for pattern and current text window
    pattern_hash = 0
    text_hash = 0
    
    # Base value for rolling hash
    base = 256
    
    # Compute the hash of the pattern and the first window of text
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime
    
    # Compute the highest power of base for rolling hash
    h = pow(base, m - 1) % prime
    
    # Store found indices
    found_indices = []
    
    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check if current window hash matches pattern hash
        if pattern_hash == text_hash:
            # Perform character by character matching
            if text[i:i+m] == pattern:
                found_indices.append(i)
        
        # Compute hash for next window
        if i < n - m:
            # Remove leading character, add trailing character
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            
            # Ensure positive hash value
            if text_hash < 0:
                text_hash += prime
    
    return found_indices