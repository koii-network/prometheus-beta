import os
import pytest
import bz2
from src.bzip2_compression import compress_bzip2, decompress_bzip2

def test_compress_string():
    """Test compressing a string"""
    input_data = "Hello, world! This is a test of Bzip2 compression."
    compressed = compress_bzip2(input_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != input_data.encode('utf-8')

def test_compress_bytes():
    """Test compressing bytes"""
    input_data = b"Binary data for compression test"
    compressed = compress_bzip2(input_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != input_data

def test_decompress_bytes():
    """Test decompressing bytes"""
    input_data = "Hello, world! This is a test of Bzip2 compression."
    compressed = compress_bzip2(input_data)
    decompressed = decompress_bzip2(compressed)
    assert decompressed.decode('utf-8') == input_data

def test_compress_to_file(tmp_path):
    """Test compressing to a file"""
    input_data = "Compress to file test"
    output_path = tmp_path / "compressed.bz2"
    compress_bzip2(input_data, str(output_path))
    assert os.path.exists(output_path)
    assert os.path.getsize(output_path) > 0

def test_decompress_from_file(tmp_path):
    """Test decompressing from a file"""
    input_data = "Decompress from file test"
    compressed_path = tmp_path / "compressed.bz2"
    decompressed_path = tmp_path / "decompressed.txt"
    
    # Compress to file
    compress_bzip2(input_data, str(compressed_path))
    
    # Decompress from file
    decompress_bzip2(str(compressed_path), str(decompressed_path))
    
    # Verify decompressed content
    with open(decompressed_path, 'r') as f:
        assert f.read() == input_data

def test_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        compress_bzip2(123)
    
    with pytest.raises(TypeError):
        decompress_bzip2(123)

def test_invalid_compressed_data():
    """Test handling of invalid compressed data"""
    with pytest.raises(bz2.BZ2Error):
        decompress_bzip2(b"Invalid compressed data")

def test_round_trip_compression():
    """Test complete compression and decompression cycle"""
    input_data = "Complete round-trip compression test with various characters: !@#$%^&*()"
    compressed = compress_bzip2(input_data)
    decompressed = decompress_bzip2(compressed)
    assert decompressed.decode('utf-8') == input_data