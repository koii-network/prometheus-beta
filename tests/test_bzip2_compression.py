import os
import pytest
import tempfile
import bz2
from src.bzip2_compression import bzip2_compress, bzip2_decompress

@pytest.fixture
def sample_text_file():
    """Create a temporary file with sample text for testing."""
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write("This is a sample text for compression testing.\n" * 100)
        temp_file_path = temp_file.name
    yield temp_file_path
    os.unlink(temp_file_path)

def test_bzip2_compression_full_cycle(sample_text_file):
    """Test full compression and decompression cycle."""
    # Compress the file
    compressed_file = bzip2_compress(sample_text_file)
    assert os.path.exists(compressed_file)
    assert compressed_file.endswith('.bz2')
    
    # Decompress the file
    decompressed_file = bzip2_decompress(compressed_file)
    assert os.path.exists(decompressed_file)
    
    # Verify content matches original
    with open(sample_text_file, 'rb') as original, open(decompressed_file, 'rb') as decompressed:
        assert original.read() == decompressed.read()
    
    # Clean up
    os.unlink(compressed_file)
    os.unlink(decompressed_file)

def test_compression_custom_output_path(sample_text_file):
    """Test compression with a custom output path."""
    custom_output = os.path.join(tempfile.gettempdir(), 'custom_compressed.bz2')
    compressed_file = bzip2_compress(sample_text_file, custom_output)
    
    assert compressed_file == custom_output
    assert os.path.exists(compressed_file)
    
    os.unlink(compressed_file)

def test_decompression_custom_output_path(sample_text_file):
    """Test decompression with a custom output path."""
    compressed_file = bzip2_compress(sample_text_file)
    custom_output = os.path.join(tempfile.gettempdir(), 'custom_decompressed.txt')
    
    decompressed_file = bzip2_decompress(compressed_file, custom_output)
    
    assert decompressed_file == custom_output
    assert os.path.exists(decompressed_file)
    
    # Clean up
    os.unlink(compressed_file)
    os.unlink(decompressed_file)

def test_nonexistent_input_file():
    """Test handling of nonexistent input file."""
    with pytest.raises(FileNotFoundError):
        bzip2_compress('/path/to/nonexistent/file.txt')
    
    with pytest.raises(FileNotFoundError):
        bzip2_decompress('/path/to/nonexistent/file.bz2')

def test_large_file_compression(sample_text_file):
    """Test compression and decompression of a larger file."""
    # Multiply the sample file content to create a larger file
    with open(sample_text_file, 'a') as f:
        f.write("Additional large file content\n" * 10000)
    
    compressed_file = bzip2_compress(sample_text_file)
    decompressed_file = bzip2_decompress(compressed_file)
    
    # Verify content matches original
    with open(sample_text_file, 'rb') as original, open(decompressed_file, 'rb') as decompressed:
        assert original.read() == decompressed.read()
    
    # Clean up
    os.unlink(compressed_file)
    os.unlink(decompressed_file)

def test_empty_file_compression(tmp_path):
    """Test compression and decompression of an empty file."""
    empty_file = tmp_path / "empty_file.txt"
    empty_file.write_text("")
    
    compressed_file = bzip2_compress(str(empty_file))
    decompressed_file = bzip2_decompress(compressed_file)
    
    # Verify content matches original (empty)
    with open(str(empty_file), 'rb') as original, open(decompressed_file, 'rb') as decompressed:
        assert original.read() == decompressed.read()
    
    # Clean up
    os.unlink(compressed_file)
    os.unlink(decompressed_file)