class LZSS:
    """
    Lempel-Ziv-Storer-Szymanski (LZSS) Compression Algorithm
    
    This implementation uses a sliding window approach for compression.
    """
    
    @staticmethod
    def compress(data):
        """
        Compress input data using LZSS algorithm.
        
        Args:
            data (bytes or str): Input data to compress
        
        Returns:
            bytes: Compressed data
        """
        # Ensure input is bytes
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Compression parameters
        WINDOW_SIZE = 4096  # Size of sliding window
        LOOK_AHEAD_SIZE = 16  # Size of look-ahead buffer
        
        compressed = bytearray()
        window_start = 0
        current_pos = 0
        
        while current_pos < len(data):
            # Find longest match in sliding window
            best_length = 0
            best_offset = 0
            
            # Search back in the window
            search_start = max(0, current_pos - WINDOW_SIZE)
            search_end = current_pos
            
            for i in range(search_start, search_end):
                match_length = 0
                
                # Check how long the match continues
                while (match_length < LOOK_AHEAD_SIZE and 
                       current_pos + match_length < len(data) and 
                       data[i + match_length] == data[current_pos + match_length]):
                    match_length += 1
                
                # Update best match if longer
                if match_length > best_length:
                    best_length = match_length
                    best_offset = current_pos - i
            
            # Encode the result
            if best_length > 2:
                # Encode as (offset, length)
                # Use 12 bits for offset, 4 bits for length
                compressed.append(0)  # Flag for compression
                compressed.append(((best_offset >> 4) & 0xFF))
                compressed.append(((best_offset & 0x0F) << 4) | (best_length & 0x0F))
                current_pos += best_length
            else:
                # Encode as uncompressed literal
                compressed.append(1)  # Flag for literal
                compressed.append(data[current_pos])
                current_pos += 1
        
        return bytes(compressed)
    
    @staticmethod
    def decompress(compressed_data):
        """
        Decompress data compressed with LZSS algorithm.
        
        Args:
            compressed_data (bytes): Compressed input data
        
        Returns:
            bytes: Decompressed data
        """
        decompressed = bytearray()
        i = 0
        
        while i < len(compressed_data):
            # Check compression flag
            if compressed_data[i] == 0:  # Compressed sequence
                if i + 2 >= len(compressed_data):
                    raise ValueError("Incomplete compressed data")
                
                # Extract offset and length
                offset = ((compressed_data[i+1] << 4) | ((compressed_data[i+2] >> 4) & 0x0F))
                length = compressed_data[i+2] & 0x0F
                
                # Copy from previous sequence
                start = len(decompressed) - offset
                for j in range(length):
                    decompressed.append(decompressed[start + j])
                
                i += 3
            else:  # Literal byte
                if i + 1 >= len(compressed_data):
                    raise ValueError("Incomplete compressed data")
                
                decompressed.append(compressed_data[i+1])
                i += 2
        
        return bytes(decompressed)