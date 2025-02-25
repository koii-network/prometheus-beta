def rabin_karp_search(text, pattern, prime=101):
    """
    Implement Rabin-Karp algorithm for string matching.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
        prime (int, optional): A prime number used for hash calculation. Defaults to 101.
    
    Returns:
        list: A list of starting indices where the pattern is found in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If pattern is longer than text or pattern is empty
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        raise ValueError("Pattern cannot be empty")
    
    if len(pattern) > len(text):
        return []
    
    # Initialize variables
    pattern_length = len(pattern)
    text_length = len(text)
    pattern_hash = 0
    text_hash = 0
    h = 1
    results = []
    
    # Calculate h = prime^(pattern_length-1)
    for _ in range(pattern_length - 1):
        h = (h * prime) % (2**31 - 1)
    
    # Calculate initial hashes
    for i in range(pattern_length):
        pattern_hash = (prime * pattern_hash + ord(pattern[i])) % (2**31 - 1)
        text_hash = (prime * text_hash + ord(text[i])) % (2**31 - 1)
    
    # Slide the pattern over text one by one
    for i in range(text_length - pattern_length + 1):
        # If hashes match, check characters
        if pattern_hash == text_hash:
            # Check each character
            if text[i:i+pattern_length] == pattern:
                results.append(i)
        
        # Calculate hash for next window of text
        if i < text_length - pattern_length:
            # Remove leading digit, add trailing digit
            text_hash = (prime * (text_hash - ord(text[i]) * h) + ord(text[i + pattern_length])) % (2**31 - 1)
            
            # Convert negative hash to positive
            if text_hash < 0:
                text_hash += (2**31 - 1)
    
    return results