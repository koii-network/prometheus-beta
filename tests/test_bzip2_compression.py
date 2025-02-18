import os
import pytest
import bz2
from src.bzip2_compression import compress_bzip2, decompress_bzip2

def test_compress_string():
    input_text = "Hello, world! This is a test of Bzip2 compression."
    compressed = compress_bzip2(input_text)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != input_text.encode('utf-8')

def test_compress_bytes():
    input_bytes = b"Binary data for compression test"
    compressed = compress_bzip2(input_bytes)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != input_bytes

def test_compress_with_file_output(tmp_path):
    input_text = "Compression to file test"
    output_path = os.path.join(tmp_path, "compressed.bz2")
    result = compress_bzip2(input_text, output_path)
    
    assert os.path.exists(output_path)
    with open(output_path, 'rb') as f:
        file_contents = f.read()
    
    assert file_contents == result

def test_decompress_bytes():
    original_text = "Hello, world! Compression and decompression test."
    compressed = compress_bzip2(original_text)
    decompressed = decompress_bzip2(compressed)
    
    assert decompressed.decode('utf-8') == original_text

def test_decompress_from_file(tmp_path):
    original_text = "Decompression from file test"
    input_path = os.path.join(tmp_path, "input.bz2")
    output_path = os.path.join(tmp_path, "output.txt")
    
    # Compress and save to file
    compress_bzip2(original_text, input_path)
    
    # Decompress from file
    decompressed = decompress_bzip2(input_path, output_path)
    
    # Check file output
    assert os.path.exists(output_path)
    with open(output_path, 'rb') as f:
        file_contents = f.read()
    
    assert file_contents == decompressed
    assert file_contents.decode('utf-8') == original_text

def test_compression_levels():
    input_text = "Testing different compression levels"
    
    # Test levels 1-9
    for level in range(1, 10):
        compressed = compress_bzip2(input_text, compression_level=level)
        assert isinstance(compressed, bytes)
        assert len(compressed) > 0

def test_invalid_compression_level():
    with pytest.raises(ValueError):
        compress_bzip2("Test", compression_level=0)
    
    with pytest.raises(ValueError):
        compress_bzip2("Test", compression_level=10)

def test_invalid_input_type():
    with pytest.raises(TypeError):
        compress_bzip2(123)  # Integer is not allowed
    
    with pytest.raises(TypeError):
        compress_bzip2(["not", "a", "string"])  # List is not allowed

def test_large_data_compression():
    large_text = "A" * 1_000_000  # 1 million characters
    compressed = compress_bzip2(large_text)
    decompressed = decompress_bzip2(compressed)
    
    assert decompressed.decode('utf-8') == large_text