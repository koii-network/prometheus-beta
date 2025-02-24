import os
import pytest
import shutil
from src.text_file_creator import create_text_file

# Temporary test directory
TEST_DIR = 'test_files'

def setup_module(module):
    # Create a clean test directory before tests
    os.makedirs(TEST_DIR, exist_ok=True)

def teardown_module(module):
    # Clean up test directory after tests
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)

def test_create_empty_text_file():
    file_path = os.path.join(TEST_DIR, 'empty_file.txt')
    created_path = create_text_file(file_path)
    
    assert created_path == file_path
    assert os.path.exists(file_path)
    assert os.path.getsize(file_path) == 0

def test_create_text_file_with_content():
    file_path = os.path.join(TEST_DIR, 'file_with_content.txt')
    test_content = "Hello, World!"
    created_path = create_text_file(file_path, test_content)
    
    assert created_path == file_path
    assert os.path.exists(file_path)
    
    with open(file_path, 'r') as file:
        content = file.read()
        assert content == test_content

def test_create_file_in_nested_directory():
    file_path = os.path.join(TEST_DIR, 'nested', 'deep', 'file.txt')
    test_content = "Nested file test"
    created_path = create_text_file(file_path, test_content)
    
    assert created_path == file_path
    assert os.path.exists(file_path)
    
    with open(file_path, 'r') as file:
        content = file.read()
        assert content == test_content

def test_empty_file_path_raises_error():
    with pytest.raises(ValueError, match="File path cannot be empty"):
        create_text_file('')

def test_none_file_path_raises_error():
    with pytest.raises(ValueError, match="File path cannot be empty"):
        create_text_file(None)