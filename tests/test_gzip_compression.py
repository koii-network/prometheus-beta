import os
import gzip
import pytest
from src.gzip_compression import compress_file, decompress_file

def test_compress_file(tmp_path):
    # Create a test file
    input_file = tmp_path / 'test_input.txt'
    input_file.write_text('This is a test file for compression')
    
    # Compress the file
    compressed_path = compress_file(str(input_file))
    
    # Verify compression
    assert os.path.exists(compressed_path)
    assert compressed_path.endswith('.gz')
    
    # Check file size (compressed should be smaller)
    original_size = os.path.getsize(str(input_file))
    compressed_size = os.path.getsize(compressed_path)
    assert compressed_size < original_size

def test_decompress_file(tmp_path):
    # Create a test file
    input_file = tmp_path / 'test_input.txt'
    input_file.write_text('This is a test file for compression')
    
    # Compress the file
    compressed_path = compress_file(str(input_file))
    
    # Decompress the file
    decompressed_path = decompress_file(compressed_path)
    
    # Verify decompression
    assert os.path.exists(decompressed_path)
    
    # Check content
    with open(str(input_file), 'rb') as original, open(decompressed_path, 'rb') as decompressed:
        assert original.read() == decompressed.read()

def test_nonexistent_input_file():
    with pytest.raises(FileNotFoundError):
        compress_file('/path/to/nonexistent/file.txt')

def test_custom_output_path(tmp_path):
    # Create a test file
    input_file = tmp_path / 'test_input.txt'
    input_file.write_text('This is a test file for compression')
    
    # Custom output path
    custom_output = tmp_path / 'custom_compressed.gz'
    compressed_path = compress_file(str(input_file), str(custom_output))
    
    # Verify custom path
    assert compressed_path == str(custom_output)
    assert os.path.exists(compressed_path)

def test_compression_decompression_cycle(tmp_path):
    # Create a test file with varied content
    input_file = tmp_path / 'test_input.txt'
    test_content = 'This is a test file for compression and decompression cycle'
    input_file.write_text(test_content)
    
    # Compress
    compressed_path = compress_file(str(input_file))
    
    # Decompress
    decompressed_path = decompress_file(compressed_path)
    
    # Read decompressed content
    with open(decompressed_path, 'r') as f:
        assert f.read() == test_content