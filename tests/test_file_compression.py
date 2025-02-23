import os
import gzip
import pytest
import shutil
import tempfile

from src.file_compression import compress_file

@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname

def test_compress_file_default_output(temp_dir):
    """Test compressing a file with default output path."""
    # Create a test file
    input_file = os.path.join(temp_dir, 'test_input.txt')
    with open(input_file, 'w') as f:
        f.write("Hello, world!")
    
    # Compress the file
    compressed_path = compress_file(input_file)
    
    # Verify compression
    assert os.path.exists(compressed_path)
    assert compressed_path == input_file + '.gz'
    
    # Verify content can be decompressed
    with gzip.open(compressed_path, 'rt') as f:
        assert f.read() == "Hello, world!"

def test_compress_file_custom_output(temp_dir):
    """Test compressing a file with a custom output path."""
    # Create a test file
    input_file = os.path.join(temp_dir, 'test_input.txt')
    output_file = os.path.join(temp_dir, 'custom_output.gz')
    
    with open(input_file, 'w') as f:
        f.write("Custom compression test")
    
    # Compress the file
    compressed_path = compress_file(input_file, output_file)
    
    # Verify compression
    assert os.path.exists(compressed_path)
    assert compressed_path == output_file
    
    # Verify content can be decompressed
    with gzip.open(compressed_path, 'rt') as f:
        assert f.read() == "Custom compression test"

def test_compress_nonexistent_file(temp_dir):
    """Test compressing a non-existent file raises FileNotFoundError."""
    non_existent_file = os.path.join(temp_dir, 'non_existent.txt')
    
    with pytest.raises(FileNotFoundError):
        compress_file(non_existent_file)

def test_compress_invalid_input():
    """Test compressing with invalid input raises ValueError."""
    with pytest.raises(ValueError):
        compress_file(None)
    
    with pytest.raises(ValueError):
        compress_file("")

def test_compress_large_file(temp_dir):
    """Test compressing a larger file."""
    # Create a larger test file
    input_file = os.path.join(temp_dir, 'large_input.txt')
    with open(input_file, 'w') as f:
        f.write("A" * 1000000)  # 1 million characters
    
    # Compress the file
    compressed_path = compress_file(input_file)
    
    # Verify compression
    assert os.path.exists(compressed_path)
    
    # Verify content can be decompressed
    with gzip.open(compressed_path, 'rt') as f:
        assert f.read() == "A" * 1000000