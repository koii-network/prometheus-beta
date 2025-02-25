import os
import bz2
import pytest
import tempfile

from src.bzip2_compression import compress_bzip2, decompress_bzip2

def test_compress_bzip2_string():
    """Test compression of string input"""
    test_string = "Hello, world! This is a test of Bzip2 compression."
    compressed = compress_bzip2(test_string)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != test_string.encode('utf-8')

def test_compress_bzip2_bytes():
    """Test compression of bytes input"""
    test_bytes = b"Hello, world! This is a test of Bzip2 compression."
    compressed = compress_bzip2(test_bytes)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != test_bytes

def test_compress_bzip2_with_output_file():
    """Test compression with output file"""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        test_string = "Hello, world! This is a test of Bzip2 compression."
        compress_bzip2(test_string, output_path=temp_path)
        
        # Verify file was created and is not empty
        assert os.path.exists(temp_path)
        assert os.path.getsize(temp_path) > 0
    finally:
        # Clean up
        if os.path.exists(temp_path):
            os.unlink(temp_path)

def test_decompress_bzip2_bytes():
    """Test decompression of bytes"""
    original = "Hello, world! This is a test of Bzip2 compression."
    compressed = bz2.compress(original.encode('utf-8'))
    decompressed = decompress_bzip2(compressed)
    
    assert isinstance(decompressed, bytes)
    assert decompressed.decode('utf-8') == original

def test_decompress_bzip2_with_output_file():
    """Test decompression with output file"""
    with tempfile.NamedTemporaryFile(delete=False) as temp_compressed, \
         tempfile.NamedTemporaryFile(delete=False) as temp_decompressed:
        compressed_path = temp_compressed.name
        decompressed_path = temp_decompressed.name
    
    try:
        # Create compressed file
        original = "Hello, world! This is a test of Bzip2 compression."
        compressed_data = bz2.compress(original.encode('utf-8'))
        with open(compressed_path, 'wb') as f:
            f.write(compressed_data)
        
        # Decompress file
        decompress_bzip2(compressed_path, output_path=decompressed_path)
        
        # Verify decompressed file
        with open(decompressed_path, 'rb') as f:
            decompressed = f.read().decode('utf-8')
        
        assert decompressed == original
    finally:
        # Clean up
        for path in [compressed_path, decompressed_path]:
            if os.path.exists(path):
                os.unlink(path)

def test_compress_empty_input_raises_error():
    """Test that empty input raises ValueError"""
    with pytest.raises(ValueError):
        compress_bzip2("")
    with pytest.raises(ValueError):
        compress_bzip2(b"")

def test_compress_invalid_input_raises_error():
    """Test that invalid input types raise TypeError"""
    with pytest.raises(TypeError):
        compress_bzip2(123)
    with pytest.raises(TypeError):
        compress_bzip2(None)

def test_decompress_invalid_compressed_data():
    """Test decompression of invalid compressed data"""
    with pytest.raises(Exception):  # Catch any decompression error
        decompress_bzip2(b"invalid compressed data")

def test_roundtrip_compression():
    """Test full compression and decompression roundtrip"""
    original = "Hello, world! This is a roundtrip test of Bzip2 compression."
    compressed = compress_bzip2(original)
    decompressed = decompress_bzip2(compressed)
    
    assert decompressed.decode('utf-8') == original