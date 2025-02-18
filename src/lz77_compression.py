class LZ77Compressor:
    def __init__(self, window_size=1024, lookahead_size=16):
        """
        Initialize LZ77 Compressor
        
        :param window_size: Size of the sliding window for back-referencing
        :param lookahead_size: Size of the lookahead buffer
        """
        self.window_size = window_size
        self.lookahead_size = lookahead_size
    
    def compress(self, data):
        """
        Compress input data using LZ77 algorithm
        
        :param data: Input string or bytes to compress
        :return: List of tuples (offset, length, next_char)
        """
        if not data:
            return []
        
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        compressed = []
        start = 0
        while start < len(data):
            # Look for the longest match in the window
            best_length = 0
            best_offset = 0
            
            # Search in the sliding window
            window_start = max(0, start - self.window_size)
            search_window = data[window_start:start]
            
            # Look ahead buffer
            lookahead = data[start:min(start + self.lookahead_size, len(data))]
            
            # Find longest match
            for offset in range(len(search_window)):
                match_length = 0
                while (match_length < len(lookahead) and 
                       search_window[offset + match_length] == lookahead[match_length]):
                    match_length += 1
                    if offset + match_length >= len(search_window):
                        break
                
                # Update best match if found
                if match_length > best_length:
                    best_length = match_length
                    best_offset = len(search_window) - offset
            
            # Add compressed token
            if best_length > 0:
                next_char = lookahead[best_length] if best_length < len(lookahead) else None
                compressed.append((best_offset, best_length, 
                                   chr(next_char) if next_char is not None else ''))
                start += best_length + 1
            else:
                # No match found, encode as literal
                compressed.append((0, 0, chr(data[start])))
                start += 1
        
        return compressed
    
    def decompress(self, compressed):
        """
        Decompress LZ77 compressed data
        
        :param compressed: List of tuples (offset, length, next_char)
        :return: Decompressed bytes
        """
        if not compressed:
            return b''
        
        decompressed = bytearray()
        
        for offset, length, next_char in compressed:
            if offset == 0 and length == 0:
                # Literal character
                decompressed.append(ord(next_char))
            else:
                # Copy from previous data
                start = len(decompressed) - offset
                for i in range(length):
                    decompressed.append(decompressed[start + i])
                
                # Add next character if exists
                if next_char:
                    decompressed.append(ord(next_char))
        
        return bytes(decompressed)