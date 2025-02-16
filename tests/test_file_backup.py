import os
import pytest
import tempfile
from src.file_backup import create_file_backup

def test_create_file_backup_default_location():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Test content")
        temp_file_path = temp_file.name
    
    try:
        # Create backup
        backup_path = create_file_backup(temp_file_path)
        
        # Verify backup was created
        assert os.path.exists(backup_path)
        assert backup_path.startswith(temp_file_path)
        assert backup_path.endswith('.bak')
        
        # Verify backup content matches original
        with open(temp_file_path, 'rb') as orig, open(backup_path, 'rb') as backup:
            assert orig.read() == backup.read()
    
    finally:
        # Cleanup
        os.unlink(temp_file_path)
        if os.path.exists(backup_path):
            os.unlink(backup_path)

def test_create_file_backup_custom_location():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Test content")
        temp_file_path = temp_file.name
    
    # Create a temporary backup directory
    with tempfile.TemporaryDirectory() as backup_dir:
        try:
            # Create backup in custom location
            backup_path = create_file_backup(temp_file_path, backup_dir)
            
            # Verify backup was created in custom location
            assert os.path.exists(backup_path)
            assert os.path.dirname(backup_path) == backup_dir
            assert backup_path.endswith('.bak')
            
            # Verify backup content matches original
            with open(temp_file_path, 'rb') as orig, open(backup_path, 'rb') as backup:
                assert orig.read() == backup.read()
        
        finally:
            # Cleanup
            os.unlink(temp_file_path)

def test_backup_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        create_file_backup('/path/to/nonexistent/file.txt')

def test_backup_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(IsADirectoryError):
            create_file_backup(temp_dir)