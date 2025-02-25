import os
import zipfile
import pytest
import tempfile
import shutil

from src.zip_archiver import create_zip_archive


@pytest.fixture
def temp_files():
    """Create temporary files for testing."""
    temp_dir = tempfile.mkdtemp()
    try:
        # Create sample files
        files = [
            os.path.join(temp_dir, 'test1.txt'),
            os.path.join(temp_dir, 'test2.txt')
        ]
        
        for file in files:
            with open(file, 'w') as f:
                f.write(f"Content for {os.path.basename(file)}")
        
        yield files
    finally:
        # Clean up temporary directory
        shutil.rmtree(temp_dir)


def test_create_zip_archive_success(temp_files):
    """Test successful creation of zip archive."""
    output_zip = os.path.join(tempfile.gettempdir(), 'test_archive.zip')
    
    # Create zip archive
    result = create_zip_archive(temp_files, output_zip)
    
    # Verify creation
    assert result is True
    assert os.path.exists(output_zip)
    
    # Verify contents of zip file
    with zipfile.ZipFile(output_zip, 'r') as zipf:
        assert set(zipf.namelist()) == set(os.path.basename(f) for f in temp_files)
    
    # Clean up
    os.remove(output_zip)


def test_create_zip_archive_auto_extension(temp_files):
    """Test zip archive creation with automatic .zip extension."""
    output_path = os.path.join(tempfile.gettempdir(), 'test_archive')
    
    # Create zip archive
    result = create_zip_archive(temp_files, output_path)
    
    # Verify creation
    assert result is True
    assert os.path.exists(output_path + '.zip')
    
    # Clean up
    os.remove(output_path + '.zip')


def test_create_zip_archive_no_files():
    """Test error handling when no files are provided."""
    with pytest.raises(ValueError, match="At least one file must be provided"):
        create_zip_archive([], 'output.zip')


def test_create_zip_archive_nonexistent_file(temp_files):
    """Test error handling for nonexistent files."""
    nonexistent_file = '/path/to/nonexistent/file.txt'
    with pytest.raises(FileNotFoundError, match=f"File not found: {nonexistent_file}"):
        create_zip_archive(temp_files + [nonexistent_file], 'output.zip')