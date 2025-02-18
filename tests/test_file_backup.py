import os
import pytest
import tempfile
import shutil
from src.file_backup import create_file_backup

def test_create_file_backup_same_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Test content")
        temp_file_path = temp_file.name
    
    try:
        # Create backup
        backup_path = create_file_backup(temp_file_path)
        
        # Verify backup file exists
        assert os.path.exists(backup_path)
        assert backup_path.startswith(temp_file_path)
        assert backup_path.endswith('.bak')
        
        # Verify backup content
        with open(backup_path, 'rb') as backup_file:
            assert backup_file.read() == b"Test content"
    
    finally:
        # Clean up
        os.unlink(temp_file_path)
        if os.path.exists(backup_path):
            os.unlink(backup_path)

def test_create_file_backup_custom_directory():
    # Create a temporary file and a backup directory
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Test content")
        temp_file_path = temp_file.name
    
    backup_dir = tempfile.mkdtemp()
    
    try:
        # Create backup in custom directory
        backup_path = create_file_backup(temp_file_path, backup_dir)
        
        # Verify backup file exists in correct location
        assert os.path.exists(backup_path)
        assert os.path.dirname(backup_path) == backup_dir
        assert backup_path.endswith('.bak')
        
        # Verify backup content
        with open(backup_path, 'rb') as backup_file:
            assert backup_file.read() == b"Test content"
    
    finally:
        # Clean up
        os.unlink(temp_file_path)
        if os.path.exists(backup_path):
            os.unlink(backup_path)
        shutil.rmtree(backup_dir)

def test_create_file_backup_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        create_file_backup("/path/to/nonexistent/file.txt")

def test_create_file_backup_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(IsADirectoryError):
            create_file_backup(temp_dir)