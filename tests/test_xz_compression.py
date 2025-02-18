import os
import pytest
import lzma
import tempfile
from src.xz_compression import compress_file_xz

def test_compress_file_xz_basic():
    """Test basic XZ compression functionality"""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test input file
        input_file = os.path.join(tmpdir, 'test_input.txt')
        with open(input_file, 'w') as f:
            f.write('This is a test file for XZ compression.')
        
        # Compress the file
        compressed_file = compress_file_xz(input_file)
        
        # Verify compression
        assert os.path.exists(compressed_file)
        assert compressed_file.endswith('.xz')
        assert os.path.getsize(compressed_file) < os.path.getsize(input_file)

def test_compress_file_xz_custom_output():
    """Test XZ compression with custom output path"""
    with tempfile.TemporaryDirectory() as tmpdir:
        input_file = os.path.join(tmpdir, 'test_input.txt')
        custom_output = os.path.join(tmpdir, 'custom_compressed.xz')
        
        with open(input_file, 'w') as f:
            f.write('Custom output path test')
        
        compressed_file = compress_file_xz(input_file, custom_output)
        
        assert compressed_file == custom_output
        assert os.path.exists(compressed_file)

def test_compress_file_xz_large_file():
    """Test XZ compression with a larger file"""
    with tempfile.TemporaryDirectory() as tmpdir:
        input_file = os.path.join(tmpdir, 'large_test_file.txt')
        with open(input_file, 'w') as f:
            f.write('a' * 10000)  # 10,000 character file
        
        compressed_file = compress_file_xz(input_file)
        
        assert os.path.exists(compressed_file)
        assert os.path.getsize(compressed_file) < os.path.getsize(input_file)

def test_compress_file_xz_nonexistent_file():
    """Test XZ compression with non-existent file"""
    with tempfile.TemporaryDirectory() as tmpdir:
        non_existent_file = os.path.join(tmpdir, 'nonexistent.txt')
        
        with pytest.raises(FileNotFoundError):
            compress_file_xz(non_existent_file)

def test_compressed_file_decompression():
    """Test if the compressed file can be decompressed"""
    with tempfile.TemporaryDirectory() as tmpdir:
        input_file = os.path.join(tmpdir, 'test_input.txt')
        with open(input_file, 'w') as f:
            f.write('Verifying decompression works correctly')
        
        compressed_file = compress_file_xz(input_file)
        
        # Attempt to decompress
        with lzma.open(compressed_file, 'rb') as f:
            decompressed_content = f.read().decode('utf-8')
        
        assert decompressed_content == 'Verifying decompression works correctly'