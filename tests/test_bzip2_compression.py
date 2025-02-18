import os
import pytest
import bz2
from src.bzip2_compression import compress_bzip2, decompress_bzip2

def test_compress_bzip2_string():
    """Test compression of a string"""
    test_data = "Hello, this is a test string for Bzip2 compression!"
    compressed = compress_bzip2(test_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != test_data.encode('utf-8')

def test_compress_bzip2_bytes():
    """Test compression of bytes"""
    test_data = b"Hello, this is a test bytes for Bzip2 compression!"
    compressed = compress_bzip2(test_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != test_data

def test_decompress_bzip2_compressed_data():
    """Test decompression of compressed data"""
    test_data = "Hello, this is a test string for Bzip2 compression!"
    compressed = compress_bzip2(test_data)
    decompressed = decompress_bzip2(compressed)
    assert decompressed.decode('utf-8') == test_data

def test_compress_bzip2_file_output(tmp_path):
    """Test compressing data to a file"""
    test_data = "Hello, this is a test string for Bzip2 compression!"
    output_path = os.path.join(tmp_path, 'compressed.bz2')
    
    result = compress_bzip2(test_data, output_path)
    assert result is None
    assert os.path.exists(output_path)
    
    # Verify the file contents
    with open(output_path, 'rb') as f:
        compressed_data = f.read()
    
    decompressed = bz2.decompress(compressed_data).decode('utf-8')
    assert decompressed == test_data

def test_decompress_bzip2_file_output(tmp_path):
    """Test decompressing data to a file"""
    test_data = "Hello, this is a test string for Bzip2 compression!"
    compressed = compress_bzip2(test_data)
    output_path = os.path.join(tmp_path, 'decompressed.txt')
    
    result = decompress_bzip2(compressed, output_path)
    assert result is None
    assert os.path.exists(output_path)
    
    # Verify the file contents
    with open(output_path, 'r') as f:
        decompressed = f.read()
    
    assert decompressed == test_data

def test_compress_bzip2_invalid_input():
    """Test compression with invalid input type"""
    with pytest.raises(TypeError):
        compress_bzip2(123)

def test_decompress_bzip2_invalid_input():
    """Test decompression with invalid input type"""
    with pytest.raises(TypeError):
        decompress_bzip2(123)

def test_decompress_bzip2_invalid_compressed_data():
    """Test decompression with invalid compressed data"""
    with pytest.raises(bz2.BZ2Error):
        decompress_bzip2(b"Invalid compressed data")