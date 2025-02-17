import os
import pytest
import tempfile
from src.create_text_file import create_text_file

def test_create_empty_text_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, 'test_empty.txt')
        result = create_text_file(file_path)
        assert result == file_path
        assert os.path.exists(file_path)
        assert os.path.getsize(file_path) == 0

def test_create_text_file_with_content():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, 'test_content.txt')
        test_content = 'Hello, World!'
        result = create_text_file(file_path, test_content)
        assert result == file_path
        assert os.path.exists(file_path)
        with open(file_path, 'r') as f:
            assert f.read() == test_content

def test_create_text_file_nested_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, 'nested', 'dir', 'test_nested.txt')
        result = create_text_file(file_path)
        assert result == file_path
        assert os.path.exists(file_path)

def test_create_text_file_invalid_path():
    with pytest.raises(ValueError):
        create_text_file('')
    with pytest.raises(ValueError):
        create_text_file(None)

def test_create_text_file_existing_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, 'existing.txt')
        create_text_file(file_path)
        with pytest.raises(FileExistsError):
            create_text_file(file_path)

def test_create_text_file_with_non_string_content():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, 'test_numeric.txt')
        result = create_text_file(file_path, 42)
        assert result == file_path
        with open(file_path, 'r') as f:
            assert f.read() == '42'