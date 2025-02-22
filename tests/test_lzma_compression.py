import os
import pytest
import tempfile
from src.lzma_compression import compress_file, decompress_file

def test_compress_decompress_text_file():
    """Test compression and decompression of a text file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test input file
        input_path = os.path.join(tmpdir, 'test_input.txt')
        with open(input_path, 'w') as f:
            f.write('Hello, world! This is a test of LZMA compression.')
        
        # Compress the file
        compressed_path = compress_file(input_path)
        assert os.path.exists(compressed_path)
        assert compressed_path.endswith('.lzma')
        
        # Decompress the file
        decompressed_path = decompress_file(compressed_path)
        assert os.path.exists(decompressed_path)
        
        # Verify file contents
        with open(decompressed_path, 'r') as f:
            content = f.read()
            assert content == 'Hello, world! This is a test of LZMA compression.'

def test_compress_decompress_binary_file():
    """Test compression and decompression of a binary file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test binary file
        input_path = os.path.join(tmpdir, 'test_binary.bin')
        with open(input_path, 'wb') as f:
            f.write(b'\x00\x01\x02\x03\x04\x05\x06\x07')
        
        # Compress the file
        compressed_path = compress_file(input_path)
        assert os.path.exists(compressed_path)
        assert compressed_path.endswith('.lzma')
        
        # Decompress the file
        decompressed_path = decompress_file(compressed_path)
        assert os.path.exists(decompressed_path)
        
        # Verify file contents
        with open(decompressed_path, 'rb') as f:
            content = f.read()
            assert content == b'\x00\x01\x02\x03\x04\x05\x06\x07'

def test_file_not_found():
    """Test handling of non-existent input file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        non_existent_path = os.path.join(tmpdir, 'non_existent.txt')
        
        with pytest.raises(FileNotFoundError):
            compress_file(non_existent_path)
        
        with pytest.raises(FileNotFoundError):
            decompress_file(non_existent_path)

def test_custom_output_paths():
    """Test compression and decompression with custom output paths."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test input file
        input_path = os.path.join(tmpdir, 'test_input.txt')
        with open(input_path, 'w') as f:
            f.write('Custom paths test')
        
        # Custom compressed path
        custom_compressed_path = os.path.join(tmpdir, 'custom_compressed.lzma')
        compressed_path = compress_file(input_path, custom_compressed_path)
        assert compressed_path == custom_compressed_path
        
        # Custom decompressed path
        custom_decompressed_path = os.path.join(tmpdir, 'custom_decompressed.txt')
        decompressed_path = decompress_file(compressed_path, custom_decompressed_path)
        assert decompressed_path == custom_decompressed_path
        
        # Verify file contents
        with open(decompressed_path, 'r') as f:
            content = f.read()
            assert content == 'Custom paths test'

def test_invalid_decompress_path():
    """Test decompression with an invalid input path."""
    with tempfile.TemporaryDirectory() as tmpdir:
        invalid_path = os.path.join(tmpdir, 'invalid.txt')
        
        with pytest.raises(ValueError):
            decompress_file(invalid_path)