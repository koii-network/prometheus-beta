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
        Compress input data using a custom LZ-style compression.
        
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
        
        # Compression variables
        compressed = bytearray()
        pos = 0
        window_size = 256  # Smaller sliding window
        
        while pos < len(input_data):
            # Look for longest match in previous window
            best_match_length = 0
            best_match_distance = 0
            
            # Define search window
            window_start = max(0, pos - window_size)
            window = input_data[window_start:pos]
            
            # Look ahead buffer
            lookahead = input_data[pos:min(pos + 16, len(input_data))]
            
            # Find best match
            for distance in range(1, len(window) + 1):
                # Current search position 
                search_pos = len(window) - distance
                
                # Compute match length
                match_length = 0
                while (match_length < len(lookahead) and 
                       search_pos + match_length < len(window) and
                       window[search_pos + match_length] == lookahead[match_length]):
                    match_length += 1
                
                # Update best match
                if match_length > best_match_length:
                    best_match_length = match_length
                    best_match_distance = distance
            
            # Encode match or literal
            if best_match_length > 2:
                # Compressed token
                # First byte: Match flag (0x80) + 4-bit distance high
                # Second byte: Distance low bits
                # Third byte: Match length
                compressed.append(0x80 | ((best_match_distance >> 8) & 0x0F))
                compressed.append(best_match_distance & 0xFF)
                compressed.append(best_match_length)
                
                # Move position
                pos += best_match_length
            else:
                # Literal byte
                compressed.append(input_data[pos])
                pos += 1
        
        return bytes(compressed)
    
    def decompress(self, compressed_data):
        """
        Decompress LZRW compressed data.
        
        Args:
            compressed_data (bytes): Compressed data
        
        Returns:
            bytes: Decompressed data
        """
        # Handle empty input
        if not compressed_data:
            return bytes()
        
        # Decompression variables
        decompressed = bytearray()
        pos = 0
        
        while pos < len(compressed_data):
            # Check if current token is a match 
            if compressed_data[pos] & 0x80:
                # Verify we have enough data for match 
                if pos + 2 >= len(compressed_data):
                    raise ValueError("Invalid compressed data")
                
                # Extract match details
                # High 4 bits of distance + low distance byte
                high_distance = (compressed_data[pos] & 0x0F) << 8
                low_distance = compressed_data[pos + 1]
                distance = high_distance | low_distance
                length = compressed_data[pos + 2]
                
                # Validate match
                if distance > len(decompressed) or length == 0:
                    raise ValueError("Invalid match in compressed data")
                
                # Copy match from existing decompressed data
                match_start = len(decompressed) - distance
                for i in range(length):
                    decompressed.append(decompressed[match_start + i])
                
                # Move position
                pos += 3
            else:
                # Literal byte
                decompressed.append(compressed_data[pos])
                pos += 1
        
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