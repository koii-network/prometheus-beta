import os
import pytest
import lzma
import tempfile
import shutil
from src.xz_compression import compress_xz

def test_compress_xz_normal_case():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    try:
        # Create a test input file
        input_file_path = os.path.join(temp_dir, 'test_input.txt')
        with open(input_file_path, 'wb') as f:
            f.write(b'This is a test file for XZ compression')
        
        # Compress the file
        compressed_path = compress_xz(input_file_path)
        
        # Verify compression
        assert os.path.exists(compressed_path)
        assert compressed_path.endswith('.xz')
        assert os.path.getsize(compressed_path) > 0
        
        # Verify decompression
        with lzma.open(compressed_path, 'rb') as f:
            decompressed_content = f.read()
        
        assert decompressed_content == b'This is a test file for XZ compression'
    
    finally:
        # Clean up temporary directory
        shutil.rmtree(temp_dir)

def test_compress_xz_custom_output():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    try:
        # Create a test input file
        input_file_path = os.path.join(temp_dir, 'test_input.txt')
        output_file_path = os.path.join(temp_dir, 'custom_output.xz')
        with open(input_file_path, 'wb') as f:
            f.write(b'Another test for XZ compression')
        
        # Compress the file with custom output path
        compressed_path = compress_xz(input_file_path, output_file_path)
        
        # Verify compression
        assert compressed_path == output_file_path
        assert os.path.exists(compressed_path)
        assert os.path.getsize(compressed_path) > 0
        
        # Verify decompression
        with lzma.open(compressed_path, 'rb') as f:
            decompressed_content = f.read()
        
        assert decompressed_content == b'Another test for XZ compression'
    
    finally:
        # Clean up temporary directory
        shutil.rmtree(temp_dir)

def test_compress_xz_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        compress_xz('/path/to/nonexistent/file.txt')

def test_compress_xz_empty_file():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    try:
        # Create an empty test input file
        input_file_path = os.path.join(temp_dir, 'empty_input.txt')
        with open(input_file_path, 'wb') as f:
            pass  # Create an empty file
        
        # Compress the empty file
        compressed_path = compress_xz(input_file_path)
        
        # Verify compression
        assert os.path.exists(compressed_path)
        assert compressed_path.endswith('.xz')
        
        # Verify decompression
        with lzma.open(compressed_path, 'rb') as f:
            decompressed_content = f.read()
        
        assert decompressed_content == b''
    
    finally:
        # Clean up temporary directory
        shutil.rmtree(temp_dir)