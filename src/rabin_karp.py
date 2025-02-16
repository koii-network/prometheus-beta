def rabin_karp_search(text, pattern, prime=101):
    """
    Perform Rabin-Karp string matching algorithm.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
        prime (int, optional): A prime number used for hashing. Defaults to 101.
    
    Returns:
        list: A list of starting indices where the pattern is found in the text
    
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
    
    # Results list to store match indices
    results = []
    
    # Length of pattern and text
    n, m = len(text), len(pattern)
    
    # Calculate the hash value for pattern and first window of text
    pattern_hash = 0
    text_hash = 0
    h = 1
    
    # Calculate h = prime^(m-1)
    for _ in range(m - 1):
        h = (h * prime) % 2**32
    
    # Calculate initial hash values
    for i in range(m):
        pattern_hash = (prime * pattern_hash + ord(pattern[i])) % 2**32
        text_hash = (prime * text_hash + ord(text[i])) % 2**32
    
    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check if hash values match
        if pattern_hash == text_hash:
            # If hash matches, do character by character comparison
            if text[i:i+m] == pattern:
                results.append(i)
        
        # Calculate hash value for next window of text
        if i < n - m:
            text_hash = (prime * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % 2**32
            
            # Convert negative hash to positive
            if text_hash < 0:
                text_hash += 2**32
    
    return results