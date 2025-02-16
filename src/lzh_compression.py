import heapq
from collections import defaultdict

class LZHCompressor:
    def __init__(self):
        self.dictionary = {}
        self.next_code = 256  # Start after ASCII characters

    def compress(self, input_data):
        """
        Implement LZH (Lempel-Ziv-Huffman) compression algorithm.
        
        Args:
            input_data (str or bytes): Data to be compressed
        
        Returns:
            list: Compressed data as a list of codes
        """
        # Convert input to bytes if it's a string
        if isinstance(input_data, str):
            input_data = input_data.encode('utf-8')
        
        # Reset dictionary at the start of compression
        self.dictionary = {bytes([i]): i for i in range(256)}
        self.next_code = 256
        
        compressed = []
        current_sequence = bytes()
        
        for byte in input_data:
            # Create new sequence by adding current byte
            potential_sequence = current_sequence + bytes([byte])
            
            # If the sequence exists in dictionary, extend current sequence
            if potential_sequence in self.dictionary:
                current_sequence = potential_sequence
            else:
                # Output the code for current sequence
                compressed.append(self.dictionary[current_sequence])
                
                # Add new sequence to dictionary
                self.dictionary[potential_sequence] = self.next_code
                self.next_code += 1
                
                # Reset current sequence to last byte
                current_sequence = bytes([byte])
        
        # Output the last sequence
        if current_sequence:
            compressed.append(self.dictionary[current_sequence])
        
        return compressed

    def decompress(self, compressed_data):
        """
        Decompress LZH compressed data.
        
        Args:
            compressed_data (list): List of compressed codes
        
        Returns:
            bytes: Decompressed data
        """
        # Initialize dictionary with single-byte entries
        dictionary = {i: bytes([i]) for i in range(256)}
        next_code = 256
        
        # First code is always output directly
        result = dictionary[compressed_data[0]]
        current_entry = result
        
        # Process the rest of the compressed data
        for code in compressed_data[1:]:
            if code in dictionary:
                # Existing entry
                entry = dictionary[code]
            elif code == next_code:
                # Special case: new sequence based on previous
                entry = current_entry + current_entry[0:1]
            else:
                raise ValueError(f"Invalid compressed code: {code}")
            
            # Output the entry
            result += entry
            
            # Add new dictionary entry
            if current_entry:
                dictionary[next_code] = current_entry + entry[0:1]
                next_code += 1
            
            # Update current entry
            current_entry = entry
        
        return result