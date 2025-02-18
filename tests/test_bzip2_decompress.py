import os
import pytest
import bz2
from src.bzip2_decompress import decompress_bzip2_file

@pytest.fixture
def sample_bzip2_file(tmp_path):
    """Create a sample bzip2-compressed file for testing."""
    original_content = b"This is a test file for bzip2 decompression."
    input_path = tmp_path / "test_file.txt.bz2"
    
    with bz2.open(input_path, 'wb') as f:
        f.write(original_content)
    
    return input_path

def test_decompress_bzip2_file_default_output(sample_bzip2_file, tmp_path):
    """Test decompression with default output path."""
    output_path = decompress_bzip2_file(sample_bzip2_file)
    
    assert os.path.exists(output_path)
    assert output_path == str(sample_bzip2_file).removesuffix('.bz2')
    
    with open(output_path, 'rb') as f:
        content = f.read()
    
    assert content == b"This is a test file for bzip2 decompression."

def test_decompress_bzip2_file_custom_output(sample_bzip2_file, tmp_path):
    """Test decompression with custom output path."""
    custom_output = tmp_path / "custom_output.txt"
    output_path = decompress_bzip2_file(sample_bzip2_file, str(custom_output))
    
    assert os.path.exists(output_path)
    assert output_path == str(custom_output)
    
    with open(output_path, 'rb') as f:
        content = f.read()
    
    assert content == b"This is a test file for bzip2 decompression."

def test_decompress_nonexistent_file():
    """Test handling of non-existent input file."""
    with pytest.raises(FileNotFoundError):
        decompress_bzip2_file("nonexistent_file.txt.bz2")

def test_decompress_invalid_file_type(tmp_path):
    """Test handling of non-bzip2 file."""
    invalid_file = tmp_path / "test_file.txt"
    invalid_file.write_text("Not a bzip2 file")
    
    with pytest.raises(ValueError, match="is not a .bz2 file"):
        decompress_bzip2_file(str(invalid_file))