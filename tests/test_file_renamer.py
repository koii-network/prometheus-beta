import os
import pytest
import tempfile
from src.file_renamer import rename_file

def test_rename_file_success():
    # Create a temporary directory and file
    with tempfile.TemporaryDirectory() as tmpdir:
        source_path = os.path.join(tmpdir, 'original.txt')
        destination_path = os.path.join(tmpdir, 'renamed.txt')
        
        # Create source file
        with open(source_path, 'w') as f:
            f.write('Test content')
        
        # Rename the file
        result = rename_file(source_path, destination_path)
        
        # Assert the file was renamed
        assert result is True
        assert os.path.exists(destination_path)
        assert not os.path.exists(source_path)

def test_rename_file_nonexistent_source():
    with tempfile.TemporaryDirectory() as tmpdir:
        source_path = os.path.join(tmpdir, 'nonexistent.txt')
        destination_path = os.path.join(tmpdir, 'renamed.txt')
        
        # Attempt to rename a non-existent file
        with pytest.raises(FileNotFoundError):
            rename_file(source_path, destination_path)

def test_rename_file_destination_exists():
    with tempfile.TemporaryDirectory() as tmpdir:
        source_path = os.path.join(tmpdir, 'original.txt')
        destination_path = os.path.join(tmpdir, 'existing.txt')
        
        # Create source and destination files
        with open(source_path, 'w') as f:
            f.write('Source content')
        with open(destination_path, 'w') as f:
            f.write('Existing content')
        
        # Attempt to rename to an existing file
        with pytest.raises(FileExistsError):
            rename_file(source_path, destination_path)