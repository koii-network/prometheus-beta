import os
import gzip
import pytest
import tempfile
from src.gzip_decompress import decompress_gzip_file

def create_test_gzip_file(content, filename):
    """Helper function to create a test gzip file"""
    with gzip.open(filename, 'wb') as f:
        f.write(content.encode())

def test_decompress_valid_gzip_file():
    """Test decompressing a valid gzip file"""
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, 'test.txt.gz')
        create_test_gzip_file('Hello, World!', input_path)
        
        output_path = decompress_gzip_file(input_path)
        
        assert os.path.exists(output_path)
        with open(output_path, 'r') as f:
            assert f.read() == 'Hello, World!'

def test_decompress_with_custom_output_path():
    """Test decompressing with a specified output path"""
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, 'test.txt.gz')
        output_path = os.path.join(tmpdir, 'decompressed.txt')
        
        create_test_gzip_file('Custom output path', input_path)
        
        result_path = decompress_gzip_file(input_path, output_path)
        
        assert result_path == output_path
        with open(result_path, 'r') as f:
            assert f.read() == 'Custom output path'

def test_decompress_nonexistent_file():
    """Test handling of non-existent input file"""
    with tempfile.TemporaryDirectory() as tmpdir:
        nonexistent_path = os.path.join(tmpdir, 'nonexistent.txt.gz')
        
        with pytest.raises(FileNotFoundError):
            decompress_gzip_file(nonexistent_path)

def test_decompress_invalid_file_extension():
    """Test handling of non-gzip file extension"""
    with tempfile.TemporaryDirectory() as tmpdir:
        invalid_path = os.path.join(tmpdir, 'test.txt')
        
        with pytest.raises(ValueError):
            decompress_gzip_file(invalid_path)

def test_decompress_empty_gzip_file():
    """Test decompressing an empty gzip file"""
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, 'empty.txt.gz')
        create_test_gzip_file('', input_path)
        
        output_path = decompress_gzip_file(input_path)
        
        assert os.path.exists(output_path)
        with open(output_path, 'r') as f:
            assert f.read() == ''