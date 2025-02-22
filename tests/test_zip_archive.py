import os
import zipfile
import pytest
from src.zip_archive import create_zip_archive

@pytest.fixture
def sample_files(tmp_path):
    """Create sample files for testing"""
    # Create temporary files
    file1 = tmp_path / "test1.txt"
    file2 = tmp_path / "test2.txt"
    file1.write_text("Hello, World!")
    file2.write_text("Testing zip archive")
    return [str(file1), str(file2)]

def test_create_zip_archive_successful(sample_files, tmp_path):
    """Test successful zip archive creation"""
    output_zip = str(tmp_path / "archive.zip")
    result = create_zip_archive(sample_files, output_zip)
    
    # Check function returns True
    assert result is True
    
    # Verify zip file was created
    assert os.path.exists(output_zip)
    
    # Verify contents of zip file
    with zipfile.ZipFile(output_zip, 'r') as zipf:
        assert len(zipf.namelist()) == len(sample_files)
        assert 'test1.txt' in zipf.namelist()
        assert 'test2.txt' in zipf.namelist()

def test_create_zip_archive_empty_list():
    """Test handling of empty file list"""
    with pytest.raises(ValueError, match="No files provided for zip archive"):
        create_zip_archive([], "output.zip")

def test_create_zip_archive_nonexistent_file(tmp_path):
    """Test handling of nonexistent files"""
    with pytest.raises(FileNotFoundError, match="File not found"):
        create_zip_archive(["/path/to/nonexistent/file.txt"], str(tmp_path / "archive.zip"))

def test_create_zip_archive_without_zip_extension(sample_files, tmp_path):
    """Test automatic .zip extension addition"""
    output_path = str(tmp_path / "archive")
    result = create_zip_archive(sample_files, output_path)
    
    assert result is True
    assert os.path.exists(output_path + '.zip')

def test_create_zip_archive_preserves_filenames(sample_files, tmp_path):
    """Test that zip archive preserves original filenames"""
    output_zip = str(tmp_path / "archive.zip")
    result = create_zip_archive(sample_files, output_zip)
    
    with zipfile.ZipFile(output_zip, 'r') as zipf:
        # Check that only base filenames are in the archive
        assert all(os.path.basename(f) in zipf.namelist() for f in sample_files)