import os
import zipfile
import pytest
from src.zip_archiver import create_zip_archive

@pytest.fixture
def sample_files(tmp_path):
    """Create sample files for testing"""
    # Create three sample files
    files = [
        tmp_path / 'file1.txt',
        tmp_path / 'file2.txt',
        tmp_path / 'file3.txt'
    ]
    
    for f in files:
        f.write_text(f"Content of {f.name}")
    
    return [str(f) for f in files]

def test_create_zip_archive_success(sample_files, tmp_path):
    """Test successful zip archive creation"""
    output_path = str(tmp_path / 'test_archive.zip')
    result = create_zip_archive(sample_files, output_path)
    
    assert result is True
    assert os.path.exists(output_path)
    
    # Verify zip contents
    with zipfile.ZipFile(output_path, 'r') as zipf:
        assert set(zipf.namelist()) == set(os.path.basename(f) for f in sample_files)

def test_create_zip_archive_no_extension(sample_files, tmp_path):
    """Test zip archive creation without .zip extension"""
    output_path = str(tmp_path / 'test_archive')
    result = create_zip_archive(sample_files, output_path)
    
    assert result is True
    assert os.path.exists(output_path + '.zip')

def test_create_zip_archive_empty_files():
    """Test creating zip archive with empty files list"""
    with pytest.raises(ValueError, match="No files provided for zip archive"):
        create_zip_archive([], 'output.zip')

def test_create_zip_archive_nonexistent_file():
    """Test creating zip archive with nonexistent file"""
    with pytest.raises(FileNotFoundError, match="File not found"):
        create_zip_archive(['nonexistent_file.txt'], 'output.zip')