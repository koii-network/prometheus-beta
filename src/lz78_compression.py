def lz78_compress(input_string):
    """
    Implement LZ78 compression algorithm.
    
    Args:
        input_string (str): The input string to be compressed.
    
    Returns:
        list: A list of tuples representing the compressed data.
              Each tuple is in the format (index, character):
              - index: reference to previous dictionary entry (0 for new entries)
              - character: the new character being added
    """
    if not input_string:
        return []
    
    # Initialize dictionary with an empty first entry
    dictionary = {0: ''}
    next_index = 1
    result = []
    
    current_sequence = ''
    
    for char in input_string:
        # Check if current sequence + new char is in dictionary
        current_sequence_with_char = current_sequence + char
        
        # Find the index of the longest matching sequence
        found_index = 0
        for index, value in dictionary.items():
            if value == current_sequence_with_char:
                found_index = index
                break
        
        # If sequence is not in dictionary, add it
        if found_index == 0:
            result.append((0 if current_sequence == '' else dictionary[current_sequence], char))
            dictionary[next_index] = current_sequence_with_char
            next_index += 1
            current_sequence = ''
        else:
            current_sequence = current_sequence_with_char
    
    # Handle last sequence if exists
    if current_sequence:
        result.append((dictionary.get(current_sequence, 0), ''))
    
    return result

def lz78_decompress(compressed_data):
    """
    Decompress LZ78 compressed data.
    
    Args:
        compressed_data (list): Compressed data as list of tuples (index, character)
    
    Returns:
        str: Decompressed original string
    """
    if not compressed_data:
        return ''
    
    # Initialize dictionary with an empty first entry
    dictionary = {0: ''}
    next_index = 1
    
    # Store decompressed sequence
    decompressed = []
    
    for index, char in compressed_data:
        # Reconstruct the sequence
        if index == 0:
            # New entry
            sequence = char
        else:
            # Use previous dictionary entry and add new character
            sequence = dictionary[index] + char
        
        decompressed.append(sequence)
        
        # Add new entry to dictionary
        dictionary[next_index] = sequence
        next_index += 1
    
    return ''.join(decompressed)