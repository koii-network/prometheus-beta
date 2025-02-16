class LZRWCompressor:
    def __init__(self, max_dict_size=4096):
        """
        Initialize LZRW compression algorithm.
        
        Args:
            max_dict_size (int): Maximum size of the dictionary
        """
        self.max_dict_size = max_dict_size
    
    def compress(self, input_data):
        """
        Compress input data using LZRW algorithm.
        
        Args:
            input_data (bytes or str): Data to compress
        
        Returns:
            bytes: Compressed data
        """
        # Handle empty input
        if not input_data:
            return bytes()
        
        # Ensure input is bytes
        if isinstance(input_data, str):
            input_data = input_data.encode('utf-8')
        
        # Initialize compression variables
        dictionary = {bytes([i]): i for i in range(256)}
        next_code = 256
        
        # Compression buffers
        compressed = bytearray()
        current_sequence = b""
        
        # Process each byte
        for byte in input_data:
            # Create candidate sequence
            candidate = current_sequence + bytes([byte])
            
            # If candidate is in dictionary, extend current sequence
            if candidate in dictionary:
                current_sequence = candidate
            else:
                # Output code for current sequence
                if current_sequence in dictionary:
                    compressed.append(dictionary[current_sequence])
                else:
                    # Encode each byte of current sequence
                    for b in current_sequence:
                        compressed.append(b)
                
                # Add new sequence to dictionary if room
                if next_code < self.max_dict_size:
                    dictionary[candidate] = next_code
                    next_code += 1
                
                # Reset current sequence
                current_sequence = bytes([byte])
        
        # Handle last sequence
        if current_sequence:
            if current_sequence in dictionary:
                compressed.append(dictionary[current_sequence])
            else:
                # Encode each byte of current sequence
                for b in current_sequence:
                    compressed.append(b)
        
        return bytes(compressed)
    
    def decompress(self, compressed_data):
        """
        Decompress data using LZRW algorithm.
        
        Args:
            compressed_data (bytes): Compressed data to decompress
        
        Returns:
            bytes: Decompressed data
        """
        # Handle empty input
        if not compressed_data:
            return bytes()
        
        # Initialize decompression variables
        dictionary = {i: bytes([i]) for i in range(256)}
        next_code = 256
        
        # Decompression buffers
        decompressed = bytearray()
        current_sequence = bytes([compressed_data[0]])
        decompressed.extend(current_sequence)
        
        # Process compressed data starting from second byte
        for code in compressed_data[1:]:
            # Determine the entry
            if code in dictionary:
                next_entry = dictionary[code]
            else:
                # If code not found, create entry based on current sequence
                next_entry = current_sequence + current_sequence[0:1]
            
            # Add next entry to decompressed data
            decompressed.extend(next_entry)
            
            # Update dictionary
            if next_code < self.max_dict_size:
                dictionary[next_code] = current_sequence + next_entry[0:1]
                next_code += 1
            
            # Update current sequence
            current_sequence = next_entry
        
        return bytes(decompressed)

def lzrw_compress(input_data):
    """
    Convenience function for LZRW compression.
    
    Args:
        input_data (bytes or str): Data to compress
    
    Returns:
        bytes: Compressed data
    """
    return LZRWCompressor().compress(input_data)

def lzrw_decompress(compressed_data):
    """
    Convenience function for LZRW decompression.
    
    Args:
        compressed_data (bytes): Compressed data to decompress
    
    Returns:
        bytes: Decompressed data
    """
    return LZRWCompressor().decompress(compressed_data)