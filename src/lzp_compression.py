"""
LZP (Lempel-Ziv Prediction) Compression Algorithm Implementation.

This module provides functions for LZP compression and decompression.
"""

class LZPCompressor:
    """
    Implements Lempel-Ziv Prediction (LZP) compression algorithm.
    
    The algorithm works by maintaining a context-based prediction model
    and encoding the difference between predicted and actual characters.
    """
    
    def __init__(self, context_length=8, dictionary_size=4096):
        """
        Initialize the LZP compressor.
        
        :param context_length: Length of context used for prediction (default: 8)
        :param dictionary_size: Size of the prediction dictionary (default: 4096)
        """
        self.context_length = context_length
        self.dictionary_size = dictionary_size
    
    def compress(self, data):
        """
        Compress the input data using LZP algorithm.
        
        :param data: Input data to compress (bytes or string)
        :return: Compressed data
        """
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Validate input
        if not data:
            return b''
        
        # Initialize prediction dictionary
        context_dict = {}
        compressed = bytearray()
        context = b''
        
        for byte in data:
            # Create context key
            context_key = context[-self.context_length:] if context else b''
            
            # Predict the byte based on context
            predicted_byte = context_dict.get(context_key, 0)
            
            # Calculate the XOR difference
            diff = byte ^ predicted_byte
            
            # Add difference to compressed output
            compressed.append(diff)
            
            # Update context dictionary
            context_dict[context_key] = byte
            
            # Update context
            context += bytes([byte])
            if len(context) > self.context_length:
                context = context[-self.context_length:]
        
        return bytes(compressed)
    
    def decompress(self, compressed_data):
        """
        Decompress data compressed with LZP algorithm.
        
        :param compressed_data: Compressed input data
        :return: Decompressed data
        """
        # Validate input
        if not compressed_data:
            return b''
        
        # Initialize prediction dictionary
        context_dict = {}
        decompressed = bytearray()
        context = b''
        
        for diff in compressed_data:
            # Create context key
            context_key = context[-self.context_length:] if context else b''
            
            # Predict the byte based on context
            predicted_byte = context_dict.get(context_key, 0)
            
            # Recover original byte using XOR
            byte = diff ^ predicted_byte
            
            # Add byte to decompressed output
            decompressed.append(byte)
            
            # Update context dictionary
            context_dict[context_key] = byte
            
            # Update context
            context += bytes([byte])
            if len(context) > self.context_length:
                context = context[-self.context_length:]
        
        return bytes(decompressed)

def compress_lzp(data, context_length=8, dictionary_size=4096):
    """
    Convenience function for LZP compression.
    
    :param data: Input data to compress
    :param context_length: Length of context used for prediction
    :param dictionary_size: Size of the prediction dictionary
    :return: Compressed data
    """
    compressor = LZPCompressor(context_length, dictionary_size)
    return compressor.compress(data)

def decompress_lzp(compressed_data, context_length=8, dictionary_size=4096):
    """
    Convenience function for LZP decompression.
    
    :param compressed_data: Compressed input data
    :param context_length: Length of context used for prediction
    :param dictionary_size: Size of the prediction dictionary
    :return: Decompressed data
    """
    compressor = LZPCompressor(context_length, dictionary_size)
    return compressor.decompress(compressed_data)