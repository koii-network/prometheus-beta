import os
import bz2
import pytest
from src.file_compressor import compress_file_bzip2

def test_compress_file_bzip2(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_input.txt"
    test_file.write_text("This is a test file for bzip2 compression.")

    # Compress the file
    compressed_file = compress_file_bzip2(str(test_file))

    # Verify compressed file was created
    assert os.path.exists(compressed_file)
    assert compressed_file.endswith('.bz2')

    # Verify compressed file can be decompressed
    with bz2.open(compressed_file, 'rt') as f:
        decompressed_content = f.read()
    
    assert decompressed_content == "This is a test file for bzip2 compression."

def test_compress_file_with_custom_output(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_input.txt"
    test_file.write_text("Another test file for bzip2 compression.")

    # Custom output file
    custom_output = str(tmp_path / "custom_compressed.bz2")
    compressed_file = compress_file_bzip2(str(test_file), custom_output)

    # Verify compressed file was created at the specified location
    assert compressed_file == custom_output
    assert os.path.exists(compressed_file)

def test_compress_nonexistent_file():
    # Test compressing a file that doesn't exist
    with pytest.raises(FileNotFoundError):
        compress_file_bzip2("nonexistent_file.txt")

# Note: Testing PermissionError would require mocking filesystem permissions,
# which is beyond the scope of this basic test suite.