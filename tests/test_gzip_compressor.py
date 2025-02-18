import os
import gzip
import pytest
from src.gzip_compressor import compress_file

def test_compress_file_default_output(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("This is a test file for compression")
    
    # Compress the file
    compressed_file = compress_file(str(test_file))
    
    # Verify compressed file was created with .gz extension
    assert compressed_file == str(test_file) + '.gz'
    assert os.path.exists(compressed_file)
    
    # Verify file can be decompressed
    with gzip.open(compressed_file, 'rt') as f:
        content = f.read()
        assert content == "This is a test file for compression"

def test_compress_file_custom_output(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Another test file")
    
    # Custom output path
    custom_output = tmp_path / "compressed_custom.gz"
    compressed_file = compress_file(str(test_file), str(custom_output))
    
    # Verify compressed file was created at custom location
    assert compressed_file == str(custom_output)
    assert os.path.exists(compressed_file)
    
    # Verify file can be decompressed
    with gzip.open(compressed_file, 'rt') as f:
        content = f.read()
        assert content == "Another test file"

def test_compress_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        compress_file("/path/to/nonexistent/file.txt")

def test_compress_directory(tmp_path):
    with pytest.raises(IsADirectoryError):
        compress_file(str(tmp_path))

def test_compress_permission_denied(monkeypatch, tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Permission test file")
    
    # Modify file permissions to simulate permission denied
    monkeypatch.setattr(os, 'path', monkeypatch.Mock(wraps=os.path))
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    
    with pytest.raises(PermissionError):
        compress_file(str(test_file))