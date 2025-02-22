import os
import pytest
import bz2
from src.bzip2_compression import compress_bzip2, decompress_bzip2

@pytest.fixture
def sample_file(tmp_path):
    """Create a sample file for testing"""
    sample_content = b"This is a test file for Bzip2 compression and decompression."
    file_path = tmp_path / "sample.txt"
    file_path.write_bytes(sample_content)
    return str(file_path)

def test_compress_bzip2_success(sample_file, tmp_path):
    """Test successful file compression"""
    output_path = compress_bzip2(sample_file)
    assert os.path.exists(output_path)
    assert output_path.endswith('.bz2')
    assert os.path.getsize(output_path) > 0

def test_compress_bzip2_custom_output(sample_file, tmp_path):
    """Test compression with custom output path"""
    custom_output = str(tmp_path / "custom_compressed.bz2")
    output_path = compress_bzip2(sample_file, custom_output)
    assert output_path == custom_output
    assert os.path.exists(output_path)

def test_decompress_bzip2_success(sample_file, tmp_path):
    """Test successful file decompression"""
    compressed_path = compress_bzip2(sample_file)
    decompressed_path = decompress_bzip2(compressed_path)
    
    with open(sample_file, 'rb') as original, open(decompressed_path, 'rb') as decompressed:
        assert original.read() == decompressed.read()

def test_decompress_bzip2_custom_output(sample_file, tmp_path):
    """Test decompression with custom output path"""
    compressed_path = compress_bzip2(sample_file)
    custom_output = str(tmp_path / "custom_decompressed.txt")
    decompressed_path = decompress_bzip2(compressed_path, custom_output)
    
    assert decompressed_path == custom_output
    with open(sample_file, 'rb') as original, open(decompressed_path, 'rb') as decompressed:
        assert original.read() == decompressed.read()

def test_compress_nonexistent_file():
    """Test compression of a nonexistent file"""
    with pytest.raises(FileNotFoundError):
        compress_bzip2("/path/to/nonexistent/file.txt")

def test_decompress_nonexistent_file():
    """Test decompression of a nonexistent file"""
    with pytest.raises(FileNotFoundError):
        decompress_bzip2("/path/to/nonexistent/file.bz2")

def test_compress_directory(tmp_path):
    """Test attempting to compress a directory"""
    with pytest.raises(IsADirectoryError):
        compress_bzip2(str(tmp_path))

def test_decompress_invalid_file(sample_file):
    """Test decompression of a non-compressed file"""
    with pytest.raises(RuntimeError):
        decompress_bzip2(sample_file)

def test_decompress_without_bz2_extension(sample_file):
    """Test decompression without .bz2 extension when no output path is provided"""
    with pytest.raises(ValueError):
        decompress_bzip2(sample_file)