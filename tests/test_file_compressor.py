import os
import pytest
import bz2
import tempfile
import shutil

from src.file_compressor import compress_file

def test_compress_file_default_output():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test file
        test_file_path = os.path.join(tmpdir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('Test content for compression')
        
        # Compress the file
        compressed_path = compress_file(test_file_path)
        
        # Verify compressed file exists with .bz2 extension
        assert os.path.exists(compressed_path)
        assert compressed_path == test_file_path + '.bz2'
        
        # Verify compression worked by decompressing
        with bz2.open(compressed_path, 'rt') as f:
            assert f.read() == 'Test content for compression'

def test_compress_file_custom_output():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test file
        test_file_path = os.path.join(tmpdir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('Test content for compression')
        
        # Custom output path
        custom_output = os.path.join(tmpdir, 'custom_compressed.bz2')
        compressed_path = compress_file(test_file_path, custom_output)
        
        # Verify compressed file exists at custom path
        assert os.path.exists(compressed_path)
        assert compressed_path == custom_output
        
        # Verify compression worked by decompressing
        with bz2.open(compressed_path, 'rt') as f:
            assert f.read() == 'Test content for compression'

def test_compress_nonexistent_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        nonexistent_path = os.path.join(tmpdir, 'nonexistent.txt')
        
        # Should raise FileNotFoundError
        with pytest.raises(FileNotFoundError):
            compress_file(nonexistent_path)

def test_compress_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Should raise IsADirectoryError
        with pytest.raises(IsADirectoryError):
            compress_file(tmpdir)

def test_large_file_compression():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a large test file
        large_file_path = os.path.join(tmpdir, 'large_file.txt')
        with open(large_file_path, 'w') as f:
            f.write('x' * (1024 * 1024))  # 1MB of data
        
        compressed_path = compress_file(large_file_path)
        
        # Verify compressed file exists and is smaller
        assert os.path.exists(compressed_path)
        assert os.path.getsize(compressed_path) < os.path.getsize(large_file_path)
        
        # Verify decompression works
        with bz2.open(compressed_path, 'rt') as f:
            assert f.read() == 'x' * (1024 * 1024)