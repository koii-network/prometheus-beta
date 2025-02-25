import os
import bz2
import pytest
from src.bzip2_decompress import decompress_bzip2_file

@pytest.fixture
def create_sample_bz2_file(tmp_path):
    """Create a sample bzip2 compressed file for testing."""
    content = b"This is a test file for bzip2 decompression."
    sample_file = tmp_path / "sample.txt.bz2"
    with bz2.open(sample_file, 'wb') as f:
        f.write(content)
    return sample_file

def test_successful_decompression(create_sample_bz2_file, tmp_path):
    """Test successful file decompression."""
    compressed_path = str(create_sample_bz2_file)
    output_path = str(tmp_path / "sample.txt")
    
    # Decompress the file
    result_path = decompress_bzip2_file(compressed_path, output_path)
    
    # Verify the result
    assert result_path == output_path
    assert os.path.exists(result_path)
    
    # Check file contents
    with open(result_path, 'rb') as f:
        content = f.read()
    assert content == b"This is a test file for bzip2 decompression."

def test_default_output_filepath(create_sample_bz2_file):
    """Test default output filepath generation."""
    compressed_path = str(create_sample_bz2_file)
    result_path = decompress_bzip2_file(compressed_path)
    
    assert result_path == compressed_path.rstrip('.bz2')
    assert os.path.exists(result_path)

def test_nonexistent_file():
    """Test handling of non-existent input file."""
    with pytest.raises(FileNotFoundError):
        decompress_bzip2_file('nonexistent_file.txt.bz2')

def test_directory_input(tmp_path):
    """Test handling of directory input."""
    with pytest.raises(IsADirectoryError):
        decompress_bzip2_file(str(tmp_path))

def test_invalid_extension(tmp_path):
    """Test handling of non-bz2 file extension."""
    invalid_file = tmp_path / "file.zip"
    invalid_file.write_text("test")
    
    with pytest.raises(ValueError):
        decompress_bzip2_file(str(invalid_file))

def test_invalid_bz2_file(tmp_path):
    """Test handling of an invalid bzip2 file."""
    invalid_bz2_file = tmp_path / "invalid.bz2"
    invalid_bz2_file.write_text("Not a real bzip2 file")
    
    with pytest.raises(ValueError):
        decompress_bzip2_file(str(invalid_bz2_file))