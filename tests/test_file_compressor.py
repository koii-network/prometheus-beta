import os
import bz2
import pytest
import tempfile
import shutil

from src.file_compressor import compress_file

@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    temp_path = tempfile.mkdtemp()
    yield temp_path
    shutil.rmtree(temp_path)

def create_test_file(temp_dir, content='Test content', filename='test_file.txt'):
    """Helper function to create a test file."""
    file_path = os.path.join(temp_dir, filename)
    with open(file_path, 'w') as f:
        f.write(content)
    return file_path

def test_compress_file_default_output(temp_dir):
    """Test compression with default output path."""
    input_file = create_test_file(temp_dir)
    compressed_file = compress_file(input_file)
    
    # Check compressed file exists with .bz2 extension
    assert os.path.exists(compressed_file)
    assert compressed_file == input_file + '.bz2'
    
    # Verify content can be decompressed
    with bz2.open(compressed_file, 'rt') as f:
        assert f.read() == 'Test content'

def test_compress_file_custom_output(temp_dir):
    """Test compression with custom output path."""
    input_file = create_test_file(temp_dir)
    output_file = os.path.join(temp_dir, 'custom_compressed.bz2')
    compressed_file = compress_file(input_file, output_file)
    
    # Check compressed file exists at specified path
    assert os.path.exists(compressed_file)
    assert compressed_file == output_file
    
    # Verify content can be decompressed
    with bz2.open(compressed_file, 'rt') as f:
        assert f.read() == 'Test content'

def test_compress_nonexistent_file(temp_dir):
    """Test compressing a non-existent file raises FileNotFoundError."""
    non_existent_file = os.path.join(temp_dir, 'nonexistent.txt')
    
    with pytest.raises(FileNotFoundError):
        compress_file(non_existent_file)

def test_compress_directory(temp_dir):
    """Test attempting to compress a directory raises IsADirectoryError."""
    with pytest.raises(IsADirectoryError):
        compress_file(temp_dir)

def test_large_file_compression(temp_dir):
    """Test compression of a large file."""
    large_content = 'x' * (1024 * 1024)  # 1MB of data
    input_file = create_test_file(temp_dir, content=large_content, filename='large_file.txt')
    compressed_file = compress_file(input_file)
    
    # Verify compression happened
    assert os.path.exists(compressed_file)
    assert os.path.getsize(compressed_file) < os.path.getsize(input_file)
    
    # Verify content can be decompressed
    with bz2.open(compressed_file, 'rt') as f:
        assert f.read() == large_content

def test_empty_file_compression(temp_dir):
    """Test compression of an empty file."""
    input_file = create_test_file(temp_dir, content='')
    compressed_file = compress_file(input_file)
    
    # Verify compression happened
    assert os.path.exists(compressed_file)
    
    # Verify content can be decompressed
    with bz2.open(compressed_file, 'rt') as f:
        assert f.read() == ''