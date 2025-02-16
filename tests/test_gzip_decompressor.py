import os
import gzip
import pytest
from src.gzip_decompressor import decompress_gzip_file

@pytest.fixture
def sample_gzip_file(tmp_path):
    """Create a sample gzip file for testing"""
    input_text = "This is a test file for gzip decompression."
    input_path = tmp_path / "test_file.txt.gz"
    
    with gzip.open(input_path, 'wb') as f:
        f.write(input_text.encode())
    
    return input_path

def test_decompress_gzip_file_default_output(sample_gzip_file, tmp_path):
    """Test decompression with default output path"""
    output_path = decompress_gzip_file(sample_gzip_file)
    
    assert os.path.exists(output_path)
    with open(output_path, 'r') as f:
        content = f.read()
    
    assert content == "This is a test file for gzip decompression."

def test_decompress_gzip_file_custom_output(sample_gzip_file, tmp_path):
    """Test decompression with custom output path"""
    custom_output = tmp_path / "custom_output.txt"
    output_path = decompress_gzip_file(sample_gzip_file, str(custom_output))
    
    assert output_path == str(custom_output)
    assert os.path.exists(output_path)
    with open(output_path, 'r') as f:
        content = f.read()
    
    assert content == "This is a test file for gzip decompression."

def test_decompress_nonexistent_file():
    """Test handling of non-existent input file"""
    with pytest.raises(FileNotFoundError):
        decompress_gzip_file("nonexistent_file.gz")

def test_decompress_invalid_gzip(tmp_path):
    """Test handling of invalid gzip file"""
    invalid_file = tmp_path / "invalid.gz"
    with open(invalid_file, 'wb') as f:
        f.write(b"This is not a valid gzip file")
    
    with pytest.raises(ValueError):
        decompress_gzip_file(str(invalid_file))