class LZ77Compressor:
    def __init__(self, window_size=1024, lookahead_buffer_size=16):
        """
        Initialize LZ77 Compressor
        
        :param window_size: Size of the sliding window (dictionary)
        :param lookahead_buffer_size: Size of the lookahead buffer
        """
        self.window_size = window_size
        self.lookahead_buffer_size = lookahead_buffer_size

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
        window_start = 0
        current_pos = 0

        while current_pos < len(data):
            # Define search window and lookahead buffer
            window_end = max(0, current_pos - self.window_size)
            lookahead_end = min(len(data), current_pos + self.lookahead_buffer_size)

            best_length = 0
            best_offset = 0
            next_char = data[current_pos]

            # Search for longest match in the window
            for offset in range(current_pos - window_end, 0, -1):
                match_length = 0
                
                # Check for matching sequences
                while (match_length < lookahead_end - current_pos and
                       data[current_pos + match_length] == 
                       data[current_pos - offset + match_length]):
                    match_length += 1
                    
                    # Break if match length exceeds buffer size
                    if match_length >= self.lookahead_buffer_size:
                        break

                # Update best match if found
                if match_length > best_length:
                    best_length = match_length
                    best_offset = offset
                    
                    # If at end of buffer, take next char
                    if current_pos + match_length < len(data):
                        next_char = data[current_pos + match_length]

            # Add compressed token
            compressed.append((best_offset, best_length, next_char))

            # Move position forward
            current_pos += best_length + 1

        return compressed

    def decompress(self, compressed_data):
        """
        Decompress LZ77 compressed data
        
        :param compressed_data: List of tuples (offset, length, next_char)
        :return: Decompressed bytes
        """
        decompressed = bytearray()

        for offset, length, next_char in compressed_data:
            if length > 0:
                # Copy sequence from previous data
                start = len(decompressed) - offset
                for i in range(length):
                    decompressed.append(decompressed[start + i])
            
            # Append next character
            decompressed.append(next_char)

        return bytes(decompressed)