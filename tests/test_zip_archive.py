import os
import pytest
import zipfile
from src.zip_archive import create_zip_archive

@pytest.fixture
def sample_files(tmp_path):
    """Create sample files for testing"""
    # Create three sample files
    files = [
        tmp_path / "file1.txt",
        tmp_path / "file2.txt", 
        tmp_path / "file3.txt"
    ]
    
    for f in files:
        f.write_text(f"Content of {f.name}")
    
    return [str(f) for f in files]

def test_create_zip_archive_success(sample_files, tmp_path):
    """Test successful zip archive creation"""
    output_path = str(tmp_path / "archive.zip")
    
    # Create zip archive
    result = create_zip_archive(sample_files, output_path)
    
    # Verify results
    assert result is True
    assert os.path.exists(output_path)
    
    # Verify zip contents
    with zipfile.ZipFile(output_path, 'r') as zipf:
        assert len(zipf.namelist()) == len(sample_files)
        for file in sample_files:
            assert os.path.basename(file) in zipf.namelist()

def test_create_zip_archive_empty_files():
    """Test creating zip archive with no files"""
    with pytest.raises(ValueError, match="At least one file must be provided"):
        create_zip_archive([], "output.zip")

def test_create_zip_archive_empty_output_path(sample_files):
    """Test creating zip archive with empty output path"""
    with pytest.raises(ValueError, match="Output path must be specified"):
        create_zip_archive(sample_files, "")

def test_create_zip_archive_nonexistent_file(tmp_path):
    """Test creating zip archive with nonexistent file"""
    output_path = str(tmp_path / "archive.zip")
    
    with pytest.raises(FileNotFoundError):
        create_zip_archive(["nonexistent_file.txt"], output_path)

def test_create_zip_archive_preserve_filename(sample_files, tmp_path):
    """Test that zip archive preserves original filenames"""
    output_path = str(tmp_path / "archive.zip")
    
    create_zip_archive(sample_files, output_path)
    
    with zipfile.ZipFile(output_path, 'r') as zipf:
        # Check that only the filename (not full path) is in the archive
        for file in sample_files:
            assert os.path.basename(file) in zipf.namelist()