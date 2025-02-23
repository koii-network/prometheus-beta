import os
import gzip
import pytest
from src.gzip_decompress import decompress_gzip_file

@pytest.fixture
def sample_gzip_file(tmp_path):
    """Create a sample gzip file for testing."""
    input_file = tmp_path / "sample.txt.gz"
    with gzip.open(input_file, 'wb') as f:
        f.write(b"This is a test file for gzip decompression.")
    return input_file

def test_decompress_gzip_file_default_output(sample_gzip_file, tmp_path):
    """Test decompression with default output path."""
    output_path = decompress_gzip_file(str(sample_gzip_file))
    
    assert os.path.exists(output_path)
    assert output_path == str(sample_gzip_file)[:-3]
    
    with open(output_path, 'rb') as f:
        content = f.read()
        assert content == b"This is a test file for gzip decompression."

def test_decompress_gzip_file_custom_output(sample_gzip_file, tmp_path):
    """Test decompression with custom output path."""
    custom_output = str(tmp_path / "custom_output.txt")
    output_path = decompress_gzip_file(str(sample_gzip_file), custom_output)
    
    assert os.path.exists(output_path)
    assert output_path == custom_output
    
    with open(output_path, 'rb') as f:
        content = f.read()
        assert content == b"This is a test file for gzip decompression."

def test_decompress_nonexistent_file():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError):
        decompress_gzip_file("nonexistent_file.gz")

def test_decompress_non_gz_file(tmp_path):
    """Test that ValueError is raised for non .gz files."""
    non_gz_file = tmp_path / "sample.txt"
    non_gz_file.write_text("This is not a gzip file")
    
    with pytest.raises(ValueError):
        decompress_gzip_file(str(non_gz_file))