import os
import pytest
import tempfile
from pathlib import Path
from src.recent_file_finder import find_most_recent_file

def test_find_most_recent_file_basic():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create multiple files with different modification times
        file1 = Path(tmpdir) / 'file1.txt'
        file2 = Path(tmpdir) / 'file2.txt'
        
        file1.touch()
        os.utime(file1, (os.path.getatime(file1), os.path.getctime(file1) - 100))
        file2.touch()
        
        result = find_most_recent_file(tmpdir)
        assert result == str(file2)

def test_empty_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        result = find_most_recent_file(tmpdir)
        assert result is None

def test_invalid_directory():
    with pytest.raises(ValueError):
        find_most_recent_file('/nonexistent/path')

def test_file_input_not_directory():
    with tempfile.NamedTemporaryFile() as tmpfile:
        with pytest.raises(ValueError):
            find_most_recent_file(tmpfile.name)

def test_multiple_recent_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        file1 = Path(tmpdir) / 'file1.txt'
        file2 = Path(tmpdir) / 'file2.txt'
        
        file1.touch()
        file2.touch()
        
        result = find_most_recent_file(tmpdir)
        assert result in [str(file1), str(file2)]  # Either file could be considered most recent

def test_directory_as_path_object():
    with tempfile.TemporaryDirectory() as tmpdir:
        Path(tmpdir, 'file1.txt').touch()
        result = find_most_recent_file(Path(tmpdir))
        assert result == os.path.join(tmpdir, 'file1.txt')