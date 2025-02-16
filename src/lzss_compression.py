class LZSSCompressor:
    def __init__(self, window_size=4096, lookahead_size=16):
        """
        Initialize LZSS Compressor
        
        :param window_size: Size of the sliding window for searching matches
        :param lookahead_size: Size of the lookahead buffer for finding matches
        """
        self.window_size = window_size
        self.lookahead_size = lookahead_size
    
    def compress(self, data):
        """
        Compress input data using LZSS algorithm
        
        :param data: Input data to compress (bytes or string)
        :return: Compressed data as a list of compressed tokens
        """
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        compressed = []
        data_length = len(data)
        current_position = 0
        
        while current_position < data_length:
            # Determine search range
            search_start = max(0, current_position - self.window_size)
            search_end = current_position
            
            # Look for the longest match in the window
            best_length = 0
            best_offset = 0
            
            for offset in range(search_start, search_end):
                match_length = 0
                
                # Check how long the match continues
                while (match_length < self.lookahead_size and 
                       current_position + match_length < data_length and 
                       data[offset + match_length] == data[current_position + match_length]):
                    match_length += 1
                
                # Update best match if found
                if match_length > best_length:
                    best_length = match_length
                    best_offset = current_position - offset
            
            # Encode the result
            if best_length > 2:  # Minimum match length to compress
                # Compressed token: (offset, length, next character)
                compressed.append((best_offset, best_length, 
                                   data[current_position + best_length]))
                current_position += best_length + 1
            else:
                # Uncompressed character
                compressed.append(data[current_position])
                current_position += 1
        
        return compressed
    
    def decompress(self, compressed_data):
        """
        Decompress data compressed with LZSS algorithm
        
        :param compressed_data: List of compressed tokens
        :return: Decompressed data as bytes
        """
        decompressed = bytearray()
        
        for token in compressed_data:
            if isinstance(token, tuple):
                # Compressed token: (offset, length, next character)
                offset, length, next_char = token
                start = len(decompressed) - offset
                
                # Copy matched sequence
                for i in range(length):
                    decompressed.append(decompressed[start + i])
                
                # Append next character
                decompressed.append(next_char)
            else:
                # Uncompressed character
                decompressed.append(token)
        
        return bytes(decompressed)