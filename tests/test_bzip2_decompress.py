import os
import pytest
import bz2
from src.bzip2_decompress import decompress_bzip2_file

def create_sample_bzip2_file(filename, content):
    """Helper function to create a bzip2 compressed file for testing."""
    with bz2.open(filename, 'wb') as f:
        f.write(content.encode())

@pytest.fixture
def sample_bzip2_file(tmp_path):
    """Fixture to create a sample bzip2 compressed file."""
    input_file = tmp_path / "sample.txt.bz2"
    create_sample_bzip2_file(str(input_file), "This is a test file content.")
    return str(input_file)

def test_decompress_bzip2_file_default_output(sample_bzip2_file, tmp_path):
    """Test decompression with default output path."""
    output_file = decompress_bzip2_file(sample_bzip2_file)
    
    assert os.path.exists(output_file)
    assert output_file == sample_bzip2_file[:-4]
    
    with open(output_file, 'r') as f:
        content = f.read()
    
    assert content == "This is a test file content."

def test_decompress_bzip2_file_custom_output(sample_bzip2_file, tmp_path):
    """Test decompression with custom output path."""
    custom_output = str(tmp_path / "custom_output.txt")
    output_file = decompress_bzip2_file(sample_bzip2_file, custom_output)
    
    assert os.path.exists(output_file)
    assert output_file == custom_output
    
    with open(output_file, 'r') as f:
        content = f.read()
    
    assert content == "This is a test file content."

def test_nonexistent_input_file():
    """Test handling of non-existent input file."""
    with pytest.raises(FileNotFoundError):
        decompress_bzip2_file("/path/to/nonexistent/file.bz2")

def test_invalid_input_extension(tmp_path):
    """Test handling of input file without .bz2 extension."""
    invalid_file = str(tmp_path / "invalid_file.txt")
    with open(invalid_file, 'w') as f:
        f.write("Not a bzip2 file")
    
    with pytest.raises(ValueError):
        decompress_bzip2_file(invalid_file)

# Note: Additional error scenario tests like invalid bzip2 file 
# cannot be easily simulated due to bz2 module's implementation