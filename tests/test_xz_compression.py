import os
import pytest
import lzma
from src.xz_compression import compress_xz, decompress_xz

@pytest.fixture
def sample_file(tmp_path):
    """Create a sample file for testing"""
    sample_content = "Hello, XZ compression! " * 1000
    file_path = tmp_path / "sample.txt"
    file_path.write_text(sample_content)
    return str(file_path)

def test_compression_basic(sample_file, tmp_path):
    """Test basic XZ compression"""
    compressed_path = compress_xz(sample_file)
    assert os.path.exists(compressed_path)
    assert compressed_path.endswith('.xz')
    assert os.path.getsize(compressed_path) < os.path.getsize(sample_file)

def test_compression_custom_output(sample_file, tmp_path):
    """Test XZ compression with custom output path"""
    custom_output = str(tmp_path / "custom_compressed.xz")
    compressed_path = compress_xz(sample_file, output_path=custom_output)
    assert compressed_path == custom_output
    assert os.path.exists(compressed_path)

def test_compression_levels(sample_file):
    """Test different compression levels"""
    # Test various compression levels
    for level in range(10):
        compressed_path = compress_xz(sample_file, compression_level=level)
        assert os.path.exists(compressed_path)
        os.unlink(compressed_path)

def test_compression_decompression_round_trip(sample_file, tmp_path):
    """Test full compression and decompression round trip"""
    compressed_path = compress_xz(sample_file)
    decompressed_path = decompress_xz(compressed_path)
    
    with open(sample_file, 'r') as original, open(decompressed_path, 'r') as decompressed:
        assert original.read() == decompressed.read()

def test_compression_invalid_input():
    """Test compression with non-existent file"""
    with pytest.raises(FileNotFoundError):
        compress_xz("/path/to/nonexistent/file.txt")

def test_compression_invalid_level(sample_file):
    """Test compression with invalid compression level"""
    with pytest.raises(ValueError):
        compress_xz(sample_file, compression_level=10)

def test_decompression_basic(sample_file, tmp_path):
    """Test basic XZ decompression"""
    compressed_path = compress_xz(sample_file)
    decompressed_path = decompress_xz(compressed_path)
    
    assert os.path.exists(decompressed_path)
    assert os.path.getsize(decompressed_path) == os.path.getsize(sample_file)

def test_decompression_custom_output(sample_file, tmp_path):
    """Test XZ decompression with custom output path"""
    compressed_path = compress_xz(sample_file)
    custom_output = str(tmp_path / "custom_decompressed.txt")
    decompressed_path = decompress_xz(compressed_path, output_path=custom_output)
    
    assert decompressed_path == custom_output
    assert os.path.exists(decompressed_path)

def test_decompression_invalid_input():
    """Test decompression with non-existent file"""
    with pytest.raises(FileNotFoundError):
        decompress_xz("/path/to/nonexistent/file.xz")

def test_decompression_invalid_file(sample_file):
    """Test decompression without .xz extension when no output path given"""
    with pytest.raises(ValueError):
        decompress_xz(sample_file)