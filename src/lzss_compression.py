"""
Lempel-Ziv-Storer-Szymanski (LZSS) Compression Algorithm Implementation

This module provides functions for LZSS data compression and decompression.
LZSS is a dictionary-based compression algorithm that replaces repeated 
sequences with references to previous occurrences.
"""

class LZSSCompressor:
    def __init__(self, window_size=4096, lookahead_size=16, min_match_length=3):
        """
        Initialize the LZSS compressor.
        
        Args:
            window_size (int): Size of the sliding window for searching previous matches.
            lookahead_size (int): Size of the lookahead buffer for finding matches.
            min_match_length (int): Minimum length of match to use compression.
        """
        self.window_size = window_size
        self.lookahead_size = lookahead_size
        self.min_match_length = min_match_length
    
    def compress(self, data):
        """
        Compress input data using LZSS algorithm.
        
        Args:
            data (bytes or str): Input data to compress.
        
        Returns:
            bytes: Compressed data.
        
        Raises:
            TypeError: If input is not bytes or str.
        """
        # Convert to bytes if input is a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        if not isinstance(data, bytes):
            raise TypeError("Input must be bytes or str")
        
        # If data is too short to compress, return as-is
        if len(data) <= self.min_match_length:
            return data
        
        compressed = bytearray()
        data_length = len(data)
        current_pos = 0
        
        while current_pos < data_length:
            # Look for the longest match in the window
            best_length = 0
            best_offset = 0
            
            # Define search range (window)
            window_start = max(0, current_pos - self.window_size)
            window_end = current_pos
            
            # Look for longest match in the window
            for offset in range(window_start, window_end):
                match_length = 0
                while (match_length < self.lookahead_size and 
                       current_pos + match_length < data_length and 
                       data[offset + match_length] == data[current_pos + match_length]):
                    match_length += 1
                
                # Update best match if found
                if match_length > best_length and match_length >= self.min_match_length:
                    best_length = match_length
                    best_offset = current_pos - offset
            
            # Encode the result
            if best_length >= self.min_match_length:  # Minimum match length to compress
                # Encode as (offset, length)
                compressed.append(0)  # Flag for match
                compressed.append(best_offset & 0xFF)  # Lower byte of offset
                compressed.append((best_offset >> 8) & 0xFF)  # Upper byte of offset
                compressed.append(best_length)
                current_pos += best_length
            else:
                # Encode as literal
                compressed.append(1)  # Flag for literal
                compressed.append(data[current_pos])
                current_pos += 1
        
        return bytes(compressed)
    
    def decompress(self, compressed_data):
        """
        Decompress data compressed with LZSS algorithm.
        
        Args:
            compressed_data (bytes): Data to decompress.
        
        Returns:
            bytes: Decompressed data.
        
        Raises:
            TypeError: If input is not bytes.
            ValueError: If compressed data is invalid.
        """
        if not isinstance(compressed_data, bytes):
            raise TypeError("Input must be bytes")
        
        # If compressed data is too short, return as-is
        if len(compressed_data) <= 1:
            return compressed_data
        
        decompressed = bytearray()
        i = 0
        
        while i < len(compressed_data):
            # Check for compressed or literal flag
            if i + 1 >= len(compressed_data):
                break
            
            flag = compressed_data[i]
            i += 1
            
            if flag == 0:  # Compressed (match)
                # Ensure enough bytes for offset and length
                if i + 3 > len(compressed_data):
                    raise ValueError("Invalid compressed data")
                
                # Reconstruct offset and length
                offset = compressed_data[i] | (compressed_data[i+1] << 8)
                length = compressed_data[i+2]
                i += 3
                
                # Validate offset and length
                if offset == 0 or length == 0:
                    raise ValueError("Invalid offset or length")
                
                # Decode match
                start = len(decompressed) - offset
                for j in range(length):
                    if start + j < 0:
                        raise ValueError("Invalid decompression")
                    decompressed.append(decompressed[start + j])
            
            elif flag == 1:  # Literal
                if i >= len(compressed_data):
                    raise ValueError("Invalid compressed data")
                decompressed.append(compressed_data[i])
                i += 1
            
            else:
                raise ValueError(f"Invalid compression flag: {flag}")
        
        return bytes(decompressed)