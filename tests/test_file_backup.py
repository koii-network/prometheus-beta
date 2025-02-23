import os
import pytest
import tempfile
import shutil
import time
from src.file_backup import backup_file

def test_backup_file_default_location():
    # Create a temporary file to backup
    with tempfile.NamedTemporaryFile(delete=False) as temp_source:
        temp_source.write(b"Test content")
        temp_source.close()
    
    try:
        # Backup the file
        backup_path = backup_file(temp_source.name)
        
        # Verify backup was created
        assert os.path.exists(backup_path)
        assert os.path.getsize(backup_path) == os.path.getsize(temp_source.name)
        
        # Verify backup is in the same directory
        assert os.path.dirname(backup_path) == os.path.dirname(temp_source.name)
    finally:
        # Clean up
        os.unlink(temp_source.name)
        if os.path.exists(backup_path):
            os.unlink(backup_path)

def test_backup_file_custom_location():
    # Create a temporary file to backup
    with tempfile.NamedTemporaryFile(delete=False) as temp_source:
        temp_source.write(b"Test content")
        temp_source.close()
    
    # Create a temporary directory for backup
    backup_dir = tempfile.mkdtemp()
    
    try:
        # Backup the file to custom location
        backup_path = backup_file(temp_source.name, backup_dir)
        
        # Verify backup was created
        assert os.path.exists(backup_path)
        assert os.path.getsize(backup_path) == os.path.getsize(temp_source.name)
        
        # Verify backup is in the specified directory
        assert os.path.dirname(backup_path) == backup_dir
    finally:
        # Clean up
        os.unlink(temp_source.name)
        shutil.rmtree(backup_dir)

def test_backup_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        backup_file("/path/to/nonexistent/file.txt")

def test_backup_directory_instead_of_file():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    
    try:
        with pytest.raises(ValueError):
            backup_file(temp_dir)
    finally:
        shutil.rmtree(temp_dir)

def test_multiple_backups_unique_names():
    # Create a temporary file to backup
    with tempfile.NamedTemporaryFile(delete=False) as temp_source:
        temp_source.write(b"Test content")
        temp_source.close()
    
    try:
        # Create multiple backups quickly
        backup1 = backup_file(temp_source.name)
        # Wait a moment to ensure timestamp changes
        time.sleep(0.01)
        backup2 = backup_file(temp_source.name)
        
        # Verify backup paths are different by extracting timestamp
        timestamp1 = backup1.split('.')[-1]
        timestamp2 = backup2.split('.')[-1]
        
        assert timestamp1 != timestamp2, "Backup filenames should have different timestamps"
    finally:
        # Clean up
        os.unlink(temp_source.name)
        if os.path.exists(backup1):
            os.unlink(backup1)
        if os.path.exists(backup2):
            os.unlink(backup2)