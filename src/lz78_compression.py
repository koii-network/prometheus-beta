def lz78_compress(input_string):
    """
    Implement LZ78 compression algorithm.
    
    Args:
        input_string (str): The input string to compress
    
    Returns:
        list: A list of tuples representing the compressed data 
              Each tuple is (index, character)
    """
    # Handle empty string case
    if not input_string:
        return []
    
    # Initialize dictionary and output
    dictionary = {0: ''}  # 0 represents an empty string
    current_index = 1
    output = []
    current_sequence = ''
    
    for char in input_string:
        # Try to extend the current sequence
        extended_sequence = current_sequence + char
        
        # Check if the extended sequence is in the dictionary
        found = False
        for index, dict_sequence in dictionary.items():
            if dict_sequence == extended_sequence:
                current_sequence = extended_sequence
                found = True
                break
        
        # If extended sequence is not in dictionary
        if not found:
            # Find the index of the longest prefix
            prefix_index = 0
            for index, dict_sequence in dictionary.items():
                if dict_sequence == current_sequence:
                    prefix_index = index
                    break
            
            # Add to output and dictionary
            output.append((prefix_index, char))
            dictionary[current_index] = extended_sequence
            current_index += 1
            
            # Reset current sequence
            current_sequence = ''
    
    # Handle the last sequence if any
    if current_sequence:
        for index, dict_sequence in dictionary.items():
            if dict_sequence == current_sequence:
                output.append((index, ''))
                break
    
    return output

def lz78_decompress(compressed_data):
    """
    Decompress LZ78 compressed data.
    
    Args:
        compressed_data (list): List of tuples from LZ78 compression
    
    Returns:
        str: Decompressed original string
    """
    # Handle empty input
    if not compressed_data:
        return ''
    
    # Initialize dictionary and output
    dictionary = {0: ''}
    current_index = 1
    output = []
    
    for index, char in compressed_data:
        # Retrieve the sequence for the given index
        prefix = dictionary[index]
        
        # Construct the new sequence
        new_sequence = prefix + char if char else prefix
        
        # Add to output
        output.append(new_sequence)
        
        # Add to dictionary for future reference
        dictionary[current_index] = new_sequence
        current_index += 1
    
    # Join and return the decompressed string
    return ''.join(output)