import os
import pytest
import tempfile
from src.lzma_compression import compress_lzma, decompress_lzma

def test_lzma_compression_and_decompression():
    # Create a temporary file with known content
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_input:
        test_data = b"This is a test file for LZMA compression and decompression!"
        temp_input.write(test_data)
        input_path = temp_input.name

    compressed_path = None
    decompressed_path = None

    try:
        # Compress the file
        compressed_path = compress_lzma(input_path)
        assert os.path.exists(compressed_path)

        # Decompress the file
        decompressed_path = decompress_lzma(compressed_path)
        assert os.path.exists(decompressed_path)

        # Verify the content matches the original
        with open(decompressed_path, 'rb') as decompressed_file:
            decompressed_data = decompressed_file.read()
            assert decompressed_data == test_data

    finally:
        # Clean up temporary files, handle potential None values
        if input_path and os.path.exists(input_path):
            os.unlink(input_path)
        if compressed_path and os.path.exists(compressed_path):
            os.unlink(compressed_path)
        if decompressed_path and os.path.exists(decompressed_path):
            os.unlink(decompressed_path)

def test_lzma_compression_custom_output_path():
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_input:
        test_data = b"Custom output path test"
        temp_input.write(test_data)
        input_path = temp_input.name

    custom_compressed_path = input_path + '.custom_compressed'
    custom_decompressed_path = input_path + '.custom_decompressed'

    try:
        # Compress with custom output path
        compressed_path = compress_lzma(input_path, custom_compressed_path)
        assert compressed_path == custom_compressed_path
        assert os.path.exists(compressed_path)

        # Decompress with custom output path
        decompressed_path = decompress_lzma(compressed_path, custom_decompressed_path)
        assert decompressed_path == custom_decompressed_path
        assert os.path.exists(decompressed_path)

        with open(decompressed_path, 'rb') as decompressed_file:
            decompressed_data = decompressed_file.read()
            assert decompressed_data == test_data

    finally:
        # Clean up temporary files
        os.unlink(input_path)
        os.unlink(compressed_path)
        os.unlink(decompressed_path)

def test_lzma_nonexistent_input_file():
    with pytest.raises(FileNotFoundError):
        compress_lzma('/path/to/nonexistent/file.txt')

def test_lzma_invalid_compressed_file():
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_invalid:
        temp_invalid.write(b"Invalid compressed data")
        invalid_path = temp_invalid.name

    with pytest.raises(RuntimeError):
        decompress_lzma(invalid_path)

    os.unlink(invalid_path)