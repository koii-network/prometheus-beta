import io
import struct

class LZHCompressor:
    """
    LZH (Lempel-Ziv-Huffman) Compression implementation
    """
    
    @staticmethod
    def compress(data):
        """
        Compress input data using LZH compression algorithm
        
        Args:
            data (bytes): Input data to compress
        
        Returns:
            bytes: Compressed data
        """
        if not isinstance(data, bytes):
            raise TypeError("Input must be bytes")
        
        if not data:
            return b''
        
        # Sliding window for repeated sequences
        window_size = 4096
        look_ahead_size = 16
        
        compressed = bytearray()
        buffer = io.BytesIO(data)
        
        # Initial dictionary
        dictionary = {}
        
        while True:
            # Read current window
            current_pos = buffer.tell()
            window = data[max(0, current_pos - window_size):current_pos]
            
            # Look ahead buffer
            look_ahead = buffer.read(look_ahead_size)
            if not look_ahead:
                break
            
            # Find longest match
            best_length = 0
            best_offset = 0
            
            for i in range(len(window)):
                match_length = 0
                while (match_length < len(look_ahead) and 
                       window[len(window)-i-match_length-1] == look_ahead[match_length]):
                    match_length += 1
                    if match_length >= len(look_ahead):
                        break
                
                if match_length > best_length:
                    best_length = match_length
                    best_offset = i + 1
            
            if best_length > 2:
                # Encode match
                compressed.extend(struct.pack('&lt;H', best_offset))
                compressed.extend(struct.pack('B', best_length))
                buffer.seek(current_pos + best_length)
            else:
                # Encode single byte
                compressed.append(look_ahead[0])
                buffer.seek(current_pos + 1)
        
        return bytes(compressed)
    
    @staticmethod
    def decompress(compressed_data):
        """
        Decompress LZH compressed data
        
        Args:
            compressed_data (bytes): Compressed input data
        
        Returns:
            bytes: Decompressed data
        """
        if not isinstance(compressed_data, bytes):
            raise TypeError("Input must be bytes")
        
        if not compressed_data:
            return b''
        
        decompressed = bytearray()
        buffer = io.BytesIO(compressed_data)
        
        while True:
            try:
                # Try to read an offset
                offset_bytes = buffer.read(2)
                if len(offset_bytes) < 2:
                    break
                
                offset = struct.unpack('&lt;H', offset_bytes)[0]
                
                # Read length
                length_byte = buffer.read(1)
                if not length_byte:
                    break
                
                length = struct.unpack('B', length_byte)[0]
                
                # Reconstruct sequence
                start = len(decompressed) - offset
                for i in range(length):
                    decompressed.append(decompressed[start + i])
            
            except struct.error:
                # If no match found, treat as single byte
                byte = buffer.read(1)
                if not byte:
                    break
                decompressed.append(byte[0])
        
        return bytes(decompressed)