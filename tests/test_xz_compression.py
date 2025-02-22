import os
import pytest
import tempfile
from src.xz_compression import compress_xz, decompress_xz

def test_compress_decompress_bytes():
    """Test compression and decompression of bytes data"""
    original_data = b"Hello, this is a test of XZ compression!"
    compressed = compress_xz(original_data)
    decompressed = decompress_xz(compressed)
    assert decompressed == original_data

def test_compress_decompress_string():
    """Test compression and decompression of string data"""
    original_data = "Hello, this is a test of XZ compression!"
    compressed = compress_xz(original_data)
    decompressed = decompress_xz(compressed)
    assert decompressed == original_data.encode('utf-8')

def test_compress_to_file():
    """Test compression to a file"""
    with tempfile.TemporaryDirectory() as tmpdir:
        original_data = b"Compress to file test"
        output_path = os.path.join(tmpdir, 'compressed.xz')
        
        compress_xz(original_data, output_path)
        assert os.path.exists(output_path)
        
        with open(output_path, 'rb') as f:
            compressed_data = f.read()
        
        decompressed = decompress_xz(compressed_data)
        assert decompressed == original_data

def test_decompress_from_file():
    """Test decompression from a file"""
    with tempfile.TemporaryDirectory() as tmpdir:
        original_data = b"Decompress from file test"
        compressed_path = os.path.join(tmpdir, 'compressed.xz')
        decompressed_path = os.path.join(tmpdir, 'decompressed.txt')
        
        # Compress to file
        compress_xz(original_data, compressed_path)
        
        # Decompress from file
        decompress_xz(compressed_path, decompressed_path)
        
        with open(decompressed_path, 'rb') as f:
            decompressed_data = f.read()
        
        assert decompressed_data == original_data

def test_compression_levels():
    """Test different compression levels"""
    data = b"Test compression levels"
    
    # Test valid compression levels
    for level in range(10):
        compressed = compress_xz(data, compression_level=level)
        decompressed = decompress_xz(compressed)
        assert decompressed == data

def test_invalid_compression_level():
    """Test invalid compression level raises ValueError"""
    with pytest.raises(ValueError):
        compress_xz(b"Test", compression_level=-1)
    
    with pytest.raises(ValueError):
        compress_xz(b"Test", compression_level=10)

def test_invalid_input_type():
    """Test invalid input types raise TypeError"""
    with pytest.raises(TypeError):
        compress_xz(123)
    
    with pytest.raises(TypeError):
        decompress_xz(123)

def test_empty_data():
    """Test compression and decompression of empty data"""
    empty_data = b""
    compressed = compress_xz(empty_data)
    decompressed = decompress_xz(compressed)
    assert decompressed == empty_data