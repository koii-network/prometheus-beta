class LZSSCompressor:
    def __init__(self, window_size=4096, look_ahead_size=16):
        """
        Initialize LZSS Compressor
        
        :param window_size: Size of the sliding window for searching previous matches
        :param look_ahead_size: Size of the look-ahead buffer for finding matches
        """
        self.window_size = window_size
        self.look_ahead_size = look_ahead_size
    
    def compress(self, data):
        """
        Compress input data using LZSS algorithm
        
        :param data: Input data to compress (bytes or string)
        :return: Compressed data as bytes
        """
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Validate input
        if not data:
            return b''
        
        compressed = bytearray()
        search_buffer = bytearray()
        look_ahead_buffer = bytearray(data[:self.look_ahead_size])
        data = data[self.look_ahead_size:]
        
        while look_ahead_buffer:
            # Find the longest match in the search buffer
            best_match_length = 0
            best_match_offset = 0
            
            for offset in range(1, min(len(search_buffer) + 1, self.window_size + 1)):
                # Start of potential match
                match_start = len(search_buffer) - offset
                
                # Calculate max match length
                match_length = 0
                while (match_length < len(look_ahead_buffer) and 
                       match_length < offset and 
                       search_buffer[match_start + match_length] == look_ahead_buffer[match_length]):
                    match_length += 1
                
                # Update best match if found
                if match_length > best_match_length:
                    best_match_length = match_length
                    best_match_offset = offset
            
            # If a match is found of length > 2
            if best_match_length > 2:
                # Encoded as (offset, length)
                compressed.append(0)  # Flag for match
                compressed.append(((best_match_offset - 1) >> 8) & 0xFF)  # High byte of offset
                compressed.append((best_match_offset - 1) & 0xFF)  # Low byte of offset
                compressed.append(best_match_length - 3)  # Length offset
                
                # Move buffers
                search_buffer.extend(look_ahead_buffer[:best_match_length])
                look_ahead_buffer = look_ahead_buffer[best_match_length:]
                
                # Add more data to look-ahead buffer if available
                while len(look_ahead_buffer) < self.look_ahead_size and data:
                    look_ahead_buffer.append(data[0])
                    data = data[1:]
            
            # No match or short match
            else:
                # Literal byte
                compressed.append(1)  # Flag for literal
                compressed.append(look_ahead_buffer[0])
                
                # Move buffers
                search_buffer.append(look_ahead_buffer[0])
                look_ahead_buffer = look_ahead_buffer[1:]
                
                # Add more data to look-ahead buffer if available
                while len(look_ahead_buffer) < self.look_ahead_size and data:
                    look_ahead_buffer.append(data[0])
                    data = data[1:]
            
            # Maintain window size
            if len(search_buffer) > self.window_size:
                search_buffer = search_buffer[-self.window_size:]
        
        return bytes(compressed)
    
    def decompress(self, compressed_data):
        """
        Decompress data compressed with LZSS algorithm
        
        :param compressed_data: Compressed input data as bytes
        :return: Decompressed data as bytes
        """
        # Validate input
        if not compressed_data:
            return b''
        
        decompressed = bytearray()
        i = 0
        
        while i < len(compressed_data):
            # Ensure there's a flag byte
            if i >= len(compressed_data):
                break
            
            # Check flag byte
            flag = compressed_data[i]
            i += 1
            
            if flag == 0:  # Match
                # Ensure sufficient data for offset and length
                if i + 2 >= len(compressed_data):
                    break
                
                # Extract offset and length
                try:
                    offset = ((compressed_data[i] << 8) | compressed_data[i+1]) + 1
                    i += 2
                    length = compressed_data[i] + 3
                    i += 1
                except IndexError:
                    # Handle cases of incomplete data
                    break
                
                # Copy matched sequence
                start = len(decompressed) - offset
                for _ in range(length):
                    if start < 0:
                        # Handle potential indexing error
                        break
                    decompressed.append(decompressed[start])
                    start += 1
            
            elif flag == 1:  # Literal
                if i >= len(compressed_data):
                    break
                
                # Add literal byte
                decompressed.append(compressed_data[i])
                i += 1
            
            else:
                # Skip invalid flags or stop processing
                break
        
        return bytes(decompressed)