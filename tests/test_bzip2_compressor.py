import os
import bz2
import pytest
import tempfile
import shutil

from src.bzip2_compressor import compress_file

def test_compress_file_basic():
    """Test basic file compression."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test file with more content to encourage compression
        input_file = os.path.join(tmpdir, 'test_input.txt')
        test_content = 'Hello, world! ' * 100  # Repeating content for better compression
        with open(input_file, 'w') as f:
            f.write(test_content)
        
        # Compress the file
        compressed_file = compress_file(input_file)
        
        # Verify compression
        assert os.path.exists(compressed_file)
        assert compressed_file.endswith('.bz2')
        assert os.path.getsize(compressed_file) > 0
        assert os.path.getsize(compressed_file) < os.path.getsize(input_file)

def test_compress_file_custom_output():
    """Test compression with a custom output path."""
    with tempfile.TemporaryDirectory() as tmpdir:
        input_file = os.path.join(tmpdir, 'test_input.txt')
        output_file = os.path.join(tmpdir, 'custom_compressed.bz2')
        
        with open(input_file, 'w') as f:
            f.write('Custom output compression test')
        
        compressed_file = compress_file(input_file, output_file)
        
        assert compressed_file == output_file
        assert os.path.exists(compressed_file)

def test_compress_nonexistent_file():
    """Test compression of a non-existent file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        nonexistent_file = os.path.join(tmpdir, 'nonexistent.txt')
        
        with pytest.raises(FileNotFoundError):
            compress_file(nonexistent_file)

def test_compress_directory():
    """Test attempting to compress a directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        with pytest.raises(IsADirectoryError):
            compress_file(tmpdir)

def test_compress_decompression():
    """Test that the compressed file can be decompressed correctly."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test file
        input_file = os.path.join(tmpdir, 'test_input.txt')
        original_content = 'Hello, world! This is a test for decompression validation.'
        with open(input_file, 'w') as f:
            f.write(original_content)
        
        # Compress the file
        compressed_file = compress_file(input_file)
        
        # Decompress and verify content
        with bz2.open(compressed_file, 'rt') as f:
            decompressed_content = f.read()
        
        assert decompressed_content == original_content