class LZSSCompressor:
    def __init__(self, window_size=4096, lookahead_size=16):
        """
        Initialize LZSS Compressor
        
        :param window_size: Size of the sliding window for searching previous matches
        :param lookahead_size: Size of the lookahead buffer for finding matches
        """
        self.window_size = window_size
        self.lookahead_size = lookahead_size

    def compress(self, data):
        """
        Compress input data using LZSS algorithm
        
        :param data: Input data to compress (bytes or string)
        :return: Compressed data as bytes
        """
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        compressed = bytearray()
        start = 0
        
        while start < len(data):
            # Find the longest match in the sliding window
            best_length = 0
            best_offset = 0
            
            # Determine the search range
            search_start = max(0, start - self.window_size)
            search_end = start
            lookahead_end = min(start + self.lookahead_size, len(data))
            
            # Search for the longest match
            for offset in range(search_start, search_end):
                match_length = 0
                
                # Check how long the match continues
                while (start + match_length < lookahead_end and 
                       data[offset + match_length] == data[start + match_length]):
                    match_length += 1
                
                # Update best match if current is longer
                if match_length > best_length:
                    best_length = match_length
                    best_offset = start - offset
            
            # If a good match is found, encode it as (offset, length)
            # Otherwise, encode a single uncompressed byte
            if best_length >= 3:  # Minimum match length to compress
                # Compressed token: (offset, length)
                compressed.append(0)  # Flag for compressed token
                compressed.extend(best_offset.to_bytes(2, byteorder='big'))
                compressed.append(best_length)
                start += best_length
            else:
                # Uncompressed token
                compressed.append(1)  # Flag for uncompressed token
                compressed.append(data[start])
                start += 1
        
        return bytes(compressed)

    def decompress(self, compressed_data):
        """
        Decompress data compressed with LZSS algorithm
        
        :param compressed_data: Compressed data to decompress
        :return: Decompressed data as bytes
        """
        decompressed = bytearray()
        i = 0
        
        while i < len(compressed_data):
            # Check token type
            if compressed_data[i] == 0:  # Compressed token
                if i + 3 >= len(compressed_data):
                    raise ValueError("Incomplete compressed data")
                
                # Extract offset and length
                offset = int.from_bytes(compressed_data[i+1:i+3], byteorder='big')
                length = compressed_data[i+3]
                
                # Reproduce the matched sequence
                start_pos = len(decompressed) - offset
                for j in range(length):
                    decompressed.append(decompressed[start_pos + j])
                
                i += 4
            else:  # Uncompressed token
                if i + 1 >= len(compressed_data):
                    raise ValueError("Incomplete compressed data")
                
                # Add single byte
                decompressed.append(compressed_data[i+1])
                i += 2
        
        return bytes(decompressed)