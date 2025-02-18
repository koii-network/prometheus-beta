def rabin_karp_search(text, pattern, prime=101):
    """
    Implement Rabin-Karp string matching algorithm.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
        prime (int, optional): A prime number used for hashing. Defaults to 101.
    
    Returns:
        list: A list of starting indices where the pattern is found in the text
    """
    # Input validation
    if not text or not pattern:
        return []
    
    # Get lengths of text and pattern
    n, m = len(text), len(pattern)
    
    # If pattern is longer than text, it can't be found
    if m > n:
        return []
    
    # Initialize variables for hash values and results
    pattern_hash = 0
    text_hash = 0
    h = 1
    results = []
    
    # Calculate h = prime^(m-1)
    for _ in range(m - 1):
        h = (h * prime) % (2**31 - 1)
    
    # Calculate initial hash values for pattern and first window of text
    for i in range(m):
        pattern_hash = (prime * pattern_hash + ord(pattern[i])) % (2**31 - 1)
        text_hash = (prime * text_hash + ord(text[i])) % (2**31 - 1)
    
    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check if hash values match
        if pattern_hash == text_hash:
            # If hash matches, do character by character comparison
            if text[i:i+m] == pattern:
                results.append(i)
        
        # Calculate hash value for next window of text
        if i < n - m:
            text_hash = (prime * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % (2**31 - 1)
            
            # We might get negative values of text_hash, converting it to positive
            if text_hash < 0:
                text_hash += (2**31 - 1)
    
    return results