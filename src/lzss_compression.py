"""
LZSS (Lempel-Ziv-Storer-Szymanski) Compression Algorithm Implementation.

This module provides functions for LZSS compression and decompression.
"""

class LZSSCompressor:
    def __init__(self, window_size=4096, lookahead_size=16):
        """
        Initialize the LZSS compressor.
        
        :param window_size: Size of the sliding window for searching previous matches
        :param lookahead_size: Size of the lookahead buffer for finding matches
        """
        self.window_size = window_size
        self.lookahead_size = lookahead_size

    def compress(self, data):
        """
        Compress the input data using LZSS algorithm.
        
        :param data: Input data to compress (bytes or bytearray)
        :return: Compressed data as bytes
        """
        if not data:
            return b''
        
        # Convert input to bytearray for manipulation
        data = bytearray(data)
        compressed = bytearray()
        
        # Initialize window and lookahead
        start = 0
        current = 0
        
        while current < len(data):
            # Find the longest match in the sliding window
            best_match_length = 0
            best_match_offset = 0
            
            # Define search range in the sliding window
            window_start = max(0, current - self.window_size)
            window_end = current
            
            # Search for the longest match
            for i in range(window_start, window_end):
                match_length = 0
                
                # Check for match length
                while (match_length < self.lookahead_size and 
                       current + match_length < len(data) and 
                       data[i + match_length] == data[current + match_length]):
                    match_length += 1
                
                # Update best match if found
                if match_length > best_match_length:
                    best_match_length = match_length
                    best_match_offset = current - i
            
            # Encode the result
            if best_match_length > 2:
                # Encode as a match: (offset, length)
                compressed.append(0)  # Match flag
                # 12 bits for offset, 4 bits for length
                compressed.append((best_match_offset >> 4) & 0xFF)
                compressed.append(((best_match_offset & 0x0F) << 4) | (best_match_length - 3))
                current += best_match_length
            else:
                # Encode as a literal
                compressed.append(1)  # Literal flag
                compressed.append(data[current])
                current += 1
        
        return bytes(compressed)

    def decompress(self, compressed_data):
        """
        Decompress LZSS compressed data.
        
        :param compressed_data: Compressed data to decompress
        :return: Decompressed data as bytes
        """
        if not compressed_data:
            return b''
        
        decompressed = bytearray()
        i = 0
        
        while i < len(compressed_data):
            # Check flag for match or literal
            flag = compressed_data[i]
            i += 1
            
            if flag == 0:  # Match
                if i + 1 >= len(compressed_data):
                    break
                
                # Extract offset and length
                offset_high = compressed_data[i]
                i += 1
                offset_low_and_length = compressed_data[i]
                i += 1
                
                # Reconstruct offset and length
                offset = (offset_high << 4) | ((offset_low_and_length >> 4) & 0x0F)
                length = (offset_low_and_length & 0x0F) + 3
                
                # Reconstruct matched sequence
                start = len(decompressed) - offset
                for j in range(length):
                    decompressed.append(decompressed[start + j])
            
            elif flag == 1:  # Literal
                if i >= len(compressed_data):
                    break
                decompressed.append(compressed_data[i])
                i += 1
            
            else:
                # Invalid flag
                raise ValueError(f"Invalid compression flag: {flag}")
        
        return bytes(decompressed)