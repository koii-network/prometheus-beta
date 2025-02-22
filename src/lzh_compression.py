import io
import struct

class LZHCompressor:
    """
    LZH (Lempel-Ziv-Huffman) Compression implementation
    """
    def __init__(self, window_size=4096):
        """
        Initialize LZH compressor
        :param window_size: Size of the sliding window for compression
        """
        self.window_size = window_size

    def compress(self, data):
        """
        Compress input data using LZH algorithm
        :param data: Input data to compress (bytes or string)
        :return: Compressed data
        """
        if isinstance(data, str):
            data = data.encode('utf-8')

        compressed = bytearray()
        buffer = data
        pos = 0

        while pos < len(buffer):
            # Find longest match in sliding window
            best_length = 0
            best_offset = 0
            
            # Define search range in sliding window
            search_start = max(0, pos - self.window_size)
            search_end = pos

            for j in range(search_start, search_end):
                current_length = 0
                
                # Extend match as long as possible
                while (pos + current_length < len(buffer) and 
                       buffer[j + current_length] == buffer[pos + current_length] and 
                       current_length < 255):
                    current_length += 1
                
                # Update best match if longer
                if current_length > best_length:
                    best_length = current_length
                    best_offset = pos - j

            # Encode match or literal
            if best_length > 2:
                # Encode as (offset, length) pair
                compressed.extend(struct.pack('<HB', best_offset, best_length))
                pos += best_length
            else:
                # Encode as literal byte
                compressed.append(buffer[pos])
                pos += 1

        return bytes(compressed)

    def decompress(self, compressed_data):
        """
        Decompress LZH compressed data
        :param compressed_data: Compressed input data
        :return: Decompressed data
        """
        decompressed = bytearray()
        pos = 0

        while pos < len(compressed_data):
            # Check if we have a match or literal
            if pos + 3 <= len(compressed_data):
                try:
                    offset, length = struct.unpack('<HB', compressed_data[pos:pos+3])
                    
                    # If valid match, copy from previous data
                    if length > 2:
                        start = len(decompressed) - offset
                        for i in range(length):
                            decompressed.append(decompressed[start + i])
                        pos += 3
                        continue
                except struct.error:
                    pass

            # Otherwise, treat as literal byte
            decompressed.append(compressed_data[pos])
            pos += 1

        return bytes(decompressed)