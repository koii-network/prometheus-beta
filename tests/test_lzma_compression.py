import os
import pytest
import lzma
from src.lzma_compression import compress_lzma, decompress_lzma

def test_compress_lzma_string():
    """Test compressing a string input"""
    test_str = "Hello, world! This is a test of LZMA compression."
    compressed = compress_lzma(test_str)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != test_str.encode('utf-8')

def test_compress_lzma_bytes():
    """Test compressing bytes input"""
    test_bytes = b"Hello, world! This is a test of LZMA compression."
    compressed = compress_lzma(test_bytes)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != test_bytes

def test_compress_lzma_to_file(tmp_path):
    """Test compressing to a file"""
    test_str = "Hello, world! This is a test of LZMA compression."
    output_path = tmp_path / "compressed.lzma"
    result = compress_lzma(test_str, str(output_path))
    
    assert result is None
    assert os.path.exists(output_path)
    assert os.path.getsize(output_path) > 0

def test_decompress_lzma_bytes():
    """Test decompressing bytes"""
    test_str = "Hello, world! This is a test of LZMA compression."
    compressed = compress_lzma(test_str)
    decompressed = decompress_lzma(compressed)
    
    assert decompressed.decode('utf-8') == test_str

def test_decompress_lzma_from_file(tmp_path):
    """Test decompressing from a file"""
    test_str = "Hello, world! This is a test of LZMA compression."
    output_path = tmp_path / "compressed.lzma"
    
    # Compress to file
    compress_lzma(test_str, str(output_path))
    
    # Decompress from file
    decompressed = decompress_lzma(str(output_path))
    assert decompressed.decode('utf-8') == test_str

def test_compress_empty_input():
    """Test compressing empty input raises ValueError"""
    with pytest.raises(ValueError):
        compress_lzma("")
    with pytest.raises(ValueError):
        compress_lzma(b"")

def test_decompress_empty_input():
    """Test decompressing empty input raises ValueError"""
    with pytest.raises(ValueError):
        decompress_lzma("")
    with pytest.raises(ValueError):
        decompress_lzma(b"")

def test_compress_invalid_input():
    """Test compressing invalid input type raises TypeError"""
    with pytest.raises(TypeError):
        compress_lzma(123)
    with pytest.raises(TypeError):
        compress_lzma(None)

def test_decompress_invalid_input():
    """Test decompressing invalid input type raises TypeError"""
    with pytest.raises(TypeError):
        decompress_lzma(123)
    with pytest.raises(TypeError):
        decompress_lzma(None)

def test_round_trip_compression():
    """Test full compression and decompression round trip"""
    test_str = "Hello, world! This is a test of LZMA compression."
    compressed = compress_lzma(test_str)
    decompressed = decompress_lzma(compressed)
    
    assert decompressed.decode('utf-8') == test_str