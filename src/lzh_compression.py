import heapq
from collections import defaultdict

class LZHCompressor:
    """
    Implements the Lempel-Ziv-Huffman (LZH) compression algorithm.
    
    This implementation provides methods for both compression and decompression 
    using a combination of Lempel-Ziv dictionary-based compression and 
    Huffman coding for final encoding.
    """
    
    def __init__(self):
        # LZ dictionary for encoding and decoding
        self.dictionary = {}
        self.next_code = 256  # Start after ASCII characters
    
    def _build_huffman_tree(self, freq):
        """
        Build a Huffman tree based on character frequencies.
        
        Args:
            freq (dict): A dictionary of character frequencies
        
        Returns:
            dict: Huffman codes for each character
        """
        heap = [[weight, [char, ""]] for char, weight in freq.items()]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        
        # Convert to code dictionary
        huffman_codes = dict(heap[0][1:])
        return huffman_codes
    
    def compress(self, data):
        """
        Compress the input data using LZH algorithm.
        
        Args:
            data (str): Input data to compress
        
        Returns:
            tuple: Compressed data and Huffman codes
        """
        if not data:
            return "", {}
        
        # Reset dictionary
        self.dictionary = {chr(i): i for i in range(256)}
        self.next_code = 256
        
        # LZ compression phase
        compressed = []
        current_sequence = ""
        
        for char in data:
            current_sequence += char
            if current_sequence not in self.dictionary:
                # Output the code for the sequence without the last character
                compressed.append(self.dictionary[current_sequence[:-1]])
                
                # Add new sequence to dictionary
                self.dictionary[current_sequence] = self.next_code
                self.next_code += 1
                
                # Reset current sequence to last character
                current_sequence = char
        
        # Add last sequence
        if current_sequence:
            compressed.append(self.dictionary[current_sequence])
        
        # Huffman encoding phase
        # Calculate frequencies
        freq = defaultdict(int)
        for code in compressed:
            freq[code] += 1
        
        # Build Huffman codes
        huffman_codes = self._build_huffman_tree(freq)
        
        # Encode with Huffman codes
        huffman_compressed = []
        for code in compressed:
            huffman_compressed.append(huffman_codes[code])
        
        return ''.join(huffman_compressed), huffman_codes
    
    def decompress(self, compressed_data, huffman_codes):
        """
        Decompress data using the stored Huffman codes and LZ dictionary.
        
        Args:
            compressed_data (str): Huffman-encoded compressed data
            huffman_codes (dict): Huffman codes used for encoding
        
        Returns:
            str: Decompressed original data
        """
        if not compressed_data:
            return ""
        
        # Reverse Huffman codes
        reverse_huffman = {code: char for char, code in huffman_codes.items()}
        
        # Decode Huffman
        current_code = ""
        decoded_codes = []
        for bit in compressed_data:
            current_code += bit
            if current_code in reverse_huffman:
                decoded_codes.append(reverse_huffman[current_code])
                current_code = ""
        
        # LZ decompression
        # Reset dictionary
        dictionary = {i: chr(i) for i in range(256)}
        next_code = 256
        
        # Reconstruct original data
        result = []
        previous = decoded_codes[0]
        result.append(dictionary[previous])
        
        for code in decoded_codes[1:]:
            if code in dictionary:
                entry = dictionary[code]
            elif code == next_code:
                entry = dictionary[previous] + dictionary[previous][0]
            else:
                raise ValueError("Invalid compressed data")
            
            result.append(entry)
            
            # Add new dictionary entry
            dictionary[next_code] = dictionary[previous] + entry[0]
            next_code += 1
            
            previous = code
        
        return ''.join(result)