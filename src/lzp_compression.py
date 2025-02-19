def lzp_compress(text):
    """
    Implement Lempel-Ziv Prediction (LZP) compression algorithm.
    
    Args:
        text (str): Input text to be compressed
    
    Returns:
        list: Compressed representation of the input text
    """
    if not text:
        return []
    
    # Initialize dictionary with empty context
    dictionary = {
        '': 0  # Empty context initially mapped to index 0
    }
    
    # Output will store the compressed representation
    output = []
    
    # Sliding context window
    context = ''
    
    for char in text:
        # Check if current context + char exists in dictionary
        full_context = context + char
        
        if full_context in dictionary:
            # If context exists, update context and continue
            context = full_context
        else:
            # If context doesn't exist, output current context's index 
            # and add new context to dictionary
            output.append(dictionary.get(context, 0))
            dictionary[full_context] = len(dictionary)
            context = char
    
    # Add the last context's index
    if context:
        output.append(dictionary.get(context, 0))
    
    return output

def lzp_decompress(compressed):
    """
    Decompress LZP compressed data.
    
    Args:
        compressed (list): Compressed representation of text
    
    Returns:
        str: Decompressed original text
    """
    if not compressed:
        return ''
    
    # Initialize dictionary with empty context
    dictionary = {
        0: ''  # Index 0 mapped to empty string
    }
    
    # Output will store the decompressed text
    output = []
    
    # Sliding context window
    context = ''
    
    for index in compressed:
        # Retrieve the decoded text for current index
        decoded_text = dictionary.get(index, '')
        
        if decoded_text:
            # If index exists, append to output and update context
            output.append(decoded_text)
            context += decoded_text
        else:
            # If index doesn't exist, add a character from context
            if context:
                decoded_text = context[0]
                output.append(decoded_text)
                context += decoded_text
        
        # Limit context length to prevent excessive memory usage
        context = context[-64:] if len(context) > 64 else context
        
        # Add new entries to dictionary
        dictionary[len(dictionary)] = decoded_text
    
    return ''.join(output)