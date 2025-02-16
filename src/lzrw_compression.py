class LZRWCompressor:
    def __init__(self, window_size=4096, lookahead_size=16):
        """
        Initialize LZRW compression algorithm.
        
        Args:
            window_size (int): Size of the sliding window for searching matches
            lookahead_size (int): Size of the lookahead buffer
        """
        self.window_size = window_size
        self.lookahead_size = lookahead_size
    
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
        
        # Compression buffers
        compressed = bytearray()
        pos = 0
        
        while pos < len(input_data):
            # Find the longest match in the window
            longest_match_length = 0
            longest_match_offset = 0
            
            # Search back in the current window
            window_start = max(0, pos - self.window_size)
            search_window = input_data[window_start:pos]
            
            # Look ahead to find a match
            lookahead_end = min(pos + self.lookahead_size, len(input_data))
            lookahead = input_data[pos:lookahead_end]
            
            for offset in range(len(search_window)):
                match_length = 0
                
                # Find match length
                while (match_length < len(lookahead) and 
                       search_window[len(search_window) - offset - 1 + match_length] == lookahead[match_length]):
                    match_length += 1
                
                # Update longest match if better match found
                if match_length > longest_match_length:
                    longest_match_length = match_length
                    longest_match_offset = offset
            
            # Encode match or literal
            if longest_match_length > 2:
                # Encode match: offset (2 bytes), length (1 byte)
                offset = longest_match_offset
                length = longest_match_length
                
                # Use high bit to mark match
                compressed.extend([
                    0x80 | ((offset >> 8) & 0x0F),  # High 4 bits of high-order offset byte
                    offset & 0xFF,                  # Low 8 bits of offset
                    length                          # Length of match
                ])
                
                # Move position
                pos += length
            else:
                # Encode literal
                compressed.append(input_data[pos])
                pos += 1
        
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
        
        # Decompression buffer
        decompressed = bytearray()
        pos = 0
        
        while pos < len(compressed_data):
            # Check if it's a match or literal
            if compressed_data[pos] & 0x80:
                # Match encoding
                if pos + 2 >= len(compressed_data):
                    raise ValueError("Invalid compressed data")
                
                # Decode match info
                high_offset = (compressed_data[pos] & 0x0F) << 8
                low_offset = compressed_data[pos + 1]
                offset = high_offset | low_offset
                length = compressed_data[pos + 2]
                
                # Find match in current decompressed data
                match_start = len(decompressed) - offset - 1
                
                # Copy match
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