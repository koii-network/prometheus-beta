import os
import pytest
import tempfile
from src.lzma_compression import compress_lzma, decompress_lzma

def test_compression_decompression_bytes():
    """Test compression and decompression with bytes input"""
    original_data = b"Hello, this is a test string for LZMA compression!"
    
    # Compress
    compressed_data = compress_lzma(original_data)
    assert compressed_data is not None
    
    # Decompress
    decompressed_data = decompress_lzma(compressed_data)
    assert decompressed_data == original_data

def test_compression_decompression_string():
    """Test compression and decompression with string input"""
    original_data = "Hello, this is a test string for LZMA compression!"
    
    # Compress
    compressed_data = compress_lzma(original_data)
    assert compressed_data is not None
    
    # Decompress
    decompressed_data = decompress_lzma(compressed_data)
    assert decompressed_data == original_data.encode('utf-8')

def test_compression_levels():
    """Test different compression levels"""
    data = b"This is a test string for testing different compression levels"
    
    # Test compression levels from 0 to 9
    for level in range(10):
        compressed_data = compress_lzma(data, compression_level=level)
        assert compressed_data is not None
        
        # Decompress and verify
        decompressed_data = decompress_lzma(compressed_data)
        assert decompressed_data == data

def test_file_compression_decompression():
    """Test compression and decompression with file paths"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Input file
        original_data = b"Test data for file compression"
        input_file = os.path.join(tmpdir, 'input.txt')
        with open(input_file, 'wb') as f:
            f.write(original_data)
        
        # Compressed file
        compressed_file = os.path.join(tmpdir, 'compressed.lzma')
        
        # Decompressed file
        decompressed_file = os.path.join(tmpdir, 'decompressed.txt')
        
        # Compress file
        compress_lzma(input_file, output_path=compressed_file)
        assert os.path.exists(compressed_file)
        
        # Decompress file
        decompress_lzma(compressed_file, output_path=decompressed_file)
        assert os.path.exists(decompressed_file)
        
        # Verify contents
        with open(decompressed_file, 'rb') as f:
            decompressed_data = f.read()
        
        assert original_data == decompressed_data

def test_invalid_compression_level():
    """Test invalid compression level raises ValueError"""
    with pytest.raises(ValueError):
        compress_lzma(b"test", compression_level=-1)
    
    with pytest.raises(ValueError):
        compress_lzma(b"test", compression_level=10)

def test_invalid_input_type():
    """Test invalid input types raise TypeError"""
    with pytest.raises(TypeError):
        compress_lzma(123)  # Integer input
    
    with pytest.raises(TypeError):
        compress_lzma(None)  # None input
    
    with pytest.raises(TypeError):
        decompress_lzma(123)  # Integer input
    
    with pytest.raises(TypeError):
        decompress_lzma(None)  # None input