import os
import pytest
import gzip
from src.gzip_compression import compress_file, decompress_file

def test_compress_file(tmpdir):
    # Create a test file
    test_file = tmpdir.join('test_file.txt')
    test_file.write('Hello, world!')
    
    # Compress the file
    compressed_file = compress_file(str(test_file))
    
    # Check that compressed file exists and is a gzip file
    assert os.path.exists(compressed_file)
    assert compressed_file.endswith('.gz')
    
    # Verify it's a valid gzip file
    with gzip.open(compressed_file, 'rb') as f:
        content = f.read().decode('utf-8')
        assert content == 'Hello, world!'

def test_decompress_file(tmpdir):
    # Create a test file
    test_file = tmpdir.join('test_file.txt')
    test_file.write('Hello, world!')
    
    # Compress the file
    compressed_file = compress_file(str(test_file))
    
    # Decompress the file
    decompressed_file = decompress_file(compressed_file)
    
    # Check that decompressed file exists
    assert os.path.exists(decompressed_file)
    
    # Verify decompressed content
    with open(decompressed_file, 'r') as f:
        content = f.read()
        assert content == 'Hello, world!'

def test_compress_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        compress_file('nonexistent_file.txt')

def test_decompress_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        decompress_file('nonexistent_file.txt.gz')

def test_custom_output_filename(tmpdir):
    # Create a test file
    test_file = tmpdir.join('test_file.txt')
    test_file.write('Hello, world!')
    
    # Compress with custom output filename
    custom_compressed = tmpdir.join('custom_compressed.gz')
    compressed_file = compress_file(str(test_file), str(custom_compressed))
    
    # Check custom filename was used
    assert compressed_file == str(custom_compressed)
    
    # Decompress with custom output filename
    custom_decompressed = tmpdir.join('custom_decompressed.txt')
    decompressed_file = decompress_file(compressed_file, str(custom_decompressed))
    
    # Check custom filename was used
    assert decompressed_file == str(custom_decompressed)

def test_large_file(tmpdir):
    # Create a large test file
    test_file = tmpdir.join('large_file.txt')
    test_file.write('A' * 1_000_000)  # 1 MB of data
    
    # Compress and decompress
    compressed_file = compress_file(str(test_file))
    decompressed_file = decompress_file(compressed_file)
    
    # Verify decompressed content
    with open(decompressed_file, 'r') as f:
        content = f.read()
        assert content == 'A' * 1_000_000  # Verify full content