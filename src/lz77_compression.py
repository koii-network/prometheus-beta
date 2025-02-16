class LZ77Compressor:
    def __init__(self, window_size=1024, lookahead_buffer_size=16):
        """
        Initialize LZ77 compressor with configurable window and lookahead buffer sizes
        
        :param window_size: Size of the sliding window for finding matches
        :param lookahead_buffer_size: Size of the lookahead buffer for finding matches
        """
        self.window_size = window_size
        self.lookahead_buffer_size = lookahead_buffer_size

    def compress(self, input_data):
        """
        Compress input data using LZ77 algorithm
        
        :param input_data: String or bytes to compress
        :return: List of tuples representing compressed data (offset, length, next_char)
        """
        if input_data is None:
            raise TypeError("Input data cannot be None")
        
        if not isinstance(input_data, (str, bytes)):
            raise TypeError("Input must be a string or bytes")

        if not input_data:
            return []

        # Convert input to bytes if it's a string
        if isinstance(input_data, str):
            input_data = input_data.encode('utf-8')

        compressed = []
        input_length = len(input_data)
        current_index = 0

        while current_index < input_length:
            # Define search window and look-ahead buffer
            search_start = max(0, current_index - self.window_size)
            search_end = current_index
            lookahead_end = min(current_index + self.lookahead_buffer_size, input_length)

            # Find the longest match in the search window
            best_length = 0
            best_offset = 0
            search_window = input_data[search_start:search_end]
            lookahead_buffer = input_data[current_index:lookahead_end]

            # Check each possible offset in the search window
            for offset in range(1, len(search_window) + 1):
                match_length = 0
                
                # Find the maximum match length
                while (match_length < len(lookahead_buffer) and 
                       match_length < offset and 
                       search_window[-offset + match_length] == 
                       lookahead_buffer[match_length]):
                    match_length += 1
                
                # Update best match if necessary
                if match_length > best_length:
                    best_length = match_length
                    best_offset = offset

            # Encode match or literal
            if best_length > 0:
                next_char = lookahead_buffer[best_length] if best_length < len(lookahead_buffer) else None
                compressed.append((best_offset, best_length, next_char))
                current_index += best_length + 1
            else:
                # No match found, encode literal
                compressed.append((0, 0, input_data[current_index]))
                current_index += 1

        return compressed

    def decompress(self, compressed_data):
        """
        Decompress data compressed with LZ77 algorithm
        
        :param compressed_data: List of tuples from compression
        :return: Decompressed bytes
        """
        if not compressed_data:
            return b''

        decompressed = bytearray()

        for offset, length, next_char in compressed_data:
            if length == 0 and offset == 0:
                # Literal character
                decompressed.append(next_char if isinstance(next_char, int) else ord(next_char))
            else:
                # Backreference
                start = len(decompressed) - offset
                for i in range(length):
                    decompressed.append(decompressed[start + i])
                
                if next_char is not None:
                    decompressed.append(next_char if isinstance(next_char, int) else ord(next_char))

        return bytes(decompressed)