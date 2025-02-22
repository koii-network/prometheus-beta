import os
import pytest
import tempfile
from src.file_backup import create_file_backup

def test_create_file_backup():
    # Create a temporary file for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file_path = os.path.join(temp_dir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write("Test content")
        
        # Create backup in the same directory
        backup_path = create_file_backup(test_file_path)
        
        # Verify backup was created
        assert os.path.exists(backup_path)
        assert backup_path.endswith('.bak')
        assert os.path.getsize(backup_path) == os.path.getsize(test_file_path)

def test_create_backup_to_custom_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file_path = os.path.join(temp_dir, 'test_file.txt')
        backup_dir = os.path.join(temp_dir, 'backups')
        
        with open(test_file_path, 'w') as f:
            f.write("Test content")
        
        # Create backup in a custom directory
        backup_path = create_file_backup(test_file_path, backup_dir)
        
        # Verify backup was created in the specified directory
        assert os.path.exists(backup_path)
        assert backup_path.startswith(backup_dir)
        assert backup_path.endswith('.bak')

def test_backup_nonexistent_file():
    # Test backing up a file that doesn't exist
    with pytest.raises(FileNotFoundError):
        create_file_backup('nonexistent_file.txt')

def test_backup_invalid_path():
    # Test with invalid path input
    with pytest.raises(ValueError):
        create_file_backup(None)
        create_file_backup('')