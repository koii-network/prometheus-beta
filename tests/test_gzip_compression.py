import os
import gzip
import pytest
from src.gzip_compression import compress_file

@pytest.fixture
def sample_file(tmp_path):
    """Create a sample file for testing"""
    sample_content = "This is a test file for gzip compression"
    file_path = tmp_path / "sample_file.txt"
    file_path.write_text(sample_content)
    return str(file_path)

def test_compress_file_default_output(sample_file, tmp_path):
    """Test compression with default output filename"""
    compressed_file = compress_file(sample_file)
    
    # Check compressed file exists
    assert os.path.exists(compressed_file)
    assert compressed_file == sample_file + '.gz'
    
    # Verify compression worked
    with gzip.open(compressed_file, 'rt') as f:
        content = f.read()
        assert content == "This is a test file for gzip compression"

def test_compress_file_custom_output(sample_file, tmp_path):
    """Test compression with custom output filename"""
    custom_output = str(tmp_path / "custom_compressed.gz")
    compressed_file = compress_file(sample_file, custom_output)
    
    # Check compressed file exists
    assert os.path.exists(compressed_file)
    assert compressed_file == custom_output
    
    # Verify compression worked
    with gzip.open(compressed_file, 'rt') as f:
        content = f.read()
        assert content == "This is a test file for gzip compression"

def test_nonexistent_file():
    """Test that FileNotFoundError is raised for non-existent file"""
    with pytest.raises(FileNotFoundError):
        compress_file("nonexistent_file.txt")

def test_file_permissions(monkeypatch, sample_file):
    """Test handling of permission errors"""
    def mock_open(*args, **kwargs):
        raise PermissionError("Mocked permission error")
    
    monkeypatch.setattr('builtins.open', mock_open)
    
    with pytest.raises(PermissionError):
        compress_file(sample_file)