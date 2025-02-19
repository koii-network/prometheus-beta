class LZVNCompressor:
    """
    LZVN (Lempel-Ziv Variable-length Number) Compression Algorithm Implementation
    
    This is a simplified version of the LZVN compression algorithm.
    """
    
    @staticmethod
    def compress(data):
        """
        Compress input data using LZVN compression algorithm.
        
        Args:
            data (bytes): Input data to be compressed
        
        Returns:
            bytes: Compressed data
        """
        if not isinstance(data, bytes):
            raise TypeError("Input must be bytes")
        
        compressed = bytearray()
        i = 0
        
        while i < len(data):
            # Look ahead for repeated sequences
            best_length = 0
            best_offset = 0
            
            # Search back for matching sequences
            for j in range(max(0, i - 4096), i):
                # Check for potential match
                match_length = 0
                while (i + match_length < len(data) and 
                       data[j + match_length] == data[i + match_length] and 
                       match_length < 255):
                    match_length += 1
                
                # Update best match if found
                if match_length > best_length:
                    best_length = match_length
                    best_offset = i - j
            
            # Encode the result
            if best_length >= 3:
                # Encode a match
                compressed.append(best_length)
                compressed.append(best_offset & 0xFF)
                compressed.append((best_offset >> 8) & 0xFF)
                i += best_length
            else:
                # Encode a literal
                compressed.append(data[i])
                i += 1
        
        return bytes(compressed)
    
    @staticmethod
    def decompress(compressed_data):
        """
        Decompress data that was compressed using LZVN compression.
        
        Args:
            compressed_data (bytes): Compressed input data
        
        Returns:
            bytes: Decompressed data
        """
        if not isinstance(compressed_data, bytes):
            raise TypeError("Input must be bytes")
        
        decompressed = bytearray()
        i = 0
        
        while i < len(compressed_data):
            # Check if it's a match or a literal
            if i + 2 < len(compressed_data) and compressed_data[i] >= 3:
                # It's a match
                length = compressed_data[i]
                offset = (compressed_data[i+2] << 8) | compressed_data[i+1]
                
                # Reconstruct the matched sequence
                start = len(decompressed) - offset
                for j in range(length):
                    decompressed.append(decompressed[start + j])
                
                i += 3
            else:
                # It's a literal
                decompressed.append(compressed_data[i])
                i += 1
        
        return bytes(decompressed)