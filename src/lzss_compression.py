class LZSS:
    def __init__(self, window_size=4096, look_ahead_size=16):
        """
        Initialize LZSS compression parameters.
        
        :param window_size: Size of the sliding window for searching previous matches
        :param look_ahead_size: Size of the look-ahead buffer for finding matches
        """
        self.window_size = window_size
        self.look_ahead_size = look_ahead_size

    def compress(self, data):
        """
        Compress input data using LZSS algorithm.
        
        :param data: Input data to compress (bytes or string)
        :return: Compressed data as a list of tuples/bytes
        """
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        compressed = []
        data_length = len(data)
        search_start = 0
        current_pos = 0

        while current_pos < data_length:
            # Find the longest match in the window
            best_length = 0
            best_offset = 0
            search_end = min(current_pos + self.look_ahead_size, data_length)
            
            # Search in the sliding window
            window_start = max(0, current_pos - self.window_size)
            for offset in range(current_pos - window_start):
                match_length = 0
                while (match_length < self.look_ahead_size and 
                       current_pos + match_length < data_length and
                       data[current_pos - offset - 1 + match_length] == data[current_pos + match_length]):
                    match_length += 1
                
                if match_length > best_length:
                    best_length = match_length
                    best_offset = offset + 1

            # Add compressed token
            if best_length > 2:
                # (offset, length, next_char)
                compressed.append((best_offset, best_length, data[current_pos + best_length]))
                current_pos += best_length + 1
            else:
                # Literal character
                compressed.append(data[current_pos])
                current_pos += 1

        return compressed

    def decompress(self, compressed_data):
        """
        Decompress data compressed with LZSS algorithm.
        
        :param compressed_data: Compressed data from compress method
        :return: Decompressed data as bytes
        """
        decompressed = bytearray()
        
        for token in compressed_data:
            if isinstance(token, tuple):
                # Matched token: (offset, length, next_char)
                offset, length, next_char = token
                start = len(decompressed) - offset
                
                # Copy matched sequence
                for i in range(length):
                    decompressed.append(decompressed[start + i])
                
                # Add next character
                decompressed.append(next_char)
            else:
                # Literal byte
                decompressed.append(token)
        
        return bytes(decompressed)