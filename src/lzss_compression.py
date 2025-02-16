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
        :return: Compressed data as a list of tuples/tokens
        """
        # Ensure input is bytes
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        compressed = []
        data_length = len(data)
        current_pos = 0

        while current_pos < data_length:
            # Find the longest match in the sliding window
            best_length = 0
            best_offset = 0
            
            # Define search boundaries
            search_start = max(0, current_pos - self.window_size)
            search_end = current_pos
            look_ahead_end = min(current_pos + self.look_ahead_size, data_length)

            # Search for the longest match
            for offset in range(search_start, search_end):
                match_length = 0
                while (current_pos + match_length < look_ahead_end and
                       data[current_pos + match_length] == data[offset + match_length]):
                    match_length += 1
                
                # Update best match if found
                if match_length > best_length:
                    best_length = match_length
                    best_offset = current_pos - offset

            # Encode the token
            if best_length > 2:
                # Match found: (offset, length, next_char)
                compressed.append((best_offset, best_length, 
                                   data[current_pos + best_length]))
                current_pos += best_length + 1
            else:
                # No match: literal character
                compressed.append(data[current_pos])
                current_pos += 1

        return compressed

    def decompress(self, compressed_data):
        """
        Decompress data compressed with LZSS algorithm
        
        :param compressed_data: Compressed data (list of tuples/tokens)
        :return: Decompressed data as bytes
        """
        decompressed = bytearray()

        for token in compressed_data:
            if isinstance(token, tuple):
                # Matched sequence: (offset, length, next_char)
                offset, length, next_char = token
                start = len(decompressed) - offset
                
                # Reproduce the matched sequence
                for i in range(length):
                    decompressed.append(decompressed[start + i])
                
                # Add the next character
                decompressed.append(next_char)
            else:
                # Literal character
                decompressed.append(token)

        return bytes(decompressed)