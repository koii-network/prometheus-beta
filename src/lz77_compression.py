class LZ77Compressor:
    def __init__(self, window_size=4096, lookahead_buffer_size=16):
        """
        LZ77 Compression Algorithm Implementation
        
        Args:
            window_size (int): Size of the sliding window for searching previous matches
            lookahead_buffer_size (int): Size of the lookahead buffer for finding matches
        """
        self.window_size = window_size
        self.lookahead_buffer_size = lookahead_buffer_size
    
    def compress(self, data):
        """
        Compress input data using LZ77 algorithm
        
        Args:
            data (str or bytes): Input data to compress
        
        Returns:
            list: Compressed data represented as tuples of (offset, length, next_char)
        """
        if not data:
            return []
        
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        compressed = []
        current_pos = 0
        
        while current_pos < len(data):
            # Define search window boundaries
            start = max(0, current_pos - self.window_size)
            end = min(len(data), current_pos + self.lookahead_buffer_size)
            
            # Find the longest match in the search window
            best_offset = 0
            best_length = 0
            next_char = data[current_pos]
            
            for offset in range(1, current_pos - start + 1):
                match_length = 0
                
                # Check match length
                while (match_length < end - current_pos and 
                       data[current_pos - offset + match_length] == data[current_pos + match_length]):
                    match_length += 1
                
                # Update best match if longer
                if match_length > best_length:
                    best_offset = offset
                    best_length = match_length
                    if current_pos + match_length < len(data):
                        next_char = data[current_pos + match_length]
            
            # Add compressed token
            compressed.append((best_offset, best_length, next_char))
            
            # Move current position
            current_pos += best_length + 1
        
        return compressed
    
    def decompress(self, compressed_data):
        """
        Decompress data compressed with LZ77 algorithm
        
        Args:
            compressed_data (list): Compressed data as tuples of (offset, length, next_char)
        
        Returns:
            bytes: Decompressed data
        """
        if not compressed_data:
            return b''
        
        decompressed = bytearray()
        
        for offset, length, next_char in compressed_data:
            # If no match found, just add the character
            if offset == 0 and length == 0:
                decompressed.append(next_char)
            else:
                # Copy matched sequence
                start = len(decompressed) - offset
                for i in range(length):
                    decompressed.append(decompressed[start + i])
                
                # Add next character
                decompressed.append(next_char)
        
        return bytes(decompressed)