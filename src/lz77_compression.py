class LZ77:
    @staticmethod
    def compress(data, window_size=1024, lookahead_buffer_size=16):
        """
        Implement LZ77 compression algorithm.
        
        Args:
            data (str or bytes): Input data to compress
            window_size (int): Size of the sliding window for backward searching
            lookahead_buffer_size (int): Size of the lookahead buffer
        
        Returns:
            list: Compressed data as a list of tuples (offset, length, next_char)
        """
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        if not data:
            return []
        
        compressed = []
        data_length = len(data)
        current_position = 0
        
        while current_position < data_length:
            # Define search boundaries
            search_start = max(0, current_position - window_size)
            search_end = current_position
            lookahead_end = min(current_position + lookahead_buffer_size, data_length)
            
            # Find longest matching sequence
            best_offset = 0
            best_length = 0
            
            for offset in range(search_start, search_end):
                match_length = 0
                while (current_position + match_length < lookahead_end and
                       data[offset + match_length] == data[current_position + match_length]):
                    match_length += 1
                
                if match_length > best_length:
                    best_offset = current_position - offset
                    best_length = match_length
            
            # Add compressed token
            if best_length > 0:
                next_char = data[current_position + best_length]
                compressed.append((best_offset, best_length, chr(next_char)))
                current_position += best_length + 1
            else:
                compressed.append((0, 0, chr(data[current_position])))
                current_position += 1
        
        return compressed
    
    @staticmethod
    def decompress(compressed_data):
        """
        Decompress LZ77 compressed data.
        
        Args:
            compressed_data (list): Compressed data as list of tuples (offset, length, next_char)
        
        Returns:
            bytes: Decompressed data
        """
        if not compressed_data:
            return b''
        
        decompressed = bytearray()
        
        for offset, length, next_char in compressed_data:
            if offset == 0 and length == 0:
                # Literal character
                decompressed.append(ord(next_char))
            else:
                # Copy from previously seen data
                start = len(decompressed) - offset
                for i in range(length):
                    decompressed.append(decompressed[start + i])
                decompressed.append(ord(next_char))
        
        return bytes(decompressed)