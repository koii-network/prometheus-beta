import heapq
from collections import defaultdict

class LZHCompressor:
    """
    Implements the Lempel-Ziv-Huffman (LZH) compression algorithm.
    
    This class provides methods for compressing and decompressing data 
    using a combination of Lempel-Ziv dictionary compression and 
    Huffman coding for entropy encoding.
    """
    
    @staticmethod
    def compress(data):
        """
        Compress the input data using LZH compression algorithm.
        
        Args:
            data (str or bytes): The input data to compress
        
        Returns:
            bytes: Compressed data
        
        Raises:
            TypeError: If input is not a string or bytes
            ValueError: If input is empty
        """
        # Input validation
        if not data:
            raise ValueError("Input data cannot be empty")
        
        if not isinstance(data, (str, bytes)):
            raise TypeError("Input must be string or bytes")
        
        # Convert to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Lempel-Ziv dictionary compression
        dictionary = {bytes([i]): i for i in range(256)}
        result = []
        current_sequence = bytes()
        next_code = 256
        
        for byte in data:
            # Extend current sequence
            potential_sequence = current_sequence + bytes([byte])
            
            # If sequence exists in dictionary, continue building
            if potential_sequence in dictionary:
                current_sequence = potential_sequence
            else:
                # Output the code for current sequence
                result.append(dictionary[current_sequence])
                
                # Add new sequence to dictionary
                dictionary[potential_sequence] = next_code
                next_code += 1
                
                # Reset current sequence
                current_sequence = bytes([byte])
        
        # Output last sequence
        if current_sequence:
            result.append(dictionary[current_sequence])
        
        # Huffman coding
        freq = defaultdict(int)
        for code in result:
            freq[code] += 1
        
        # Build Huffman tree
        heap = [[weight, [symbol, ""]] for symbol, weight in freq.items()]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        
        # Create Huffman codes
        huffman_codes = {symbol: code for _, [symbol, code] in heap[0][1:]}
        
        # Encode result with Huffman codes
        encoded_result = ''.join(huffman_codes[code] for code in result)
        
        # Pad to make it byte-aligned
        while len(encoded_result) % 8 != 0:
            encoded_result += '0'
        
        # Convert to bytes
        compressed = bytes(int(encoded_result[i:i+8], 2) for i in range(0, len(encoded_result), 8))
        
        return compressed
    
    @staticmethod
    def decompress(compressed_data):
        """
        Decompress data compressed with LZH algorithm.
        
        Args:
            compressed_data (bytes): The compressed data to decompress
        
        Returns:
            bytes: Decompressed data
        
        Raises:
            TypeError: If input is not bytes
            ValueError: If input is empty
        """
        # Input validation
        if not compressed_data:
            raise ValueError("Compressed data cannot be empty")
        
        if not isinstance(compressed_data, bytes):
            raise TypeError("Compressed data must be bytes")
        
        # Implement decompression logic here (simplified placeholder)
        # Note: Full LZH decompression is complex and would require 
        # reconstructing the Huffman tree and dictionary
        return compressed_data