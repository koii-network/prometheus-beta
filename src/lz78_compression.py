class LZ78Compressor:
    """
    LZ78 Compression algorithm implementation.
    
    This implementation follows the classic LZ78 compression technique,
    which builds a dictionary of unique substrings during compression.
    """
    
    @staticmethod
    def compress(input_text):
        """
        Compress the input text using LZ78 compression algorithm.
        
        Args:
            input_text (str): The text to be compressed
        
        Returns:
            list: A list of tuples representing compressed data
                  Each tuple is (index, character)
        """
        if not input_text:
            return []
        
        # Initialize dictionary with 0 index representing empty string
        dictionary = {0: ''}
        next_index = 1
        result = []
        current_sequence = ''
        
        for char in input_text:
            # Try to extend current sequence
            extended_sequence = current_sequence + char
            
            # Check if extended sequence exists in dictionary
            found = False
            for index, entry in dictionary.items():
                if entry == extended_sequence:
                    current_sequence = extended_sequence
                    found = True
                    break
            
            # If extended sequence not found, add to dictionary
            if not found:
                # Find the index of current_sequence
                dict_index = next(
                    (idx for idx, entry in dictionary.items() if entry == current_sequence), 
                    0
                )
                
                # Add compressed tuple
                result.append((dict_index, char))
                
                # Add new sequence to dictionary
                dictionary[next_index] = extended_sequence
                next_index += 1
                
                # Reset current sequence
                current_sequence = ''
        
        # Handle any remaining sequence
        if current_sequence:
            dict_index = next(
                (idx for idx, entry in dictionary.items() if entry == current_sequence), 
                0
            )
            result.append((dict_index, ''))
        
        return result
    
    @staticmethod
    def decompress(compressed_data):
        """
        Decompress data compressed with LZ78 algorithm.
        
        Args:
            compressed_data (list): List of tuples from compression
        
        Returns:
            str: Decompressed text
        """
        if not compressed_data:
            return ''
        
        # Initialize dictionary with 0 index representing empty string
        dictionary = {0: ''}
        next_index = 1
        result = []
        
        for index, char in compressed_data:
            # Retrieve previous sequence
            prev_sequence = dictionary.get(index, '')
            
            # Construct current sequence
            current_sequence = prev_sequence + char
            
            # Add to result
            result.append(current_sequence)
            
            # Add to dictionary
            dictionary[next_index] = current_sequence
            next_index += 1
        
        return ''.join(result)