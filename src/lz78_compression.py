def lz78_compress(input_string):
    """
    Implement LZ78 compression algorithm.
    
    Args:
        input_string (str): The input string to compress.
    
    Returns:
        list: A list of tuples representing the compressed output,
              where each tuple is (index, character).
    """
    if not input_string:
        return []
    
    # Initialize dictionary with 0 index representing empty string
    dictionary = {0: ''}
    next_index = 1
    
    # Initialize compressed output and current sequence
    compressed = []
    current_sequence = ''
    
    for char in input_string:
        # Try to find the longest match in the dictionary
        test_sequence = current_sequence + char
        
        # Check if the current sequence + char is in the dictionary
        found = False
        for index, entry in dictionary.items():
            if entry == test_sequence:
                current_sequence = test_sequence
                found = True
                break
        
        # If not found, add to dictionary and output
        if not found:
            # Find the index of the current sequence
            current_index = 0
            for idx, entry in dictionary.items():
                if entry == current_sequence:
                    current_index = idx
                    break
            
            # Add compressed tuple and new dictionary entry
            compressed.append((current_index, char))
            dictionary[next_index] = test_sequence
            next_index += 1
            
            # Reset current sequence
            current_sequence = ''
    
    # Handle any remaining sequence
    if current_sequence:
        for index, entry in dictionary.items():
            if entry == current_sequence:
                compressed.append((index, ''))
                break
    
    return compressed

def lz78_decompress(compressed):
    """
    Decompress LZ78 compressed data.
    
    Args:
        compressed (list): A list of tuples from LZ78 compression.
    
    Returns:
        str: The decompressed original string.
    """
    if not compressed:
        return ''
    
    # Initialize dictionary with 0 index representing empty string
    dictionary = {0: ''}
    next_index = 1
    
    # Initialize decompressed output
    decompressed = []
    
    for index, char in compressed:
        # Retrieve the string for the given index
        prefix = dictionary.get(index, '')
        
        # Construct the full string for this entry
        current_string = prefix + char
        
        # Add to decompressed output
        decompressed.append(current_string)
        
        # Add to dictionary
        dictionary[next_index] = current_string
        next_index += 1
    
    return ''.join(decompressed)