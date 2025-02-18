import io
import struct

class LZOCompressor:
    """
    Implement a basic Lempel-Ziv-Oberhumer (LZO) compression algorithm.
    This is a simplified version focusing on the core LZO compression principles.
    """
    @staticmethod
    def compress(data):
        """
        Compress input data using a basic LZO-like compression algorithm.
        
        Args:
            data (bytes): Input data to compress
        
        Returns:
            bytes: Compressed data
        """
        if not isinstance(data, bytes):
            raise TypeError("Input must be bytes")
        
        if not data:
            return b''
        
        compressed = bytearray()
        window_size = 4096  # Typical sliding window size
        look_ahead_buffer = 16  # Look-ahead buffer size
        
        # Add compressed data length as first 4 bytes
        compressed.extend(struct.pack('>I', len(data)))
        
        current_pos = 0
        while current_pos < len(data):
            # Find the longest match in the sliding window
            best_length = 0
            best_offset = 0
            
            # Search back in the window for potential matches
            window_start = max(0, current_pos - window_size)
            for offset in range(current_pos - window_start, 0, -1):
                match_length = 0
                
                # Check for match length
                while (match_length < look_ahead_buffer and 
                       current_pos + match_length < len(data) and 
                       data[current_pos - offset + match_length] == data[current_pos + match_length]):
                    match_length += 1
                
                # Update best match if found
                if match_length > best_length:
                    best_length = match_length
                    best_offset = offset
            
            # If no good match found, output literal byte
            if best_length < 3:
                compressed.append(data[current_pos])
                current_pos += 1
            else:
                # Encode match as (offset, length)
                compressed.append(0xFF)  # Flag for match
                compressed.extend(struct.pack('>H', best_offset))
                compressed.append(best_length)
                current_pos += best_length
        
        return bytes(compressed)
    
    @staticmethod
    def decompress(compressed_data):
        """
        Decompress data compressed with the LZO-like algorithm.
        
        Args:
            compressed_data (bytes): Compressed input data
        
        Returns:
            bytes: Decompressed original data
        """
        if not isinstance(compressed_data, bytes):
            raise TypeError("Input must be bytes")
        
        if not compressed_data:
            return b''
        
        # Read original data length from first 4 bytes
        original_length = struct.unpack('>I', compressed_data[:4])[0]
        decompressed = bytearray()
        
        current_pos = 4
        while current_pos < len(compressed_data):
            # Check if it's a literal or match
            if compressed_data[current_pos] != 0xFF:
                # Literal byte
                decompressed.append(compressed_data[current_pos])
                current_pos += 1
            else:
                # Match: read offset and length
                current_pos += 1
                offset = struct.unpack('>H', compressed_data[current_pos:current_pos+2])[0]
                current_pos += 2
                length = compressed_data[current_pos]
                current_pos += 1
                
                # Copy matched sequence
                start = len(decompressed) - offset
                for i in range(length):
                    decompressed.append(decompressed[start + i])
        
        # Validate decompressed data length
        if len(decompressed) != original_length:
            raise ValueError("Decompression failed: incorrect data length")
        
        return bytes(decompressed)