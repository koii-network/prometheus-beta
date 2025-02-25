import os
import pytest
import tempfile
import zstandard as zstd

from src.zstandard_compression import compress_data, decompress_data, compress_file


def test_compress_decompress_bytes():
    """Test compressing and decompressing byte data"""
    original_data = b"Hello, Zstandard compression!"
    compressed = compress_data(original_data)
    
    # Verify compressed data is different and shorter
    assert compressed != original_data
    assert len(compressed) < len(original_data)
    
    # Decompress and verify
    decompressed = decompress_data(compressed)
    assert decompressed == original_data


def test_compress_decompress_string():
    """Test compressing and decompressing string data"""
    original_data = "Hello, Zstandard compression!"
    compressed = compress_data(original_data)
    
    # Decompress and verify
    decompressed = decompress_data(compressed)
    assert decompressed == original_data.encode('utf-8')


def test_compression_level():
    """Test different compression levels"""
    data = b"Test compression levels"
    
    # Test valid compression levels
    for level in [1, 5, 10, 22]:
        compressed = compress_data(data, compression_level=level)
        decompressed = decompress_data(compressed)
        assert decompressed == data


def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        compress_data(123)
    
    with pytest.raises(TypeError):
        decompress_data(123)


def test_invalid_compression_level():
    """Test handling of invalid compression levels"""
    with pytest.raises(ValueError):
        compress_data(b"test", compression_level=0)
    
    with pytest.raises(ValueError):
        compress_data(b"test", compression_level=23)


def test_compress_file():
    """Test file compression functionality"""
    # Create a temporary file with test data
    with tempfile.NamedTemporaryFile(delete=False) as temp_input:
        test_data = b"Test file compression with Zstandard"
        temp_input.write(test_data)
        temp_input.close()

    try:
        # Compress the file
        compressed_path = compress_file(temp_input.name)
        
        # Verify compressed file exists and is different
        assert os.path.exists(compressed_path)
        assert os.path.getsize(compressed_path) < os.path.getsize(temp_input.name)

        # Verify can decompress
        dctx = zstd.ZstdDecompressor()
        with open(compressed_path, 'rb') as compressed_file, \
             open(temp_input.name + '.decompressed', 'wb') as decompressed_file:
            dctx.copy_stream(compressed_file, decompressed_file)

        # Check decompressed content
        with open(temp_input.name + '.decompressed', 'rb') as f:
            assert f.read() == test_data

    finally:
        # Clean up temporary files
        os.unlink(temp_input.name)
        if os.path.exists(compressed_path):
            os.unlink(compressed_path)
        if os.path.exists(temp_input.name + '.decompressed'):
            os.unlink(temp_input.name + '.decompressed')