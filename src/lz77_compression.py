class LZ77Compressor:
    def __init__(self, window_size=1024, lookahead_size=16):
        """
        Initialize LZ77 Compressor
        
        :param window_size: Size of the sliding window (search buffer)
        :param lookahead_size: Size of the lookahead buffer
        """
        self.window_size = window_size
        self.lookahead_size = lookahead_size
    
    def compress(self, data):
        """
        Compress input data using LZ77 algorithm
        
        :param data: Input data to compress (string or bytes)
        :return: List of tuples representing compressed tokens
        """
        if not data:
            return []
        
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        compressed = []
        data_length = len(data)
        current_index = 0
        
        while current_index < data_length:
            # Define search and lookahead boundaries
            search_start = max(0, current_index - self.window_size)
            search_end = current_index
            lookahead_end = min(current_index + self.lookahead_size, data_length)
            
            # Find longest match in the search buffer
            best_length = 0
            best_offset = 0
            
            for search_pos in range(search_start, search_end):
                match_length = 0
                
                # Check for matching subsequence
                while (current_index + match_length < lookahead_end and
                       data[search_pos + match_length] == data[current_index + match_length]):
                    match_length += 1
                    
                    # Prevent out of bounds
                    if (search_pos + match_length >= search_end or 
                        current_index + match_length >= data_length):
                        break
                
                # Update best match if longer
                if match_length > best_length:
                    best_length = match_length
                    best_offset = current_index - search_pos
            
            # If no match found, output literal
            if best_length == 0:
                compressed.append((0, 0, data[current_index]))
                current_index += 1
            else:
                # Output (offset, length, next character)
                next_char = data[current_index + best_length] if current_index + best_length < data_length else None
                compressed.append((best_offset, best_length, next_char))
                current_index += best_length + 1
        
        return compressed
    
    def decompress(self, compressed_data):
        """
        Decompress LZ77 encoded data
        
        :param compressed_data: List of tuples from compression
        :return: Decompressed bytes
        """
        if not compressed_data:
            return b''
        
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
                
                # Add next character if exists
                if next_char is not None:
                    decompressed.append(next_char)
        
        return bytes(decompressed)