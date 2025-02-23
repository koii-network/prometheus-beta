import sys

def rabin_karp_search(text: str, pattern: str, prime: int = 101) -> list:
    """
    Implement the Rabin-Karp algorithm for string matching.
    
    This function finds all occurrences of a pattern within a given text using 
    the Rabin-Karp rolling hash algorithm.
    
    Args:
        text (str): The text to search within
        pattern (str): The pattern to search for
        prime (int, optional): A prime number used for hash calculation. Defaults to 101.
    
    Returns:
        list: A list of starting indices where the pattern is found in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If pattern is empty or longer than text
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
    matches = []
    
    # Compute the hash value for the pattern and first window of text
    pattern_hash = 0
    text_hash = 0
    h = 1
    
    # Calculate h = prime^(pattern_length-1)
    for _ in range(pattern_length - 1):
        h = (h * prime) % sys.maxsize
    
    # Calculate initial hashes
    for i in range(pattern_length):
        pattern_hash = (prime * pattern_hash + ord(pattern[i])) % sys.maxsize
        text_hash = (prime * text_hash + ord(text[i])) % sys.maxsize
    
    # Slide the pattern over text one by one
    for i in range(text_length - pattern_length + 1):
        # Check if hash values match
        if pattern_hash == text_hash:
            # Check characters one by one if hash matches
            if text[i:i+pattern_length] == pattern:
                matches.append(i)
        
        # Calculate hash for next window of text
        if i < text_length - pattern_length:
            # Remove leading digit, add trailing digit
            text_hash = (prime * (text_hash - ord(text[i]) * h) + ord(text[i + pattern_length])) % sys.maxsize
            
            # Ensure positive hash value
            if text_hash < 0:
                text_hash += sys.maxsize
    
    return matches