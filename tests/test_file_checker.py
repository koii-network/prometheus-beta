import os
import pytest
from src.file_checker import file_exists

def test_file_exists_returns_true_for_existing_file():
    # Use an existing file in the repository for testing
    assert file_exists('README.md') == True
    assert file_exists('requirements.txt') == True

def test_file_exists_returns_false_for_nonexistent_file():
    assert file_exists('nonexistent_file.txt') == False

def test_file_exists_handles_absolute_path():
    current_dir = os.path.abspath(os.curdir)
    existing_file_path = os.path.join(current_dir, 'README.md')
    assert file_exists(existing_file_path) == True

def test_file_exists_handles_empty_string():
    assert file_exists('') == False

def test_file_exists_handles_none_input():
    with pytest.raises(TypeError):
        file_exists(None)