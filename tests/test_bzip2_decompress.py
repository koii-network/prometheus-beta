import os
import bz2
import pytest
from src.bzip2_decompress import decompress_bzip2_file

# Create a temporary directory for test files
import tempfile

@pytest.fixture
def sample_bzip2_file():
    """Create a sample bzip2 compressed file for testing."""
    with tempfile.NamedTemporaryFile(suffix='.txt.bz2', delete=False) as temp_compressed:
        original_content = b"This is a test file for bzip2 decompression."
        compressed_content = bz2.compress(original_content)
        temp_compressed.write(compressed_content)
        temp_compressed.close()
        return temp_compressed.name

def test_decompress_bzip2_file_default_output(sample_bzip2_file):
    """Test decompression with default output path."""
    decompressed_file = decompress_bzip2_file(sample_bzip2_file)
    
    assert os.path.exists(decompressed_file)
    with open(decompressed_file, 'rb') as f:
        content = f.read()
    
    assert content == b"This is a test file for bzip2 decompression."
    os.unlink(decompressed_file)
    os.unlink(sample_bzip2_file)

def test_decompress_bzip2_file_custom_output(sample_bzip2_file):
    """Test decompression with custom output path."""
    output_path = os.path.join(tempfile.gettempdir(), 'custom_output.txt')
    decompressed_file = decompress_bzip2_file(sample_bzip2_file, output_path)
    
    assert decompressed_file == output_path
    assert os.path.exists(decompressed_file)
    with open(decompressed_file, 'rb') as f:
        content = f.read()
    
    assert content == b"This is a test file for bzip2 decompression."
    os.unlink(decompressed_file)
    os.unlink(sample_bzip2_file)

def test_decompress_nonexistent_file():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        decompress_bzip2_file('/path/to/nonexistent/file.txt.bz2')

def test_decompress_invalid_bzip2_file(tmp_path):
    """Test handling of invalid bzip2 file."""
    invalid_file = tmp_path / 'invalid.bz2'
    with open(invalid_file, 'wb') as f:
        f.write(b'Not a valid bzip2 file')
    
    with pytest.raises(ValueError):
        decompress_bzip2_file(str(invalid_file))