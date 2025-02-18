class LZ77Compressor:
    def __init__(self, window_size=1024, look_ahead_size=16):
        """
        Initialize LZ77 Compressor
        
        :param window_size: Size of the sliding window (dictionary)
        :param look_ahead_size: Size of the look-ahead buffer
        """
        self.window_size = window_size
        self.look_ahead_size = look_ahead_size
    
    def compress(self, data):
        """
        Compress input data using LZ77 algorithm
        
        :param data: Input string or bytes to compress
        :return: List of tuples representing compressed tokens
        """
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        compressed = []
        current_pos = 0
        
        while current_pos < len(data):
            # Define search window boundaries
            start = max(0, current_pos - self.window_size)
            
            # Initialize best match
            best_length = 0
            best_offset = 0
            
            # Search through the window for the longest match
            for offset in range(current_pos - start):
                match_length = 0
                
                # Check how long the match continues
                while (match_length < self.look_ahead_size and 
                       current_pos + match_length < len(data) and 
                       data[current_pos - start + offset + match_length] == 
                       data[current_pos + match_length]):
                    match_length += 1
                
                # Update best match if needed
                if match_length > best_length:
                    best_length = match_length
                    best_offset = offset + 1
            
            # If no match found, output a single character
            if best_length == 0:
                compressed.append((0, 0, data[current_pos]))
                current_pos += 1
            else:
                # Output (offset, length, next character)
                compressed.append((best_offset, best_length, 
                                   data[current_pos + best_length]))
                current_pos += best_length + 1
        
        return compressed
    
    def decompress(self, compressed_data):
        """
        Decompress LZ77 compressed data
        
        :param compressed_data: List of tuples from compression
        :return: Decompressed bytes
        """
        decompressed = bytearray()
        
        for offset, length, next_char in compressed_data:
            if offset == 0 and length == 0:
                # Literal character
                decompressed.append(next_char)
            else:
                # Copy from previous data
                start = len(decompressed) - offset
                for i in range(length):
                    decompressed.append(decompressed[start + i])
                decompressed.append(next_char)
        
        return bytes(decompressed)