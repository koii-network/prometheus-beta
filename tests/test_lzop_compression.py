import os
import pytest
import tempfile
from src.lzop_compression import lzop_compress, lzop_decompress

def test_lzop_compression_and_decompression():
    # Create a temporary file with test data
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_input:
        test_data = b"Hello, this is a test data for LZOP compression and decompression!"
        temp_input.write(test_data)
        input_path = temp_input.name
    
    try:
        # Compress the file
        compressed_path = lzop_compress(input_path)
        assert os.path.exists(compressed_path)
        assert compressed_path.endswith('.lzo')
        assert os.path.getsize(compressed_path) < os.path.getsize(input_path)
        
        # Decompress the file
        decompressed_path = lzop_decompress(compressed_path)
        assert os.path.exists(decompressed_path)
        
        # Verify decompressed content matches original
        with open(decompressed_path, 'rb') as f:
            decompressed_data = f.read()
        
        assert decompressed_data == test_data
    
    finally:
        # Clean up temporary files
        for path in [input_path, compressed_path, decompressed_path]:
            if os.path.exists(path):
                os.unlink(path)

def test_compress_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        lzop_compress('/path/to/nonexistent/file.txt')

def test_decompress_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        lzop_decompress('/path/to/nonexistent/file.lzo')

def test_custom_output_paths():
    # Create a temporary file with test data
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_input:
        test_data = b"Testing custom output paths for LZOP compression"
        temp_input.write(test_data)
        input_path = temp_input.name
    
    try:
        # Custom compressed output path
        custom_compressed = input_path + '.custom.lzo'
        compressed_path = lzop_compress(input_path, custom_compressed)
        assert compressed_path == custom_compressed
        
        # Custom decompressed output path
        custom_decompressed = input_path + '.custom'
        decompressed_path = lzop_decompress(compressed_path, custom_decompressed)
        assert decompressed_path == custom_decompressed
        
        # Verify decompressed content
        with open(decompressed_path, 'rb') as f:
            decompressed_data = f.read()
        
        assert decompressed_data == test_data
    
    finally:
        # Clean up temporary files
        for path in [input_path, custom_compressed, custom_decompressed]:
            if os.path.exists(path):
                os.unlink(path)