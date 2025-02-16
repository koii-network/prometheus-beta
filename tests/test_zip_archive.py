import os
import pytest
import zipfile
from src.zip_archive import create_zip_archive

@pytest.fixture
def sample_files(tmp_path):
    """Create sample files for testing"""
    # Create directory for test files
    test_dir = tmp_path / "test_files"
    test_dir.mkdir()
    
    # Create sample files
    file1 = test_dir / "test1.txt"
    file1.write_text("Content of test1")
    
    file2 = test_dir / "test2.txt"
    file2.write_text("Content of test2")
    
    return [str(file1), str(file2)]

def test_create_zip_archive(sample_files, tmp_path):
    """Test creating a zip archive with multiple files"""
    archive_path = str(tmp_path / "test_archive.zip")
    result = create_zip_archive(sample_files, archive_path)
    
    # Check return value
    assert result == archive_path
    
    # Verify zip file was created
    assert os.path.exists(archive_path)
    
    # Check contents of zip file
    with zipfile.ZipFile(archive_path, 'r') as zipf:
        assert set(zipf.namelist()) == {'test1.txt', 'test2.txt'}
        assert zipf.read('test1.txt') == b"Content of test1"
        assert zipf.read('test2.txt') == b"Content of test2"

def test_create_zip_archive_no_files():
    """Test creating zip archive with no files raises ValueError"""
    with pytest.raises(ValueError, match="At least one file must be specified"):
        create_zip_archive([], "test.zip")

def test_create_zip_archive_invalid_filename():
    """Test creating zip archive with invalid filename raises ValueError"""
    with pytest.raises(ValueError, match="Archive name must end with .zip"):
        create_zip_archive(["dummy.txt"], "test")

def test_create_zip_archive_nonexistent_file():
    """Test creating zip archive with nonexistent file raises FileNotFoundError"""
    with pytest.raises(FileNotFoundError, match="File not found: nonexistent.txt"):
        create_zip_archive(["nonexistent.txt"], "test.zip")

def test_create_zip_archive_single_file(tmp_path):
    """Test creating zip archive with a single file"""
    test_file = tmp_path / "single_test.txt"
    test_file.write_text("Single file content")
    
    archive_path = str(tmp_path / "single_archive.zip")
    result = create_zip_archive([str(test_file)], archive_path)
    
    assert result == archive_path
    
    with zipfile.ZipFile(archive_path, 'r') as zipf:
        assert zipf.namelist() == ['single_test.txt']
        assert zipf.read('single_test.txt') == b"Single file content"