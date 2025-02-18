import os
import pytest
import shutil
from src.file_backup import create_file_backup

@pytest.fixture
def sample_file(tmp_path):
    """Create a sample file for testing"""
    sample_path = tmp_path / "sample.txt"
    sample_path.write_text("Test content")
    return str(sample_path)

def test_file_backup_same_directory(sample_file):
    """Test backing up a file in the same directory"""
    backup_path = create_file_backup(sample_file)
    
    # Check backup file exists
    assert os.path.exists(backup_path)
    
    # Check backup content matches original
    with open(sample_file, 'r') as orig, open(backup_path, 'r') as backup:
        assert orig.read() == backup.read()
    
    # Check backup filename contains original filename and timestamp
    assert os.path.basename(sample_file) in os.path.basename(backup_path)
    assert backup_path.endswith('.bak')

def test_file_backup_custom_directory(sample_file, tmp_path):
    """Test backing up a file to a custom directory"""
    backup_dir = tmp_path / "backups"
    backup_path = create_file_backup(sample_file, str(backup_dir))
    
    # Check backup directory exists
    assert os.path.exists(backup_dir)
    
    # Check backup file exists in correct location
    assert os.path.exists(backup_path)
    assert backup_path.startswith(str(backup_dir))

def test_file_backup_nonexistent_file():
    """Test backing up a non-existent file raises FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        create_file_backup("/path/to/nonexistent/file.txt")

def test_file_backup_directory_error(tmp_path):
    """Test backing up a directory raises IsADirectoryError"""
    with pytest.raises(IsADirectoryError):
        create_file_backup(str(tmp_path))