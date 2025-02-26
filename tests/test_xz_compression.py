import os
import pytest
import lzma
import tempfile
import shutil

from src.xz_compression import compress_xz

def test_xz_compression_basic():
    """Test basic XZ compression functionality."""
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Create a test input file
        input_file = os.path.join(temp_dir, 'test_input.txt')
        with open(input_file, 'wb') as f:
            f.write(b'This is a test file for XZ compression.')
        
        # Perform compression
        compressed_file = compress_xz(input_file)
        
        # Check if compressed file exists
        assert os.path.exists(compressed_file)
        assert compressed_file.endswith('.xz')
        
        # Verify compression by decompressing and checking content
        with lzma.open(compressed_file, 'rb') as f:
            decompressed_content = f.read()
        
        assert decompressed_content == b'This is a test file for XZ compression.'
    
    finally:
        # Clean up temporary directory
        shutil.rmtree(temp_dir)

def test_xz_compression_custom_output():
    """Test XZ compression with a custom output path."""
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Create a test input file
        input_file = os.path.join(temp_dir, 'test_input.txt')
        output_file = os.path.join(temp_dir, 'custom_output.xz')
        
        with open(input_file, 'wb') as f:
            f.write(b'Custom output path test')
        
        # Perform compression with custom output
        compressed_file = compress_xz(input_file, output_file)
        
        # Check if compressed file exists at the specified location
        assert compressed_file == output_file
        assert os.path.exists(compressed_file)
        
        # Verify compression by decompressing and checking content
        with lzma.open(compressed_file, 'rb') as f:
            decompressed_content = f.read()
        
        assert decompressed_content == b'Custom output path test'
    
    finally:
        # Clean up temporary directory
        shutil.rmtree(temp_dir)

def test_xz_compression_nonexistent_file():
    """Test XZ compression with a non-existent input file."""
    with pytest.raises(FileNotFoundError):
        compress_xz('/path/to/nonexistent/file.txt')

def test_xz_compression_large_file():
    """Test XZ compression with a larger file."""
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Create a larger test file
        input_file = os.path.join(temp_dir, 'large_test_file.txt')
        with open(input_file, 'wb') as f:
            f.write(b'x' * (1024 * 1024))  # 1MB of data
        
        # Perform compression
        compressed_file = compress_xz(input_file)
        
        # Verify compression
        assert os.path.exists(compressed_file)
        
        # Check that compressed file is smaller than original
        original_size = os.path.getsize(input_file)
        compressed_size = os.path.getsize(compressed_file)
        assert compressed_size < original_size
    
    finally:
        # Clean up temporary directory
        shutil.rmtree(temp_dir)